# напишите класс Employee, представляющий работника. 
# Метод __init__() должен получать имя, фамилию и ежегодный оклад; 
# все эти значения должны сохраняться в атрибутах. 
# Напишите метод give_raise(), который по умолчанию увеличивает ежегодный 
# оклад на $5000 — но при этом может получать другую величину прибавки.
# Напишите тестовый сценарий для Employee. 
# Напишите два тестовых метода, 
# test_give_default_raise() и test_give_custom_raise(). 
# Используйте метод setUp(), чтобы вам не приходилось заново создавать 
# экземпляр Employee в каждом тестовом метода. Запустите 
# свой тестовый сценарий и убедитесь в том, что оба теста прошли успешно.
import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.name = 'alexander'
        self.family = 'bogdanov'
        self.salary = 10000
        self.employee = Employee(self.name, self.family, self.salary)
    
    def test_give_default_raise(self):
        self.employee.give_raise()
        temp = (f'{self.name.strip().title()} '
             f'{self.family.strip().title()} '
             f'salary=${self.salary+5000}')
        self.assertEqual(temp, self.employee.get_full_info())
    
    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        temp = (f'{self.name.strip().title()} '
             f'{self.family.strip().title()} '
             f'salary=${self.salary+10000}')
        self.assertEqual(temp, self.employee.get_full_info())

if __name__ == '__main__':
    unittest.main()
