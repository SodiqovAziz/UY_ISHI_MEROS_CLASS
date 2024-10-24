class Shaxs:
    def __init__(self, ism, yosh, jins):
        self.ism = ism
        self.yosh = yosh
        self.jins = jins

    def get_info(self):
        return f"Ismi: {self.ism}, Yoshi: {self.yosh}, Jinsi: {self.jins}"

class Professor(Shaxs):
    def __init__(self, ism, yosh, jins, fan, daraja):
        super().__init__(ism, yosh, jins)
        self.fan = fan
        self.daraja = daraja

    def get_info(self):
        return f"Ismi: {self.ism}, Yoshi: {self.yosh}, Jinsi: {self.jins}, Fan: {self.fan}, Ilmiy daraja: {self.daraja}"

    def dars_berish(self):
        return f"{self.ism} {self.fan} fanidan dars beradi."


class Foydalanuvchi(Shaxs):
    def __init__(self, ism, yosh, jins, login, parol):
        super().__init__(ism, yosh, jins)
        self.login = login
        self.parol = parol

    def get_info(self):
        return f"Ismi: {self.ism}, Yoshi: {self.yosh}, Login: {self.login}"

    def tizimga_kirish(self):
        return f"{self.ism} tizimga kirishdi."


class Sotuvchi(Shaxs):
    def __init__(self, ism, yosh, jins, dokon, maosh):
        super().__init__(ism, yosh, jins)
        self.dokon = dokon
        self.maosh = maosh

    def get_info(self):
        return f"Ismi: {self.ism}, Yoshi: {self.yosh}, Do'koni: {self.dokon}, Maoshi: {self.maosh} so'm"

    def savdo_qilish(self):
        return f"{self.ism} {self.dokon} do'konida savdo qiladi."


class Mijoz(Shaxs):
    def __init__(self, ism, yosh, jins, mijoz_id, telefon):
        super().__init__(ism, yosh, jins)
        self.mijoz_id = mijoz_id
        self.telefon = telefon

    def get_info(self):
        return f"Ismi: {self.ism}, Yoshi: {self.yosh}, Mijoz ID: {self.mijoz_id}, Telefon: {self.telefon}"

    def buyurtma_berish(self):
        return f"{self.ism} buyurtma berdi."


class Admin(Foydalanuvchi):
    def __init__(self, ism, yosh, jins, login, parol, huquq):
        super().__init__(ism, yosh, jins, login, parol)
        self.huquq = huquq

    def get_info(self):
        return f"Ismi: {self.ism}, Yoshi: {self.yosh}, Login: {self.login}, Huquq: {self.huquq}"

    def ban_user(self, foydalanuvchi):
        print(f"Foydalanuvchi {foydalanuvchi.ism} bloklandi.")


prof = Professor("Anvar", 45, "Erkak", "Matematika", "PhD")
print(prof.get_info())
print(prof.dars_berish())

foydalanuvchi = Foydalanuvchi("Ali", 30, "Erkak", "ali30", "parol123")
print(foydalanuvchi.get_info())
print(foydalanuvchi.tizimga_kirish())

sotuvchi = Sotuvchi("Dilshod", 40, "Erkak", "Oltin Markaz", 3000000)
print(sotuvchi.get_info())
print(sotuvchi.savdo_qilish())

mijoz = Mijoz("Madina", 25, "Ayol", 12345, "998901234567")
print(mijoz.get_info())
print(mijoz.buyurtma_berish())

admin = Admin("Nodir", 35, "Erkak", "nodir_admin", "admin123", "SuperAdmin")
print(admin.get_info())
admin.ban_user(foydalanuvchi)