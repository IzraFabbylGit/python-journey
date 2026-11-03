"""
ini merupakan sesi untuk belajar,eksperimenting, dan project untuk
topic string dulu, dipandu dengan claude AI
"""

a = "ini adalah STRING pertama"

print(type(a))

isinstance = isinstance(a, str)
print(isinstance)

# mengecek panjang atau jumlah karakter pada string
# spasi dihitung sebagai karakter pada string
b = len(a)
print(b)

# interpolation pada string / biasa disebut juga dengan f string
# f string ditandai dengan {} pada variabel yang akan dimasukan
c = f"Panjang dari string '{a}' adalah {b} karakter."
print(c)

# STRING SLICING ATAU INDEXING PADA STRING
# INDEKS STRING DIMULAI DARI 0 DAN BISA DILAKUKAN INDEXING TERBALIK DENGAN -1
""" a [Start:Stop:Step]
Dengan nilai default pada star merupakan 0, stop merupakan len string, dan step 1
"""

stringslicing_a = a[:3]
print(f"substring dari a untuk [:3] adalah  '{stringslicing_a}'")

# slicing dengan step mundur
slicingstringmundur_a = a[::-2]
print(f"substring dari a untuk [::-2] adalah  '{slicingstringmundur_a}'")

"""terlihat bahwa jika step pad slicing dibuat -1 maka memunculkan efek cermin pada hasilnya
"""

print(""" ------------------
BERIKUT MERUPAKAN BEBERAPA METHOD ATAU FUNGSI YAG BIASA DIGUNAKAN PADA STRING
-----------------
""")

# 1. . UPPER() -> untuk mengubah string menjadi huruf kapital semua
# caranya dengan menambahkan ".upper()" pada variabel string yang ingin diubah

upper_a = a.upper()
print(f"1. string '{a}' setelah diubah menjadi huruf kapital semua adalah '{upper_a}'")

# 2. .lower() -> untuk mengubah string menjadi huruf kecil semua
# caranya dengan menambahkan ".lower()" pada variabel string yang ingin diubah

lower_a = a.lower()
print(f"2. string '{a}' setelah diubah menjadi huruf kecil semua adalah '{lower_a}'")

# 3. .STRIP() -> untuk menghapus spasi pada awal dan akhir string
# ternyata strip sensitif dengan capslock dan hruf kapitalnya

strip_a = a.strip()
print(
    f"3. string '{a}' setelah dihapus spasi pada awal dan akhir string adalah \n'{strip_a}'"
)

# 4. .REPLACE() -> untuk mengganti karakter pada string dengan karakter lain
# caranya dengan menambahkan ".replace('karakter lama','karakter baru')" pada variabel string yang ingin diubah

replace_a = a.replace("ini", "HIYAAAAA")
print(f"4. string '{a}' setelah digunakan replace adalah \n'{replace_a}'")

# 5. .SPLIT() -> untuk memisahkan string menjadi list dengan pemisah tertentu
# caranya dengan menambahkan ".split('pemisah')" pada variabel
# HASIL AKHIR DARI PENGGUNAAN SPLIT BERUPA LIST DENGAN TIAP ELEMENNYA DIPISAHKAN OLEH SEPARATOR YANG
# TELAH DITENTUKAN SEBELUMNYA.

split_a = a.split(" ")
print(f"5. string '{a}' setelah digunakan split adalah \n{split_a}")
