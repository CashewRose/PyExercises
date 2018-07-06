zoo = ('chinchillas', 'pandas', 'minks', 'peacocks')

minx = zoo[2]

def check_in_zoo(creature="monkeys"):
  for animal in zoo:
      if creature == animal:
        print("There are " + creature + " in this zoo.")

check_in_zoo("minks")
check_in_zoo("mink")

(chinchillas, pandas, minks, peacocks) = zoo
print(pandas)

zoo = list(zoo)

zoo.extend(["sabertooth tigers", "unicorns", "reindeers"])

zoo = tuple(zoo)