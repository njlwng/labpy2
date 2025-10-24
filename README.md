# Praktikum 2 - Kondisional dan Perulangan
Nama        : Najla Wening Khairunnisa 

Nim         : 312510225

Mata Kuliah : Pengantar Pemrograman  

Dosen       : Agung Nugroho, M.Kom

## PRAKTIKUM 2 - Kondisional dan Perulangan

## 🎯 Tujuan
Untuk memahami dan mempraktikkan penggunaan **struktur kondisi** (`if`, `elif`, `else`) dan **struktur perulangan** (`for`, `while`) dalam bahasa pemrograman Python.  

## 📂 Struktur Folder

Praktikum2 (labpy2)


├── README.md

├── kondisi_if/

     ├── latihan1.py

     └── latihan2.py

├──perulangan/ 

    ├── latihan1.py
  
    └── latihan2.py

## 🧩 LAB 2 – STRUKTUR KONDISI

### 🔹 Latihan 1 – Menentukan Bilangan Terbesar
**Deskripsi:**  
Membuat program untuk menentukan bilangan terbesar dari empat bilangan input.

**Kode Program:**
```python
print("Menentukan bilangan terbesar dari 4 bilangan")
a = int(input("Masukkan bilangan 1: "))
b = int(input("Masukkan bilangan 2: "))
c = int(input("Masukkan bilangan 3: "))
d = int(input("Masukkan bilangan 4: "))

terbesar = a
if b > terbesar:
    terbesar = b
if c > terbesar:
    terbesar = c
if d > terbesar:
    terbesar = d
print("Bilangan terbesar adalah:", terbesar)

```
Screenshoot
[Latihan 1 Kondisi If](img/latihan1_kondisi_if)

## Penjelasan
Program ini menggunakan struktur if untuk membandingkan empat bilangan.
Setiap kondisi akan mengganti nilai terbesar bila ditemukan angka yang lebih besar

**Flowchart:**
┌───────────────────────────┐
│          Mulai            │
└─────────────┬─────────────┘
              ↓
      Input a, b, c, d
              ↓
     terbesar = a
              ↓
     ┌───────────────────────┐
     │ Apakah b > terbesar ? │
     └────────┬──────────────┘
              │Ya
              ▼
       terbesar = b
              │
              ▼
     ┌───────────────────────┐
     │ Apakah c > terbesar ? │
     └────────┬──────────────┘
              │Ya
              ▼
       terbesar = c
              │
              ▼
     ┌───────────────────────┐
     │ Apakah d > terbesar ? │
     └────────┬──────────────┘
              │Ya
              ▼
       terbesar = d
              ↓
 Tampilkan "Bilangan Terbesar"
              ↓
┌───────────────────────────┐
│          Selesai          │
└───────────────────────────┘

### 🔹 Latihan 2 – Mengurutkan Bilangan
**Deskripsi:**  
Membuat program untuk mengurutkan tiga bilangan dari terkecil ke terbesar.

**Kode Program:**
```python
print("Mengurutkan tiga bilangan")
x = int(input("Masukkan bilangan pertama: "))
y = int(input("Masukkan bilangan kedua: "))
z = int(input("Masukkan bilangan ketiga: "))

data = [x, y, z]
data.sort()

print("Urutan dari terkecil ke terbesar:", data)
```
Screenshoot
[Latihan 2 Kondisi If](img/latihan2_kondisi_if)

**Flowchart:**
┌───────────────────────────┐
│          Mulai            │
└─────────────┬─────────────┘
              ↓
        Input x, y, z
              ↓
 Masukkan ke list [x, y, z]
              ↓
   Urutkan dengan sort()
              ↓
Tampilkan hasil urutan list
              ↓
┌───────────────────────────┐
│          Selesai          │
└───────────────────────────┘

## 🧩 LAB 3 – PERULANGAN
### 🔹Latihan 1 – Pola Segitiga Bintang
**Deskripsi:**
Membuat program dengan perulangan bertingkat (nested loop) untuk mencetak pola segitiga bintang.

**Kode Program:**
```python
print("Pola segitiga bintang")
n = int(input("Masukkan tinggi segitiga: "))

for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()
```
Screenshoot
[Latihan 1 Perulangan](img/latihan1_perulangan)

**Flowchart:**
┌───────────────────────────┐
│          Mulai            │
└─────────────┬─────────────┘
              ↓
    Input n (tinggi segitiga)
              ↓
          i = 1
              ↓
     ┌──────────────────────┐
     │ Apakah i ≤ n ?       │
     └───────┬──────────────┘
             │Ya
             ▼
           j = 1
             ↓
       ┌───────────────────┐
       │ Apakah j ≤ i ?    │
       └──────┬────────────┘
              │Ya
              ▼
         Cetak "*" tanpa enter
              ↓
            j = j + 1
              ↑
              │
       ┌──────┘
       │ Tidak
       ▼
     Cetak enter (pindah baris)
              ↓
           i = i + 1
              ↑
              │
     ┌────────┘
     │ Tidak
     ▼
┌───────────────────────────┐
│          Selesai          │
└───────────────────────────┘


### 🔹 Latihan 2 – Bilangan Acak < 0.5
**Deskripsi:**
Menampilkan n bilangan acak yang lebih kecil dari 0.5
(dengan kombinasi perulangan while dan for).

**Kode Program:**
```python
import random
print("Menampilkan n bilangan acak yang lebih kecil dari 0.5")
n = int(input("Masukkan jumlah bilangan acak: "))
i = 0
while i < n:
    for j in range(1):
        bil = random.random()
        if bil < 0.5:
            print(bil)
    i += 1
```
Screenshoot
[Latihan 2 Perulangan](img/latihan2_perulangan)

**Flowchart**
M┌───────────────────────────┐
│          Mulai            │
└─────────────┬─────────────┘
              ↓
          Input n
              ↓
           i = 0
              ↓
     ┌──────────────────────┐
     │ Apakah i < n ?       │
     └───────┬──────────────┘
             │Ya
             ▼
           j = 1
             ↓
      bil = random.random()
             ↓
  ┌───────────────────────────┐
  │ Apakah bil < 0.5 ?        │
  └────────┬──────────────────┘
           │Ya
           ▼
        Cetak bil
           ↓
         i = i + 1
           ↑
           │
     ┌─────┘
     │ Tidak
     ▼
┌───────────────────────────┐
│          Selesai          │
└───────────────────────────┘

### 📘 Kesimpulan
Dari praktikum ini saya belajar bahwa:

-Struktur kondisi (if, elif, else) digunakan untuk mengambil keputusan berdasarkan logika tertentu.

-Struktur perulangan (for, while) digunakan untuk mengulang proses hingga kondisi tertentu terpenuhi.

-Kombinasi keduanya bisa digunakan untuk membuat program yang dinamis dan efisien.
