# Perbandingan Kode: Sebelum & Sesudah Perbaikan

## Deskripsi Aplikasi

Aplikasi Python sederhana untuk konversi suhu dari Celsius ke Fahrenheit dan Fahrenheit ke Celsius. Proyek ini menunjukkan peningkatan kualitas kode dengan menerapkan prinsip-prinsip Software Engineering yang baik.

---

## Perbandingan Detail Sebelum & Sesudah

### 1. **Meaningful Naming** (Penamaan yang Bermakna)

| Aspek | Sebelum (Kode Asli) | Sesudah (Perbaikan) |
|-------|-------------------|-------------------|
| **Nama Fungsi** | `c2f()`, `f2c()` | `celsius_to_fahrenheit()`, `fahrenheit_to_celsius()` |
| **Nama Variabel** | `p`, `x`, `c`, `f` | `choice`, `temperature`, `celsius`, `fahrenheit` |
| **Keuntungan** | Singkat tapi tidak jelas | Deskriptif dan mudah dipahami |

**Penjelasan:**
- Variabel single-letter seperti `p` dan `x` membingungkan pembaca tentang tujuannya
- Nama yang jelas (`choice`, `temperature`) membuat kode self-documenting dan mengurangi kebutuhan akan komentar

```python
# SEBELUM: Tidak jelas apa yang dilakukan
p = input("1 C ke F, 2 F ke C: ")
x = float(input("Masukkan suhu: "))

# SESUDAH: Jelas dan deskriptif
choice = input("1 C ke F, 2 F ke C: ").strip()
temperature = get_temperature("Masukkan suhu Celsius: ")
```

---

### 2. **Single Responsibility Principle (SRP)** (Satu Fungsi, Satu Tanggung Jawab)

| Aspek | Sebelum (Kode Asli) | Sesudah (Perbaikan) |
|-------|-------------------|-------------------|
| **Input Handling** | Ditangani langsung di `main()` | Dipisah ke fungsi `get_temperature()` |
| **Validasi Input** | Tidak ada validasi | Ada try-except untuk menangani error |
| **Responsibilities** | `main()` melakukan terlalu banyak | Setiap fungsi punya satu tanggung jawab spesifik |

**Penjelasan:**
- Kode asli: `main()` bertanggung jawab untuk input, konversi, dan output (terlalu banyak)
- Kode diperbaiki: Setiap fungsi punya satu tanggung jawab (Separation of Concerns)

```python
# SEBELUM: main() melakukan terlalu banyak
def main():
    p = input("1 C ke F, 2 F ke C: ")         # Input
    x = float(input("Masukkan suhu: "))       # Input handling
    if p == "1":                               # Logika
        print("Hasil: " + str(c2f(x)) + " F") # Output

# SESUDAH: Tanggung jawab dipisah
def get_temperature(prompt: str) -> float:
    """Bertanggung jawab hanya untuk mengambil dan validasi input angka"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Masukkan angka yang valid")

def main() -> None:
    """Bertanggung jawab hanya untuk orchestration"""
    choice = input("1 C ke F, 2 F ke C: ").strip()
    if choice == "1":
        temperature = get_temperature("Masukkan suhu Celsius: ")
        result = celsius_to_fahrenheit(temperature)
        print(f"Hasil: {result:.2f} F")
```

---

### 3. **Don't Repeat Yourself (DRY)** (Jangan Ulangi Kode)

| Aspek | Sebelum (Kode Asli) | Sesudah (Perbaikan) |
|-------|-------------------|-------------------|
| **Magic Numbers** | `9`, `5`, `32` hardcoded di setiap fungsi | Konstanta `FAHRENHEIT_FACTOR` dan `FAHRENHEIT_OFFSET` |
| **Maintenance** | Jika rumus berubah, harus edit banyak tempat | Edit di satu tempat saja |
| **Kejelasan** | Tidak jelas kenapa angka tersebut digunakan | Konstanta bernama jelas menunjukkan maksudnya |

**Penjelasan:**
- Magic numbers (angka tanpa konteks) membuat kode sulit dipahami dan sulit di-maintain
- Konstanta terpusat memudahkan perubahan dan meningkatkan clarity

