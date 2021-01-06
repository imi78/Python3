class Zoo:
  __animals = 0

  def __init__(self, name):
    self.name = name
    self.mammals = []
    self.fishes = []
    self.birds = []


  def add_animal(self, species, name):
    if species == 'mammal':
      self.mammals.append(name)

    elif species == 'fish':
      self.fishes.append(name)
    
    elif species == 'bird':
      self.birds.append(name)
    Zoo.__animals += 1


    def get_info(self, species):
      animals_to_display = []
      if species == 'mammal':
        animals_to_display = self.mammals
      elif species == 'fish':
        animals_to_display = self.fishes
      elif species == 'bird':
        animals_to_display = self.birds

      species = species.capitalize() + "es" if species == "fish" else species.capitalize() + "s"

      return f"{species} in zoo: {self.name}: {', '.join(animals_to_display)} \n Total animals: {Zoo.__animals}"
      
zoo = Zoo("Great Zoo")
animals = 3


for el in range(animals):
  species, animal_name = input().split()
  zoo.add_animal(species, animal_name)
required_species = input()
print(zoo.get_info(required_species))