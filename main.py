import pandas as pd
import matplotlib.pyplot as plt

# Membaca data keuangan dari file CSV
df = pd.read_csv('data_keuangan.csv')

# Menampilkan ringkasan data
print("Ringkasan Data Keuangan:")
print(df.head())

# Menghitung Total Pendapatan dan Total Pengeluaran per Bulan
df['Total Pendapatan'] = df['Pendapatan 1'] + df['Pendapatan 2']
df['Total Pengeluaran'] = df['Pengeluaran 1'] + df['Pengeluaran 2']

# Menampilkan rata-rata Total Pendapatan dan Total Pengeluaran
rata_rata_pendapatan = df['Total Pendapatan'].mean()
rata_rata_pengeluaran = df['Total Pengeluaran'].mean()
print("\nRata-rata Total Pendapatan: ", rata_rata_pendapatan)
print("Rata-rata Total Pengeluaran: ", rata_rata_pengeluaran)

# Visualisasi data
bulan = df['Bulan']
plt.figure(figsize=(10, 6))
plt.plot(bulan, df['Total Pendapatan'], marker='o', label='Total Pendapatan')
plt.plot(bulan, df['Total Pengeluaran'], marker='o', label='Total Pengeluaran')
plt.xlabel('Bulan')
plt.ylabel('Jumlah')
plt.title('Total Pendapatan dan Total Pengeluaran per Bulan')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Menyimpan gambar grafik ke file
plt.savefig('analisis_keuangan.png')

# Menampilkan grafik
plt.show()