```python
# SEBELUM: Magic numbers tersebar dan berulang
def c2f(c):
    return (c * 9 / 5) + 32  # Magic numbers

def f2c(f):
    return (f - 32) * 5 / 9  # Magic numbers berulang (DRY violation)

# SESUDAH: Konstanta terpusat dengan nama yang jelas
FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_OFFSET = 32

def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - FAHRENHEIT_OFFSET) / FAHRENHEIT_FACTOR
```

**Keuntungan:**
- Jika rumus konversi berubah, hanya perlu ubah konstanta di atas
- Kode lebih readable dan self-documenting

---

### 4. **Type Hints & Dokumentasi** (Tipe Data & Dokumentasi)

| Aspek | Sebelum (Kode Asli) | Sesudah (Perbaikan) |
|-------|-------------------|-------------------|
| **Type Hints** | Tidak ada, tipe harus ditebak | `celsius: float`, `-> float`, `-> None` |
| **Docstring** | Tidak ada | `"""Aplikasi konversi suhu sederhana."""` |
| **IDE Support** | Tidak ada auto-complete & type checking | IDE memberikan auto-complete & error detection |
| **Clarity** | Harus membaca implementasi untuk tahu tipe | Tipe sudah jelas di fungsi signature |

**Penjelasan:**
- Type hints membantu IDE memberikan suggestion yang lebih akurat
- Type hints berfungsi sebagai dokumentasi bawaan
- Memudahkan debugging dengan early error detection

```python
# SEBELUM: Tipe tidak jelas
def c2f(c):
    return (c * 9 / 5) + 32  # Apa tipe c? int atau float?

def f2c(f):
    return (f - 32) * 5 / 9  # Return type apa?

# SESUDAH: Tipe sudah jelas
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert temperature from Fahrenheit to Celsius."""
    return (fahrenheit - FAHRENHEIT_OFFSET) / FAHRENHEIT_FACTOR
```

---

### 5. **Error Handling & Input Validation** (Penanganan Error & Validasi)

| Aspek | Sebelum (Kode Asli) | Sesudah (Perbaikan) |
|-------|-------------------|-------------------|
| **Validasi Input** | Tidak ada | Ada try-except dengan loop retry |
| **Error Recovery** | Program crash jika input salah | Loop menanyakan ulang sampai input valid |
| **User Experience** | Buruk (program crash) | Baik (user diminta input ulang dengan pesan jelas) |

**Penjelasan:**
- Kode asli akan crash jika user memasukkan input non-numeric
- Kode diperbaiki handling error secara graceful dan meminta user input ulang

```python
# SEBELUM: Akan crash jika input bukan angka
x = float(input("Masukkan suhu: "))  # ValueError jika input "abc" → program crash!

# SESUDAH: Error handling dengan user-friendly message
def get_temperature(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Masukkan angka yang valid")  # Pesan jelas, user diminta input ulang
```

**Contoh interaksi:**
```
# Kode diperbaiki:
Masukkan suhu Celsius: abc
Masukkan angka yang valid
Masukkan suhu Celsius: 25
Hasil: 77.00 F

# Kode asli:
Masukkan suhu: abc
ValueError: could not convert string to float: 'abc'
Program crash!
```

---

### 6. **String Formatting & Code Style** (Format String & Style Kode)

| Aspek | Sebelum (Kode Asli) | Sesudah (Perbaikan) |
|-------|-------------------|-------------------|
| **String Concatenation** | `"Hasil: " + str(c2f(x)) + " F"` | `f"Hasil: {result:.2f} F"` |
| **Output Formatting** | Tidak konsisten, banyak desimal | Konsisten 2 desimal |
| **Input Cleanup** | Tidak ada `.strip()` | Ada `.strip()` untuk menghilangkan whitespace |
| **Readability** | Agak verbose dan sulit dibaca | Clean dan mudah dipahami |

**Penjelasan:**
- String concatenation dengan `+` verbose dan error-prone
- F-string modern, clean, dan lebih readable
- Format specifier `.2f` memastikan output konsisten

```python
# SEBELUM: String concatenation verbose
result = c2f(25)
print("Hasil: " + str(result) + " F")  
# Output: Hasil: 77.0 F (tidak konsisten, bisa 77.0 atau 77.00)

# SESUDAH: F-string dengan formatting
result = celsius_to_fahrenheit(25)
print(f"Hasil: {result:.2f} F")  
# Output: Hasil: 77.00 F (konsisten 2 desimal)
```

