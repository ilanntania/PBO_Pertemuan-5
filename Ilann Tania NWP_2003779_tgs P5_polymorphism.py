class Person:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def printDetails(self):
        print("Saat ini saya sedang kuliah di UPI kampus Daerah Serang")  

person = Person ("Ilann Tania Nur Widona Putri", 2003779, "Sistem Informasi Kelautan")
print(person.nama)
print(person.nim)
print(person.jurusan)
person.printDetails()