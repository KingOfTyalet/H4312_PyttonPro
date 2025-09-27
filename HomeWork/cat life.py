import random


class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50

    def eat(self):
        self.hunger -= 10
        print(f"{self.name} їсть")

    def play(self):
        self.happiness += 10
        self.hunger += 5
        print(f"{self.name} грається")

    def sleep(self):
        self.hunger += 3
        self.happiness += 5
        print(f"{self.name} спить")

    def status(self):
        print(f"{self.name}: голод {self.hunger}, щастя {self.happiness}")


class House:
    def __init__(self):
        self.food = 100

    def give_food(self, cat):
        if self.food > 0:
            self.food -= 10
            cat.eat()
            print(f"Їжа в домі: {self.food}")
        else:
            print("Їжа закінчилась!")


class Human:
    def __init__(self, name):
        self.name = name

    def play_with_cat(self, cat):
        print(f"{self.name} грається з {cat.name}")
        cat.play()


# Симуляція
cat = Cat("Мурчик")
house = House()
owner = Human("Власник")

for day in range(1, 6):
    print(f"\n--- День {day} ---")

    action = random.choice(["eat", "play", "sleep"])

    if action == "eat":
        house.give_food(cat)
    elif action == "play":
        owner.play_with_cat(cat)
    else:
        cat.sleep()

    cat.status()