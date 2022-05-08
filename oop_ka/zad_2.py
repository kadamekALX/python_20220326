# Zaimplementuj klasę Employee umożliwiającą rejestrowanie czasu
# pracy oraz wypłacanie pensji na podstawie zadanej stawki
# godzinowej. Jeżeli pracownik będzie pracował więcej niż 8 godzin
# (podczas pojedynczej rejestracji czasu) to kolejne godziny policz
# jako nadgodziny (z podwójną stawką godzinową).
# Przykład użycia:
# >>> employee = Employee('Jan', 'Nowak', 100.0)
# >>> employee.register_time(5)
# >>> employee.pay_salary()
# 500.0
# >>> employee.pay_salary()
# 0.0
# >>> employee.register_time(10)
# >>> employee.pay_salary()

class Employee:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja
        self.przepracowane_godziny = 0

    def register_time(self, h):
        if h <= 8:
            self.przepracowane_godziny += h
        else:
            self.przepracowane_godziny += 8 + (h - 8) * 2

    def pay_salary(self):
        wynagrodzenie = self.przepracowane_godziny * self.pensja
        self.przepracowane_godziny = 0
        return wynagrodzenie


def test_0():
    e = Employee("Jan", "Kowalski", 100)
    assert e.pay_salary() == 0
    e.register_time(5)
    assert e.pay_salary() == 500
    assert e.pay_salary() == 0
    e.register_time(5)
    e.register_time(5)
    assert e.pay_salary() == 1000
    e.register_time(5) # 0 nadgodzin
    e.register_time(9) # 1 nadgodzina
    assert e.pay_salary() == 1500
    e.register_time(10)
    assert e.pay_salary() == 1200
