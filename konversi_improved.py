"""
Program Konversi Suhu - Versi Clean Code
Aplikasi sederhana untuk konversi satuan suhu dengan prinsip Clean Code
"""

# Konstanta
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
CELSIUS_TO_FAHRENHEIT_OFFSET = 32
KELVIN_OFFSET = 273.15


def konversi_celsius_ke_fahrenheit(suhu_celsius: float) -> float:
    """
    Konversi suhu dari Celsius ke Fahrenheit
    
    Args:
        suhu_celsius: Suhu dalam derajat Celsius
        
    Returns:
        Suhu dalam derajat Fahrenheit
    """
    return (suhu_celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + CELSIUS_TO_FAHRENHEIT_OFFSET


def konversi_fahrenheit_ke_celsius(suhu_fahrenheit: float) -> float:
    """
    Konversi suhu dari Fahrenheit ke Celsius
    
    Args:
        suhu_fahrenheit: Suhu dalam derajat Fahrenheit
        
    Returns:
        Suhu dalam derajat Celsius
    """
    return (suhu_fahrenheit - CELSIUS_TO_FAHRENHEIT_OFFSET) / CELSIUS_TO_FAHRENHEIT_FACTOR


def konversi_celsius_ke_kelvin(suhu_celsius: float) -> float:
    """
    Konversi suhu dari Celsius ke Kelvin
    
    Args:
        suhu_celsius: Suhu dalam derajat Celsius
        
    Returns:
        Suhu dalam Kelvin
    """
    return suhu_celsius + KELVIN_OFFSET


def konversi_kelvin_ke_celsius(suhu_kelvin: float) -> float:
    """
    Konversi suhu dari Kelvin ke Celsius
    
    Args:
        suhu_kelvin: Suhu dalam Kelvin
        
    Returns:
        Suhu dalam derajat Celsius
    """
    return suhu_kelvin - KELVIN_OFFSET


def dapatkan_input_suhu(prompt: str) -> float:
    """
    Mendapatkan input suhu dari pengguna dengan validasi
    
    Args:
        prompt: Pesan untuk ditampilkan kepada pengguna
        
    Returns:
        Nilai suhu yang valid sebagai float
    """
    while True:
        try:
            suhu = float(input(prompt))
            return suhu
        except ValueError:
            print("Masukkan angka yang valid!")


def tampilkan_menu() -> None:
    """Menampilkan menu konversi suhu"""
    print("\n" + "=" * 40)
    print("    PROGRAM KONVERSI SUHU")
    print("=" * 40)
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")
    print("5. Keluar")
    print("=" * 40)


def tangani_pilihan(pilihan: str) -> bool:
    """
    Menangani pilihan menu pengguna
    
    Args:
        pilihan: Pilihan menu yang dipilih pengguna
        
    Returns:
        False jika pengguna memilih keluar, True sebaliknya
    """
    if pilihan == "1":
        suhu_celsius = dapatkan_input_suhu("Masukkan suhu (Celsius): ")
        hasil = konversi_celsius_ke_fahrenheit(suhu_celsius)
        print(f"Hasil: {suhu_celsius}°C = {hasil:.2f}°F\n")
    
    elif pilihan == "2":
        suhu_fahrenheit = dapatkan_input_suhu("Masukkan suhu (Fahrenheit): ")
        hasil = konversi_fahrenheit_ke_celsius(suhu_fahrenheit)
        print(f"Hasil: {suhu_fahrenheit}°F = {hasil:.2f}°C\n")
    
    elif pilihan == "3":
        suhu_celsius = dapatkan_input_suhu("Masukkan suhu (Celsius): ")
        hasil = konversi_celsius_ke_kelvin(suhu_celsius)
        print(f"Hasil: {suhu_celsius}°C = {hasil:.2f}K\n")
    
    elif pilihan == "4":
        suhu_kelvin = dapatkan_input_suhu("Masukkan suhu (Kelvin): ")
        hasil = konversi_kelvin_ke_celsius(suhu_kelvin)
        print(f"Hasil: {suhu_kelvin}K = {hasil:.2f}°C\n")
    
    elif pilihan == "5":
        print("Terima kasih telah menggunakan program konversi suhu!\n")
        return False
    
    else:
        print("Pilihan tidak valid (1-5)\n")
    
    return True


def jalankan_aplikasi() -> None:
    """Menjalankan aplikasi konversi suhu"""
    print("Selamat datang di Program Konversi Suhu!")
    
    while True:
        tampilkan_menu()
        pilihan_pengguna = input("Pilih menu (1-5): ").strip()
        
        try:
            if not tangani_pilihan(pilihan_pengguna):
                break
        except Exception as kesalahan:
            print(f"Error: {kesalahan}\n")


if __name__ == "__main__":
    jalankan_aplikasi()
