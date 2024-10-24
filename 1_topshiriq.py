class Talaba:
    def __init__(self):
        self.fanlar = []

    def fanga_yozil(self, fan):
        self.fanlar.append(fan)

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
            print(f"{fan} fani o'chirildi.")
        else:
            print("Siz bu fanga yozilmagansiz.")

class Fan:
    def __init__(self):
        self.fan1 = "Matematika"
        self.fan2 = "Fizika"
        self.fan3 = "Kimyo"
        self.fan4 = "Biologiya"

fan = Fan()

talaba1 = Talaba()
talaba1.fanga_yozil(fan.fan1)
talaba1.fanga_yozil(fan.fan2)
talaba1.fanga_yozil(fan.fan3)
talaba1.fanga_yozil(fan.fan4)

print("Talabaning fanlari:")
for i in talaba1.fanlar:
    print(i)

remove_fan = input("O'chirmoqchi bo'lgan faningiz nomini kiriting: ")
talaba1.remove_fan(remove_fan)

print("Yangilangan fanlar ro'yxati:")
for i in talaba1.fanlar:
    print(i)
