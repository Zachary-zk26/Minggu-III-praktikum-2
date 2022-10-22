from ast import Break


bil=[]
for i in range(1,4):
        bil.append(input(f"Masukkan bilangan ke-{i}\t: "))
bil1=bil.pop(0)
bil2=bil.pop(0)
bil3=bil.pop(0)

if bil1==bil2==bil3:
    print("Semua bilangan sama")
    Break
elif bil1==bil2:
    print("Bilangan ke-1 dan ke-2 sama")
elif bil1==bil3:
    print("Bilangan ke-1 dan ke-3 sama")
elif bil2==bil3:
    print("Bilangan ke-2 dan ke-3 sama")
else:
    print("Tidak ada bilangan yang sama")