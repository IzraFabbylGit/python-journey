"""
ini merupakan sesi untuk belajar,eksperimenting, dan project untuk
topic string dulu, dipandu dengan claude AI
"""

a = "ini adalah STRING pertama"
a2 = "INI ADALAH STRING PERTAMA"

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

# 6. .JOIN() -> untuk menggabungkan list menjadi string dengan pemisah tertentu
"""caranya dengan menambahkan ".join(list/yang sudah di split sebelumnya)" pada variabel 
string yang ingin digunakan sebagai pemisah 
join_a = (di isi dengan separator yang akan digunakan pada hasil stringnya).join(split_a)
"""
# DARI LIST MENJADI STRING DARI TIAP ELEMENTNYA

join_a = " ".join(split_a)
print(f"6. list {split_a} setelah digunakan join menjadi string adalah \n'{join_a}'")

# 7. .FIND() -> untuk mencari index dari karakter tertentu pada string
""" caranya dengan menambahkan ".find('karakter yang dicari')" pada variabel string yang ingin dicari
    MENCARINYA DIMULAI DARI O, JADI KALAU UDAH KETEMU MAKA AKAN MENGEMBALIKAN NILAI INDEXNYA, 
    JIKA TIDAK DITEMUKAN MAKA AKAN MENGEMBALIKAN NILAI -1
"""
find_a = a.find("adalah")
print(
    f"7. index dari karakter 'adalah' pada string '{a}' adalah {find_a} (dimulai dari 0)"
)

# KETIKA KARATKER YANG DICARI TIDAK ADA PADA STRING MAKA AKAN MENGEMBALIKAN NILAI -1
find_a2 = a.find("yanto")
print(
    f"7. index dari karakter 'yanto' pada string '{a}' adalah {find_a2} (dimulai dari 0)"
)


# 8. .COUNT() -> untuk menghitung jumlah karakter tertentu pada string
""" caranya dengan menambahkan ".count('karakter yang dihitung')" pada variabel string  
    MENGHITUNGNYA DIMULAI DARI O, JADI KALAU ADA MAKA AKAN MENGEMBALIKAN NILAI JUMLAHNYA, 
    JIKA TIDAK ADA MAKA AKAN MENGEMBALIKAN NILAI 0
    pengunaan count ini sensitif terhadap huruf kapital dan kecil, jadi jika ingin 
    menghitung jumlah karakter tertentu pada string tanpa memperhatikan huruf kapital 
    dan kecil maka harus diubah dulu menjadi huruf kapital semua atau huruf kecil semua
"""

count_a = a.count("I")
print(f"8. jumlah karakter 'I' pada string '{a}' adalah {count_a}")

# Kalau karakter yang dicari gada samsek
count_a2 = a.count("0")
print(f"8. jumlah karakter '0' pada string '{a}' adalah {count_a2}")

# 9. .startswith() -> untuk mengecek apakah string diawali dengan karakter tertentu
""" caranya dengan menambahkan ".startswith('karakter yang dicek')" pada variabel string    
    MENGECEKNYA DIMULAI DARI O, JADI KALAU ADA MAKA AKAN MENGEMBALIKAN NILAI TRUE, 
    JIKA TIDAK ADA MAKA AKAN MENGEMBALIKAN NILAI FALSE
    HASILNYA BERUPA BOOLEAN
"""
startswith_a = a.startswith("ini")
print(f"9. apakah string '{a}' diawali dengan 'ini'? {startswith_a}")

# 10. .endswith() -> untuk mengecek apakah string diakhiri dengan karakter tertentu
""" caranya dengan menambahkan ".endswith('karakter yang dicek')" pada variabel string    
    MENGECEKNYA DIMULAI DARI O, JADI KALAU ADA MAKA AKAN MENGEMBALIKAN NILAI TRUE, 
    JIKA TIDAK ADA MAKA AKAN MENGEMBALIKAN NILAI FALSE
    HASILNYA BERUPA BOOLEAN
    DIA NGECEKNYA KARAKTER TERAKHIR BANGET EVEN ITU SATU KARAKTER AJA
"""
endswith_a = a.endswith("p")
print(f"10. apakah string '{a}' diakhiri dengan 'p'? {endswith_a}")

# 11. .isupper() -> untuk mengecek apakah string semuanya huruf kapital
""" caranya dengan menambahkan ".isupper()" pada variabel string    
    MENGECEKNYA DIMULAI DARI O, JADI KALAU ADA MAKA AKAN MENGEMBALIKAN NILAI TRUE, 
    JIKA TIDAK ADA MAKA AKAN MENGEMBALIKAN NILAI FALSE
    HASILNYA BERUPA BOOLEAN
"""

isupper_a2 = a2.isupper()
print(f"11. apakah string '{a2}' semuanya huruf kapital? {isupper_a2}")

# 12. .islower() -> untuk mengecek apakah string semuanya huruf kecil
""" caranya dengan menambahkan ".islower()" pada variabel string
    MENGECEKNYA DIMULAI DARI O, JADI KALAU ADA MAKA AKAN MENGEMBALIKAN NILAI TRUE, 
    JIKA TIDAK ADA MAKA AKAN MENGEMBALIKAN NILAI FALSE
    HASILNYA BERUPA BOOLEAN
"""
islower_a = a.islower()
print(f"12. apakah string '{a}' semuanya huruf kecil? {islower_a}")

islower_a2 = a2.islower()
print(f"12. apakah string '{a2}' semuanya huruf kecil? {islower_a2}")

# 13. .capitalize() -> untuk mengubah huruf pertama menjadi huruf kapital
""" caranya dengan menambahkan ".capitalize()" pada variabel string
    Dengan sisanya menjadi hurus kecil semua, dan spasi awal string akan dihapus
"""

capitalize_a = a.capitalize()
print(
    f"13. string '{a}' setelah diubah menjadi huruf pertama kapital adalah '{capitalize_a}'"
)


# 14. .title() -> untuk mengubah huruf pertama dari setiap kata menjadi huruf kapital
""" caranya dengan menambahkan ".title()" pada variabel string
    Dengan sisanya menjadi hurus kecil semua
"""
title_a = a.title()
print(
    f"14. string '{a}' setelah diubah, huruf pertama dari setiap kata menjadi kapital adalah '{title_a}'"
)

"""
    KURANG LEBIH SESI STRING ITU DULU YANG PERLU DIKETAHUI.
    BAGIAN INI AKAN DIUPDATE TERUS SEIRING DENGAN BERJALANNYA WAKTU DAN PENGALAMAN SAYA DALAM BELAJAR PYTHON.    
"""
