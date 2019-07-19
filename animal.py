class (Animal):
 def __init__(self, nome, dono):
    self.nome = nome 
    self.dono = dono

class Gato(Animal):
    def __init__(self, nome, dono, raca):
        self.nome = nome 
        self.dono = dono
        self.raca = raca

    def miar(self):
        print('Minhaaaauuu')

class Cachorro(Animal):
    def latir(self):
        print('Au auu')

gato = Gato('xuxuzinho', 'Matheus', 'Siames')
cachorro = Cachorro ('Rex', 'Barbára')
animal = Animal ('Toddy', 'Gabriel')

print(cachorro.nome)
print(cachorro.dono)
print(gato.raca)


