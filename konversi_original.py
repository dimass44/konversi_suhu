# Aplikasi konversi suhu

def c2f(c):
    return (c * 9 / 5) + 32

def f2c(f):
    return (f - 32) * 5 / 9

def main():
    print("KONVERSI SUHU")
    p = input("1 C ke F, 2 F ke C: ")
    x = float(input("Masukkan suhu: "))
    if p == "1":
        print("Hasil: " + str(c2f(x)) + " F")
    elif p == "2":
        print("Hasil: " + str(f2c(x)) + " C")
    else:
        print("Salah")


main()