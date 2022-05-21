from zad_2 import Employee

# Zaimplementuj klasę PremiumEmployee, która będzie klasą
# pochodną Employee. Klasa ta powinna umożliwiać dodatkowo
# przyznawanie bonusów pracownikowi.
# >>> employee = PremiumEmployee('Jan', 'Nowak', 100.0)
# >>> employee.register_time(5)
# >>> employee.give_bonus(1000.0)
# >>> employee.pay_salary()
# 1500.0

class PremiumEmployee(Employee):
    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka)
        self.bonus = 0

    def give_bonus(self, b):
        self.bonus += b

    def pay_salary(self):
        wyplata = super().pay_salary() + self.bonus
        self.bonus = 0
        return wyplata

p = PremiumEmployee("Jan", "Nowak", 100)
print(p.pay_salary())

p.register_time(5)
p.give_bonus(1000)
print(p.pay_salary())
print(p.pay_salary())
p.give_bonus(10)
p.give_bonus(20)
print(p.pay_salary())

