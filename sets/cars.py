showroom = set()

showroom.update({'Toyota Corolla', 'Honda Civic', 'Tesla Model S', 'Maserati GranTurismo'})
print(len(showroom))
showroom.add("Toyota Corolla")
print(showroom)
showroom.update({'Volkswagen Beetle Convertable', 'Smart ForTwo'})
showroom.discard('Honda Civic')

junkyard = set(['Toyota Camry', 'Honda Civic', 'Smart ForTwo', 'Tesla Model 3'])

same = showroom.intersection(junkyard)
both = showroom.union(junkyard)
withoutOneJunkyardCar = both.discard('Toyota Camry')

