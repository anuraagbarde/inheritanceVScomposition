from abc import ABC, abstractmethod

class Animal(ABC):
    __step_counter: int
    
    def __init__(self) -> None:
        self.__step_counter = 0
    
    def step_forward(self) -> None:
        self.__step_counter += 1
        
    def __get_steps(self) -> int:
        return self.__step_counter
    
    def _print_steps(self, name) -> None:
        print(f"The {name} has moved {self.__get_steps()} steps.")
    
    @abstractmethod
    def make_sound(self) -> None:
        pass
    
class Dog(Animal):
    
    def make_sound(self) -> None:
        super().step_forward()
        print('Woof!')
        
    def print_steps(self) -> None:
        super()._print_steps('Dog')

class Cat(Animal):
    
    def make_sound(self) -> None:
        super().step_forward()
        print('Meow.')
        
    def print_steps(self) -> None:
        super()._print_steps('Cat')
        
dog = Dog()
dog.make_sound()
dog.make_sound()
dog.print_steps()

cat = Cat()
cat.make_sound()
cat.print_steps()
cat.make_sound()
cat.make_sound()
cat.print_steps()
