import func as q

#tanggal = "YYYY-MM-DD"
tanggal = input("Input Tanggal: ")
hari = q.getWeekdayByDate(tanggal)

file_listjadwal = q.getListJadwal()

jadwal = []
for i in file_listjadwal:
    j = q.getJadwal(i)
    if (j.tanggal == tanggal or j.hari == hari):
        jadwal.append(j)
        
sorted_jadwal = q.sortJadwal(jadwal)                

print(f"\n== JADWAL {q.getStrDay(hari).upper()}, {tanggal} ==")
index = 0
for ij in sorted_jadwal:
    index += 1
    print(f"""
JADWAL {index}          
{ij.nama}
Jam {ij.jam}    Tanggal {ij.tanggal}
{ij.desc}
          """)
    
input()    
