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
        pass

    def register_time(self, h):
        pass

    def pay_salary(self):
        pass

def test_0():
    e = Employee("Jan", "Kowalski", 100)
    e.register_time(5)
    assert e.pay_salary() == 500
    assert e.pay_salary() == 0
    e.register_time(5)
    e.register_time(5)
    assert e.pay_salary() == 1000
    e.register_time(10)
    assert e.pay_salary() == 1200
