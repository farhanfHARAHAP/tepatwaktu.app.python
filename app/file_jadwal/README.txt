# Tutorial #

@ Cara menambah jadwal:
1. Copy jadwal_prototype.json, paste dan ubah namanya bebas tanpa spasi!
2. Ubah nilai variabel dalam file sesuai kebutuhan!
3. Save file
4. Tambahkan nama file jadwal baru ke listjadwal.txt!

@ Format file .json jadwal:
"jadwalNama": "",		// Isi dengan Nama
"jadwalDesc": "",		// Isi dengan Deskripsi
"jadwalJam": 0,			// Isi dengan angka bulat jam berapa jadwal, format 0 - 23
"jadwalHari": 0,		// Isi 0 jika jadwal non-pengulangan, isi dengan angka bulat 0 (minggu) - 6 (sabtu)
"jadwalTanggal": "YYYY-MM-DD"   // Ubah jika jadwal non repetitif, sesuai format

@ Cara menghapus jadwal:
1. Cari nama file jadwal yang ingin dihapus.
2. Hapus file.
3. Hapus juga nama file jadwal terhapus di listjadwal.txt!

@ Cara mengedit jadwal:
1. Cari nama file jadwal yang ingin diedit.
2. Edit sesuai kebutuhan.
3. Save.
