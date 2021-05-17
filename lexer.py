#######################################
# IMPORTS
#######################################

from strings_with_arrows import *


TT_INT       = 'INT'
TT_FLOAT    = 'FLOAT'
TT_PLUS     = 'TAMBAH'
TT_MINUS    = 'KURANG'
TT_MUL      = 'KALI'
TT_DIV      = 'BAGI'
TT_POW      = 'POW'
TT_LPAREN   = 'KIKURUNG'
TT_RPAREN   = 'KAKURUNG'
TT_EOF      = 'EOF'

class Token:
    def __init__(self, tipe_, value=None, posisi_awal=None, posisi_akhir=None):
        self.tipe = tipe_
        self.value = value

        if posisi_awal:
            self.posisi_awal = posisi_awal.salin()
            self.posisi_akhir = posisi_awal.salin()
            self.posisi_akhir.maju()

        if posisi_akhir:
            self.posisi_akhir = posisi_akhir
    
    def __repr__(self):
        if self.value: return f'{self.tipe}:{self.value}'
        return f'{self.tipe}'

#######################################
# LEXER
#######################################

class Lexer:
    def __init__(self, nama_file, teks):
        self.nama_file = nama_file
        self.teks = teks
        self.posisi = Position(-1, 0, -1, nama_file, teks)
        self.current_char = None
        self.maju()
    
    def maju(self):
        self.posisi.maju(self.current_char)
        self.current_char = self.teks[self.posisi.idx] if self.posisi.idx < len(self.teks) else None

    def buatTokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.maju()
            elif self.current_char in DIGITS:
                tokens.append(self.buatNomor())
            elif self.current_char == '+':
                tokens.append(Token(TT_TAMBAH, posisi_awal=self.posisi))
                self.maju()
            elif self.current_char == '-':
                tokens.append(Token(TT_KURANG, posisi_awal=self.posisi))
                self.maju()
            elif self.current_char == '*':
                tokens.append(Token(TT_KALI, posisi_awal=self.posisi))
                self.maju()
            elif self.current_char == '/':
                tokens.append(Token(TT_BAGI, posisi_awal=self.posisi))
                self.maju()
            elif self.current_char == '^':
                tokens.append(Token(TT_POW, posisi_awal=self.posisi))
                self.maju()
            elif self.current_char == '(':
                tokens.append(Token(TT_KIKURUNG, posisi_awal=self.posisi))
                self.maju()
            elif self.current_char == ')':
                tokens.append(Token(TT_KAKURUNG, posisi_awal=self.posisi))
                self.maju()
            else:
                posisi_awal = self.posisi.salin()
                char = self.current_char
                self.maju()
                return [], IllegalCharError(posisi_awal, self.posisi, "'" + char + "'")

        tokens.append(Token(TT_EOF, posisi_awal=self.pos))
        return tokens, None

    def buatNomor(self):
        angkaString = ''
        jumlahAngka = 0
        posisi_awal = self.posisi.salin()

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if jumlahAngka == 1: break
                jumlahAngka += 1
                angkaString += '.'
            else:
                angkaString += self.current_char
            self.maju()

        if jumlahAngka == 0:
            return Token(TT_INT, int(angkaString), posisi_awal, self.posisi)
        else:
            return Token(TT_FLOAT, float(angkaString), posisi_awal, self.posisi)