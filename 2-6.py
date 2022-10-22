from ctypes.wintypes import CHAR


print("DATA PEGAWAI".center(80))
print("_"*80)
nama=input("\t\tNama\t\t: ")
gol=(input("\t\tGolongan\t: "))
jam_kerja=int(input("\t\tTotal jam kerja\t: "))
new_jam_kerja=jam_kerja-200
if gol=='A':
    gaji=500000
    tjg=gaji*(10/100)
    lembur=500*new_jam_kerja
elif gol=='B':
    gaji=700000
    tjg=gaji*(15/100)
    lembur=7500*new_jam_kerja
elif gol=='C':
    gaji=900000
    tjg=gaji*(20/100)
    lembur=10000*new_jam_kerja
total=gaji+tjg+lembur
print("_"*80)
print("\n")
print("PERHITUNGAN GAJI".center(80))
print("_"*80)
print(f"\t\tGaji pokok\t: {gaji}")
print(f"\t\tTunjangan\t: {tjg}")
print(f"\t\tLembur\t\t: {lembur}")
print("_"*80)
print(f"\t\tTotal\t\t: {total}")
