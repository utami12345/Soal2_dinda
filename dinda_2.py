def format_rupiah(angka):
    return "Rp {:,}".format(int(angka)).replace(",", ".")

total_penjualan = 0

while True:
    print("\n=== INPUT DATA BARANG ===")
    nama = input("Nama barang: ")
    jumlah = int(input("Jumlah: "))
    
    # Input harga bisa pakai titik
    harga_input = input("Harga per item: ")
    harga = int(harga_input.replace(".", ""))

    total = jumlah * harga
    print("Total harga", nama, "=", format_rupiah(total))

    total_penjualan += total

    lagi = input("Tambah barang lagi? (y/n): ")
    if lagi.lower() != 'y':
        break

print("\n=== RINCIAN PEMBAYARAN ===")
print("Total penjualan:", format_rupiah(total_penjualan))

# Diskon bertingkat
if total_penjualan >= 500000:
    diskon = 0.25 * total_penjualan
elif total_penjualan >= 250000:
    diskon = 0.15 * total_penjualan
elif total_penjualan >= 100000:
    diskon = 0.10 * total_penjualan
else:
    diskon = 0

print("Diskon:", format_rupiah(diskon))

# Setelah diskon
setelah_diskon = total_penjualan - diskon
print("Total setelah diskon:", format_rupiah(setelah_diskon))

# Pajak 11%
pajak = 0.11 * setelah_diskon
print("Pajak (11%):", format_rupiah(pajak))

# Total akhir
total_bayar = setelah_diskon + pajak
print("Total yang harus dibayar:", format_rupiah(total_bayar))

print("\n=== TERIMA KASIH ===")

#promp Ai
# BUATLAH PROGRAM KASIR BERUPA INPUT DATA BARANG (NAMA, JUMLah, dan harga) kemudian hitung total penjualan. ketentuan dalam perhitungan transakasi ada diskon berupa :
# 1. jika pembelian barang bernilai RP 100.000 maka diskonnya 10%
# 2. jika pembelian barang bernilai RP 250.000 maka diskonnya 15%
# 3. jika pembelian barang bernilai >= RP 500.000 maka diskonnya 25%
# Selanjutnya seluruh pembelian barang dikenakan pajak senilai 11%
# tolong kerjakan tugas tersebut dalam bahasa python