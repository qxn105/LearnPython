# напишите класс Employee, представляющий работника. 
# Метод __init__() должен получать имя, фамилию и ежегодный оклад; 
# все эти значения должны сохраняться в атрибутах. 
# Напишите метод give_raise(), который по умолчанию увеличивает ежегодный 
# оклад на $5000 — но при этом может получать другую величину прибавки.

from symtable import SymbolTableFactory


class Employee():
    def __init__(self, name, family, salary):
        self.name = name.strip().title()
        self.family = family.strip().title()
        try:
            self.salary = int(salary)
        except ValueError:
            self.salary = 5000
    
    def give_raise(self, increase = 5000):
        self.salary += increase
    
    def get_full_info(self):
        return f'{self.name} {self.family} salary=${self.salary}'