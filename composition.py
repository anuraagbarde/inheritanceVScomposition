from abc import ABC, abstractmethod

class AnimalMovement:
    __step_counter: int
    
    def __init__(self) -> None:
        self.__step_counter = 0

    def step_forward(self) -> None:
        self.__step_counter += 1
    
    def __get_steps(self) -> int:
        return self.__step_counter

    def print_steps(self, name) -> None:
        print(f"The {name} has moved {self.__get_steps()} steps.")
    

class AnimalWithSound(ABC):
    
    @abstractmethod
    def make_sound(self) -> None:
        pass
    
class AnimalThatWalk(ABC):
    
    @abstractmethod
    def make_sound(self) -> None:
        pass
    
    @abstractmethod
    def step_forward(self) -> None:
        pass
        
    @abstractmethod
    def print_steps(self) -> None:
        pass
    
class Dog(AnimalWithSound, AnimalThatWalk):
    animal_movement: AnimalMovement
    
    def __init__(self):
        self.animal_movement = AnimalMovement()
    
    def make_sound(self) -> None:
        self.step_forward()
        print('Woof!')
    
    def step_forward(self) -> None:
        self.animal_movement.step_forward()
        
    def print_steps(self):
        self.animal_movement.print_steps('Dog')

class Cat(AnimalWithSound, AnimalThatWalk):
    animal_movement: AnimalMovement
    
    def __init__(self):
        self.animal_movement = AnimalMovement()
    
    def make_sound(self) -> None:
        self.step_forward()
        print('Meow.')
    
    def step_forward(self) -> None:
        self.animal_movement.step_forward()
    
    def print_steps(self):
        self.animal_movement.print_steps('Cat')
        
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
