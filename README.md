# Laporan Audit Kode - Program Konversi Suhu

## Pelanggaran Clean Code yang Ditemukan

### 1. **Penamaan Variabel yang Buruk (Poor Naming)**
**Lokasi:** Seluruh kode
**Deskripsi:** Menggunakan nama yang sangat singkat dan tidak deskriptif:

| Buruk | Seharusnya |
|-------|-----------|
| `c` (parameter) | `suhu_celsius` |
| `f` (parameter) | `suhu_fahrenheit` |
| `k` (parameter) | `suhu_kelvin` |
| `x` (input) | `suhu` |
| `c2f()` | `konversi_celsius_ke_fahrenheit()` |
| `f2c()` | `konversi_fahrenheit_ke_celsius()` |
| `c2k()` | `konversi_celsius_ke_kelvin()` |
| `k2c()` | `konversi_kelvin_ke_celsius()` |

**Dampak:** Kode tidak jelas, sulit dipahami oleh orang lain, maintenance lebih sulit

---

### 2. **Magic Numbers**
**Lokasi:** Line 6, 9, 12, 15
**Deskripsi:** Angka-angka ajaib tanpa nama yang jelas:

```python
def c2f(c):
    return (c * 9/5) + 32        # Apa arti 9/5 dan 32?

def c2k(c):
    return c + 273.15             # Apa arti 273.15?
```

Seharusnya menggunakan named constants:
```python
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
CELSIUS_TO_FAHRENHEIT_OFFSET = 32
KELVIN_OFFSET = 273.15
```

**Dampak:** Sulit diubah di masa depan, tidak jelas apa arti angka tersebut

---

### 3. **Tidak Ada Type Hints**
**Lokasi:** Semua fungsi
**Deskripsi:** Parameter dan return types tidak didefinisikan:

```python
def c2f(c):              # Tipe c? Return apa?
def f2c(f):              # Tipe f? Return apa?
```

Seharusnya:
```python
def konversi_celsius_ke_fahrenheit(suhu_celsius: float) -> float:
```

**Dampak:** IDE tidak bisa memberikan autocompletion dan type checking

---

### 4. **String Concatenation dengan `+`**
**Lokasi:** Line 35
**Deskripsi:** Menggunakan concatenation daripada f-string:

```python
print("Hasil: " + str(c2f(x)) + " F")
```

Seharusnya menggunakan f-string:
```python
print(f"Hasil: {suhu_celsius:.2f}°C = {hasil:.2f}°F")
```

**Dampak:** Kurang Pythonic, less readable, tidak professional

---

### 5. **Tidak Ada Docstrings**
**Lokasi:** Semua fungsi
**Deskripsi:** Tidak ada dokumentasi untuk fungsi:

```python
def c2f(c):
    return (c * 9/5) + 32
```

Tidak jelas apa yang fungsi ini lakukan tanpa membaca kode.

Seharusnya:
```python
def konversi_celsius_ke_fahrenheit(suhu_celsius: float) -> float:
    """
    Konversi suhu dari Celsius ke Fahrenheit
    
    Args:
        suhu_celsius: Suhu dalam derajat Celsius
        
    Returns:
        Suhu dalam derajat Fahrenheit
    """
```

**Dampak:** Dokumentasi tidak jelas, tidak professional

---

### 6. **Tidak Ada Input Validation**
**Lokasi:** Line 33-37
**Deskripsi:** Tidak ada error handling untuk input yang salah:

```python
x = float(input("Masukkan suhu: "))  # Akan crash jika input bukan angka!
```

Seharusnya:
```python
def dapatkan_input_suhu(prompt: str) -> float:
    while True:
        try:
            suhu = float(input(prompt))
            return suhu
        except ValueError:
            print("Masukkan angka yang valid!")
```

**Dampak:** Aplikasi bisa crash dengan input yang salah

---

### 7. **Code Duplication (DRY Violation)**
**Lokasi:** Line 33-48
**Deskripsi:** Pattern input dan output diulang multiple times:

```python
if pilihan == "1":
    x = float(input("Masukkan suhu: "))      # Diulang 4x
    print("Hasil: " + str(c2f(x)) + " F")
elif pilihan == "2":
    x = float(input("Masukkan suhu: "))      # Diulang lagi
    print("Hasil: " + str(f2c(x)) + " C")
```