**Keuntungan F-string:**
- Lebih mudah dibaca dan dipahami
- Performa lebih baik dari string concatenation
- Lebih mudah untuk men-debug jika ada error

---

### 7. **Main Guard & Reusability** (Guard Clause & Reusability)

| Aspek | Sebelum (Kode Asli) | Sesudah (Perbaikan) |
|-------|-------------------|-------------------|
| **Main Guard** | `main()` dipanggil langsung | `if __name__ == "__main__": main()` |
| **Reusability** | Tidak bisa di-import tanpa execute | Bisa di-import sebagai module |
| **Structure** | Linear, semua di top-level | Terstruktur dengan main guard |

**Penjelasan:**
- Kode asli memanggil `main()` langsung → tidak bisa di-import tanpa execution
- Kode diperbaiki menggunakan main guard → bisa di-import untuk digunakan di project lain

```python
# SEBELUM: main() dijalankan langsung
def c2f(c):
    return (c * 9 / 5) + 32

def f2c(f):
    return (f - 32) * 5 / 9

def main():
    # ... kode main ...

main()  # ← Dijalankan langsung!

# Jika di-import: from konversi_original import c2f
# → main() akan tetap dijalankan (tidak diinginkan!)

# SESUDAH: Main guard memungkinkan reusability
FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_OFFSET = 32

def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

def main() -> None:
    # ... kode main ...

if __name__ == "__main__":
    main()  # ← Hanya dijalankan jika ini script utama

# Jika di-import: from konversi_improved import celsius_to_fahrenheit
# → main() tidak akan dijalankan (yang diinginkan!)
```

---

## Ringkasan Manfaat Perbaikan

| Metrik | Sebelum | Sesudah | Dampak |
|--------|--------|--------|--------|
| **Maintainability** | Sulit | Mudah | Kode lebih mudah diubah di masa depan |
| **Readability** | Rendah | Tinggi | Developer baru cepat memahami kode |
| **Reusability** | Tidak bisa di-import | Bisa di-import | Fungsi bisa digunakan di project lain |
| **Error Handling** | Tidak ada | Comprehensive | Program tidak crash, UX lebih baik |
| **Type Safety** | Tidak ada | Ada | IDE dapat membantu deteksi error |
| **Documentation** | Tidak ada | Self-documenting | Kode sudah jelas tanpa doc terpisah |
| **Code Style** | Inconsistent | PEP 8 compliant | Konsisten dengan Python best practices |

---

## Prinsip-Prinsip Software Engineering yang Diterapkan

✅ **Meaningful Naming** - Nama yang jelas dan deskriptif
✅ **Single Responsibility Principle (SRP)** - Setiap fungsi punya satu tanggung jawab
✅ **Don't Repeat Yourself (DRY)** - Tidak ada pengulangan, konstanta terpusat
✅ **Error Handling** - Input validation dan exception handling yang proper
✅ **Type Hints** - Dokumentasi tipe untuk clarity dan IDE support
✅ **Modern Python Style** - F-string, main guard, code formatting sesuai PEP 8
✅ **Defensive Programming** - Validasi input dan error recovery yang baik

---

## File dalam Proyek

| File | Deskripsi |
|------|-----------|
| `konversi_original.py` | Versi awal dengan beberapa clean code violations |
| `konversi_improved.py` | Versi perbaikan dengan best practices |
| `README.md` | Dokumentasi lengkap perbandingan |

File `konversi_improved.py` berisi versi yang sudah diperbaiki dengan prinsip Clean Code.

## Hasil Code Audit

Pelanggaran yang ditemukan pada versi awal:

1. Penamaan fungsi dan variabel tidak jelas.
2. Ada magic numbers seperti `9`, `5`, dan `32`.
3. Tidak ada type hints.
4. Input tidak divalidasi.
5. Output memakai string concatenation.

## Prinsip yang Diterapkan

- Meaningful names
- Constants untuk nilai tetap
- Type hints
- Input validation
- F-string untuk output

## Perbandingan Sebelum dan Sesudah

Versi awal lebih singkat, tetapi sulit dibaca dan rawan error. Versi perbaikan lebih rapi, lebih mudah dipahami, dan lebih aman digunakan.

## Cara Menjalankan

```powershell
python konversi_improved.py
```
