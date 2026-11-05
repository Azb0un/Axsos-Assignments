class Animal:
    def __init__(self, name, age, health, happiness):
        self.animal_name = name
        self.animal_age = age
        self.health_level = health
        self.happiness_level = happiness

    def display_info(self):
        print(f"Animal name:{self.animal_name}, age: {self.animal_age}, health level: %{self.health_level}, happiness level: %{self.happiness_level} ")
        return self
    def feed(self):
        self.health_level = min(self.health_level + 10, 100)
        self.happiness_level = min(self.happiness_level + 10, 100)
        return self


class Mammoth(Animal):
    def __init__(self, name, age, health, happiness,strengh):
        super().__init__(name, age, health, happiness)
        self.strengh_level = strengh

    def feed(self):
        super().feed()
        self.strengh_level = min(self.strengh_level+3, 100)
        return self

    def display_info(self):
        super().display_info()
        print(f"Strength level: %{self.strengh_level}")
        return self

class Sloth(Animal):
    def __init__(self, name, age, health, happiness, stealth):
        super().__init__(name, age, health, happiness)
        self.stealth_level = stealth

    def feed(self):
        super().feed()
        self.stealth_level = min(self.stealth_level+10, 100)
        return self

    def display_info(self):
        super().display_info()
        print(f"Stealth level: %{self.stealth_level}")
        return self


class Tiger(Animal):
    def __init__(self, name, age, health, happiness, stamina):
        super().__init__(name, age, health, happiness)
        self.stamina_level = stamina

    def feed(self):
        super().feed()
        self.stamina_level = min(self.stamina_level+20, 100)
        return self

    def display_info(self):
        super().display_info()
        print(f"Stamina level: %{self.stamina_level}")
        return self


manny = Mammoth("Manny", 30, 80, 70, 90 )
ellie = Mammoth("Ellie", 15, 80, 85, 65 )
peaches = Mammoth("Peaches", 1 , 90 , 100 , 40  )

diego = Tiger("Diego", 30 , 80 , 60 , 80 )
shira = Tiger("Shira", 20 , 90 , 95 , 90 )

sid = Sloth("Sid" , 20 , 70 , 90 , 90)

class Zoo:
    def __init__(self, name):
        self.animals = []
        self.zoo_name = name

    def add_animal(self, animal):
        self.animals.append(animal)
        return self

    def remove_animal(self, animal):
        self.animals.remove(animal)
        return self

    def count_animals(self):
        count = 0 
        for i in range(len(self.animals)):
            count += 1
        print(f"Numbers of animals in {self.zoo_name}: {count}") 
        

    def feed_all(self):
        for animal in self.animals:
            animal.feed()
        return self

    def print_all_info(self):
        print("-" * 30, self.zoo_name, "-" * 30)
        for animal in self.animals:
            animal.display_info()
        return self
        


zoo1 = Zoo("The Falls")

zoo1.add_animal(manny).add_animal(ellie).add_animal(peaches).add_animal(diego).add_animal(shira).add_animal(sid).feed_all().print_all_info().count_animals()
