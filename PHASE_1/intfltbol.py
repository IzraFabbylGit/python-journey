"""PADA SECTION INI KITA AKAN MENGULAS DAN MEMPELAJARI TENTNAG
INTEGER, FLOAT, BOOLEAN, DAN OPERATOR LOGIKA PADA BAHASA PEMROGRAMAN PYTHON
"""

# INTEGER DAN FLOAT
""" INTEGER ADALAH BILANGAN BULAT DAN FLOAT ADALAH BILANGAN DESIMAL,
    Pada float menggunakan titik sebagai tanda komanya. 
"""
a = 1
print(type(a))

b = 3.145873684
print(type(b))

# kita bisa melakukan pembulatan pada float dengan fungsi berikut
c = round(b, 2)  # pembulatan ke 2 angka di belakang koma
print(c)

# absolut, dalam artian absolut sejatinya, nilai minus menjadi plus

d = -10
print(abs(d))

# power, untuk menghitung pangkat dari suatu bilangan
# pow (basis,pangkat,modulus) modulus bersifat opsional

e = pow(125, 3, 3)
print(e)

print("\n ini merupakan augmented assigment \n")
# Adanya yang namanya augemnted assignment
# +=, -=, *=, /=, //=, **=, %=
a += 5
print(a)
b -= 1
print(b)
d *= 2
print(d)
f = 35
f //= 5
print(f)  # hasilnya berupa integer
f /= 5
print(f)  # hasilnya berupa float
g = 50
g **= 3  # ini merupakan perpangkatkan dari variabel sebelumnya
print(g)

print("""\n Ini merupakan bahasan mengenai boolean
      \n""")

""" Boolean merupakan ekspresi yang menyatakan falase atau true dari sebuah/sesuatu"""

# "=" menyatakan nilai yang sama
# "!=" menyatakan not equal
# ">" menyatkaan lebih besar dari
# "<" menyatakan lebih kecil dari
# ">=" menyatkaan lebih besar dan sama dengan dari
# "<=" menyatakan lebih kecil dan sama dengan dari

# cara mengecek boolean
aku = 1
dia = 2


git add .
git commit -m "intfloatbool"
git push