# Program Konversi Suhu

def c2f(c):
    return (c * 9/5) + 32

def f2c(f):
    return (f - 32) * 5/9

def c2k(c):
    return c + 273.15

def k2c(k):
    return k - 273.15

# Main
print("=== KONVERSI SUHU ===")
pilihan = input("Pilih (1-4):\n1. Celsius ke Fahrenheit\n2. Fahrenheit ke Celsius\n3. Celsius ke Kelvin\n4. Kelvin ke Celsius\n")

if pilihan == "1":
    x = float(input("Masukkan suhu: "))
    print("Hasil: " + str(c2f(x)) + " F")
elif pilihan == "2":
    x = float(input("Masukkan suhu: "))
    print("Hasil: " + str(f2c(x)) + " C")
elif pilihan == "3":
    x = float(input("Masukkan suhu: "))
    print("Hasil: " + str(c2k(x)) + " K")
elif pilihan == "4":
    x = float(input("Masukkan suhu: "))
    print("Hasil: " + str(k2c(x)) + " K")
else:
    print("Pilihan salah")
