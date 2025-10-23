print("Pola segitiga bintang")
n = int(input("Masukkan tinggi segitiga: "))

for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()
