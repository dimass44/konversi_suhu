"""Aplikasi konversi suhu sederhana."""

FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_OFFSET = 32


def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - FAHRENHEIT_OFFSET) / FAHRENHEIT_FACTOR


def get_temperature(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Masukkan angka yang valid")


def main() -> None:
    print("KONVERSI SUHU")
    choice = input("1 C ke F, 2 F ke C: ").strip()

    if choice == "1":
        temperature = get_temperature("Masukkan suhu Celsius: ")
        result = celsius_to_fahrenheit(temperature)
        print(f"Hasil: {result:.2f} F")
    elif choice == "2":
        temperature = get_temperature("Masukkan suhu Fahrenheit: ")
        result = fahrenheit_to_celsius(temperature)
        print(f"Hasil: {result:.2f} C")
    else:
        print("Pilihan salah")


if __name__ == "__main__":
    main()