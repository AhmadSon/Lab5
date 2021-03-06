x = {}

while True:
    header="PROGRAM INPUT NILAI MAHASISWA"
    print(header.center(97,"="))
    print()
    print("[ (L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar")
    c = input("Masukkan Pilihan: ")

    if c == 'T' or c == 't':
        print("TAMBAH DATA")
        nim = int(input("Masukkan NIM\t\t: "))
        nama = input("Masukkan Nama\t\t: ")
        tugas = int(input("Masukkan Nilai Tugas\t: "))
        uts = int(input("Masukkan Nilai UTS\t: "))
        uas = int(input("Masukkan Nilai UAS\t: "))
        akhir = tugas*.3 + uts*.35 + uas*.35
        x[nama] = nim, uts, uas, tugas, akhir

    elif c == 'U' or c == 'u':
        print("UBAH DATA")
        print("Cari Data Mahasiswa Menggunakan Nama")
        nama = input("Masukkan Nama Mahasiswa: ")
        if nama in x.keys():
            nim = int(input("Masukkan NIM yang benar\t\t: "))
            tugas = int(input("Masukkan Nilai Tugas yang benar\t: "))
            uts = int(input("Masukkan Nilai UTS yang benar\t: "))
            uas = int(input("Masukkan Nilai UAS yang benar\t: "))
            akhir = tugas*.3 + uts*.35 + uas*.35
            x[nama] = nim, uts, uas, tugas, akhir
        else:
            print("Nama {0} tidak ditemukan".format(nama))

    elif c == 'h' or c == 'H':
        print("HAPUS DATA")
        nama = input("Masukkan Nama untuk menghapus: ")
        if nama in x.keys():
            del x[nama]
        else:
            print("Nama {0} Tidak Ditemukan".format(nama))

    elif c == 'C' or c == 'c':
        print("CARI DATA")
        nama = input("Masukkan Nama : ")
        if nama in x.keys():
            print("="*73)
            print("|                             Daftar Mahasiswa                          |")
            print("="*73)
            print("| Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*73)
            print("| {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                  .format(nama, nim, uts, uas, tugas, akhir))
            print("="*73)
        else:
            print("Nama {0} Tidak Ditemukan".format(nama))

    elif c == 'L' or c == 'l':
        if x.items():
            print("="*78)
            print("|                               Daftar Mahasiswa                             |")
            print("="*78)
            print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*78)
            i = 0
            for z in x.items():
                i += 1
                print("| {no:2d} | {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                      .format(z[0][:13], z[1][0], z[1][1], z[1][2], z[1][3], z[1][4], no=i))
            print("=" * 78)
        else:
            print("="*78)
            print("|                               Daftar Mahasiswa                             |")
            print("="*78)
            print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*78)
            print("|                                TIDAK ADA DATA                              |")
            print("="*78)

    elif c. lower() == 'k':
        break

    else:
        print("Pilih menu yang tersedia")
