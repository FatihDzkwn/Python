print("---- Data Karyawan ----")

#Data Pokok
nama = input("Nama karyawan\t: ")
divisi = input("Divisi\t\t: ")
agama = input("Agama\t\t: ")
jabatan = input("Jabatan\t\t: ")
#Print Data Pokok


#Gaji Pokok
if jabatan == "Staff" or jabatan == "staff":
  gaji_pokok = 4000000
elif jabatan == "Kabag" or jabatan == "kabag":
  gaji_pokok = 7000000
elif jabatan == "Manager" or jabatan == "manager":
  gaji_pokok = 10000000
else:
  gaji_pokok = 0
#Print Gaji Pokok
print("Gaji Pokok\t: %.2f" %(gaji_pokok))


#Tunjangan Jabatan
tunjangan_jabatan = gaji_pokok * 0.2
#Print Tunjangan Jabatan
print("Tunjangan Jabatan: %.2f" %(tunjangan_jabatan))


#Gaji Kotor
gaji_kotor = gaji_pokok + tunjangan_jabatan
#Print Gaji Kotor
print("Gaji Kotor\t: %.2f" %(gaji_kotor))


#Zakat
zakat = 0.025 * gaji_pokok if agama == "islam" or agama == "Islam" and jabatan != "staff" else 0
#Print Zakat
print("Zakat Profesi\t: %.2f" %(zakat))


#Gaji Bersih
gaji_bersih = gaji_kotor - zakat
#Print Gaji Bersih
print("Gaji Bersih\t: %.2f" %(gaji_bersih))