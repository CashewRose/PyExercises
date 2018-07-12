
class Cars():
    def __init__(self, listing=[], names=[()]):
        self.car_brands = listing
        self.car_names = names
        self.write_make()
        self.write_model()

    def read_make(self):
        with open("car-makes.txt", "r") as make:
            pretty = make.readlines()
            return [f'{purdy_car.strip()}' for purdy_car in pretty]
            
    def read_model(self):
        with open("car-models.txt", "r") as model:
            pretty = model.readlines()
            return [f"{purdy_car.strip()}" for purdy_car in pretty]

    def write_make(self):
        with open("car-makes.txt", "w") as makes:
            for make in self.car_brands:
                makes.write(make + "\n")

    def write_model(self):
        with open("car-models.txt", "w") as models:
            for tuple in self.car_names:
                models.write(f'{tuple[0]} = {tuple[1]} \n')

    def dictionary_creation(self):
        finalized = dict()
        makes = self.read_make()
        models = self.read_model()

        for make in makes:
            single_letter = make[0]
            for model in models: 
                if single_letter == model[0]:
                    try: 
                        finalized[make].append(model[4:])

                    except KeyError:
                        finalized[make] = list()
                        finalized[make].append(model[4:])
        print(finalized)    

car_brands = ["Toyota", "Nissan", "Honda", "Volkswagen", "Ford", "Chevy", "Aston Martin"]

car_names = [
    ("F", "Fiesta"),
    ("T", "Corolla"),
    ("N", "Altima"),
    ("H", "Civic"),
    ("V", "Bug"),
    ("F", "Focus"),
    ("C", "Impala"),
    ("T", "Prius"),
    ("A", "Vantage")
]

car = Cars(car_brands, car_names)

print(car.read_model())
print(car.read_make())
car.dictionary_creation()