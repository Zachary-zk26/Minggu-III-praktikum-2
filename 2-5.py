print("DATA NILAI MAHASISWA".center(80))
print("_"*80)
nama=input("\t\tNama\t: ")
tugas=int(input("\t\tTugas\t: "))
uts=int(input("\t\tUTS\t: "))
uas=int(input("\t\tUAS\t: "))
na=(25/100)*tugas+(35/100)*uts+(40/100)*uas
if na>=75:
    grade='A'
elif 75<na>=60:
    grade='B'
elif 60<na>=45:
    grade='C'
elif na<45:
    grade='D'
print("\n")
print("NILAI AKHIR DAN GRADE".center(80))
print("_"*80)
print(f"\t\tNama\t\t: {nama}")
print(f"\t\tNilai akhir\t: {na}")
print(f"\t\tGrade\t\t: {grade}")