Seharusnya dibuat helper function:
```python
def dapatkan_input_suhu(prompt: str) -> float:
    """Mendapatkan input suhu dengan validasi"""
    # ...

def tangani_pilihan(pilihan: str) -> bool:
    """Handle semua pilihan dengan logic yang terpusat"""
    # ...
```

**Dampak:** Maintenance lebih sulit, bug fix harus dilakukan multiple places

---

### 8. **Tidak Ada Separation of Concerns**
**Lokasi:** Line 28-48
**Deskripsi:** Main logic tercampur dengan business logic:

```python
# Main
print("=== KONVERSI SUHU ===")
pilihan = input("Pilih (1-4):\n...")

if pilihan == "1":
    # business logic tercampur disini
```

Seharusnya dipisah:
```python
def tampilkan_menu() -> None:
    """Display menu"""

def tangani_pilihan(pilihan: str) -> bool:
    """Handle logic"""

def jalankan_aplikasi() -> None:
    """Main loop"""
```

**Dampak:** Sulit di-test, complexity tinggi

---

### 9. **Tidak Ada Constants untuk Format String**
**Lokasi:** Line 31
**Deskripsi:** Menu display string terlalu panjang dan sulit untuk diubah:

```python
pilihan = input("Pilih (1-4):\n1. Celsius ke Fahrenheit\n2. Fahrenheit ke Celsius\n...")
```

Seharusnya:
```python
def tampilkan_menu() -> None:
    """Menampilkan menu"""
    print("=" * 40)
    print("    PROGRAM KONVERSI SUHU")
    print("=" * 40)
    # ... etc
```

**Dampak:** Sulit untuk maintenance dan redesign

---

### 10. **Error di Output**
**Lokasi:** Line 48
**Deskripsi:** Ada kesalahan logic di output:

```python
elif pilihan == "4":
    x = float(input("Masukkan suhu: "))
    print("Hasil: " + str(k2c(x)) + " K")  # Seharusnya "C" bukan "K"!
```

Ini bug! Output salah.

Seharusnya:
```python
print(f"Hasil: {k2c(x):.2f}°C")
```

**Dampak:** Output yang salah mengindikasikan developer tidak teliti

---

## Ringkasan Pelanggaran

| No | Pelanggaran | Severity | Kategori |
|----|-------------|----------|----------|
| 1 | Poor Naming | HIGH | Maintainability |
| 2 | Magic Numbers | MEDIUM | Readability |
| 3 | No Type Hints | MEDIUM | Type Safety |
| 4 | String Concatenation | LOW | Code Style |
| 5 | No Docstrings | LOW | Documentation |
| 6 | No Input Validation | HIGH | Robustness |
| 7 | DRY Violation | MEDIUM | Code Quality |
| 8 | No Separation | MEDIUM | Architecture |
| 9 | No Constants | LOW | Maintainability |
| 10 | Logic Error | HIGH | Correctness |

**Total: 10 pelanggaran Clean Code**

---

## Prinsip Clean Code yang Diterapkan

**Meaningful Names** - Nama variabel dan fungsi yang jelas dan deskriptif
**Named Constants** - Magic numbers diganti dengan `CELSIUS_TO_FAHRENHEIT_FACTOR`, `KELVIN_OFFSET`, dll
**Type Hints** - Semua parameter dan return types didefinisikan
**Docstrings** - Setiap fungsi punya dokumentasi lengkap
**Error Handling** - Input validation dengan try-except
**DRY Principle** - Helper function `dapatkan_input_suhu()` dan `tangani_pilihan()` untuk menghindari repetisi
**Separation of Concerns** - Menu, logic, dan main loop terpisah
**F-strings** - Modern string formatting
**Consistent Output** - Output format yang konsisten dengan emoji dan formatting yang baik
**Correctness** - Logic yang benar tanpa bug

---

## Kesimpulan

Versi improved menerapkan prinsip Clean Code yang menghasilkan:
- **Better Readability**: Kode lebih mudah dipahami
- **Maintainability**: Mudah untuk diubah dan di-extend
- **Robustness**: Error handling yang comprehensive
- **Professional Quality**: Dokumentasi lengkap dan type-safe
- **Correctness**: Bug sudah diperbaiki
