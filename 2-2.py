bil=[]
for i in range(1,4):
    bil.append(input(f"Masukkan bilangan ke-{i} : "))
    i+=1
print(f"Bilangan terbesar adalah {max(bil)}")