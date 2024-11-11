#Dictionary Data Pegawai
p1 = {"nama": "Budi", "jabatan": "Manager", "agama": "Islam", "status": "Menikah"}
p2 = {"nama": "Siti", "jabatan": "Asisten Manager", "agama": "Islam", "status": "Menikah"}
p3 = {"nama": "I Gede", "jabatan": "Supervisor", "agama": "Hindu", "status": "Menikah"}
p4 = {"nama": "Joko", "jabatan": "Staff", "agama": "Islam", "status": "Belum Menikah"}
p5 = {"nama": "Alex", "jabatan": "Staff", "agama": "Kristen Protestan", "status": "Belum Menikah"}

#List Dictionary Data Pegawai
ar_pegawai = [p1, p2, p3, p4, p5]

#Loop Data Pegawai
for pegawai in ar_pegawai:
    #IF Gaji Pokok
    if pegawai['jabatan'] == 'Manager': 
        gapok = 15000000
    elif pegawai['jabatan'] == 'Asisten Manager':
        gapok = 10000000
    elif pegawai['jabatan'] == 'Supervisor':
        gapok = 7000000
    elif pegawai['jabatan'] == 'Staff':
        gapok = 4000000
    #Cetak
    print('\n========Data Pegawai========\n',
          'Nama\t\t\t :', pegawai['nama'],'\n',
          'Jabatan\t\t :', pegawai['jabatan'],'\n',
          'Agama\t\t\t :', pegawai['agama'],'\n',
          'Status\t\t\t :', pegawai['status'],'\n',
          'Gaji Pokok\t\t :',gapok,)
        #Tunjangan Jabatan
    tunjab = 0.3 * gapok
    print(' Tunjangan Jabatan\t :', tunjab)
    #BPJS
    bpjs = 0.1 * gapok
    print(' BPJS\t\t\t :', bpjs)
    #Tunjangan Keluarga
    tunkel = (0, 0.1 * gapok)[pegawai['status'] == 'Menikah']
    print(' Tunjangan Keluarga\t :', tunkel)
    #Gaji Kotor
    gakot = gapok + tunjab + tunkel + bpjs
    print(' Gaji Kotor\t\t :', gakot)
    #Zakat Profesi
    zakat = (0, 0.025 * gakot)[pegawai['agama'] == 'Islam' and gakot >= 7000000]
    print(' Zakat Profesi\t\t :', zakat)
    #Gaji Bersih
    gaber = (gakot - zakat)
    print(' Gaji Bersih\t\t :', gaber)