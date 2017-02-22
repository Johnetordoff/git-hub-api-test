
current_year = 2017
class Animal(object):
	def __init__(self):
		self.self = self

#Dog is-a Animal
	class Dog(Animal):

		def __init__(self, name):
		## Dog  has-a name?
			self.name = name
	
class Pet(Animal):
    def __init__(self, name, year_of_birth, owner, color):
        Animal.__init__(self) 
        self.name = name
        self.age = current_year - year_of_birth
        self.owner = owner
  

class Dog(Pet):
    def __init__(self, name, year_of_birth, owner, color):
        Pet.__init__(self, name, year_of_birth, owner)
        self.color = color
    

## rover is-a Dog
rover = Dog("rover", 2011, "Dani", "Black")
	
	
