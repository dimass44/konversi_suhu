# Laporan Audit Kode - Konversi Suhu

## Link GitHub

https://github.com/username/konversi-suhu

## Deskripsi Aplikasi

Aplikasi Python sederhana untuk konversi suhu dari Celsius ke Fahrenheit dan Fahrenheit ke Celsius.

## Kode Asli

File `konversi_original.py` berisi versi awal aplikasi dengan beberapa pelanggaran Clean Code.

## Kode Perbaikan

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
