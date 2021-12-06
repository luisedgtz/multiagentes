# %%
# Model design
#from _typeshed import Self
import agentpy as ap
import numpy as np

# Visualization

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.animation as animation
plt.rcParams["animation.html"] = "jshtml"
matplotlib.rcParams['animation.embed_limit'] = 2**128

import IPython

import random



promedioCalculado = []
promedioAzar = []
promedioFijo = []
pathNorteEste = [(1,14), (2,14), (3,14), (4,14), (5,14), (6,14), (7,14), (8,14), (9,14), (10,14), (11,14), (12,14), (13,15), (14,16), (15,16), (16,17), (16,18), (16,19), (16,20), (16,21), (16,22), (16,23), (16,24), (16,25), (16,26), (16,27), (16,28), (16,29)]
pathNorteSur = [(1,14), (2,14), (3,14), (4,14), (5,14), (6,14), (7,14), (8,14), (9,14), (10,14), (11,14), (12,14), (13,14), (14,14), (15,14), (16,14), (17,14), (18,14), (19,14), (20,14), (21,14), (22,14), (23,14), (24,14), (25,14), (26,14), (27,14), (28,14), (29,14)]
pathNorteOeste = [(1,14), (2,14), (3,14), (4,14), (5,14), (6,14), (7,14), (8,14), (9,14), (10,14), (11,14), (12,14), (13,14), (14,13), (14,12), (14,11), (14,10), (14,9), (14,8), (14,7), (14,6), (14,5), (14,4), (14,3), (14,2), (14,1), (14,0)]

pathSurNorte = [(28,16), (27,16), (26,16), (25,16), (24,16), (23,16), (22,16), (21,16), (20,16), (19,16), (18,16), (17,16), (16,16), (15,16), (14,16), (13,16), (12,16), (11,16), (10,16), (9,16), (8,16), (7,16), (6,16), (5,16), (4,16), (3,16), (2,16), (1,16), (0,16)]
pathSurEste = [(28,16), (27,16), (26,16), (25,16), (24,16), (23,16), (22,16), (21,16), (20,16), (19,16), (18,16), (17,16), (16,17), (16,18), (16,19), (16,20), (16,21), (16,22), (16,23), (16,24), (16,25), (16,26), (16,27), (16,28), (16,29)]
pathSurOeste = [(28,16), (27,16), (26,16), (25,16), (24,16), (23,16), (22,16), (21,16), (20,16), (19,16), (18,16), (17,16), (16,15), (15,14), (14,13), (14,12), (14,11), (14,10), (14,9), (14,8), (14,7), (14,6), (14,5), (14,4), (14,3), (14,2), (14,1), (14,0)]

pathEsteOeste = [(14,28), (14,27), (14,26), (14,25), (14,24), (14,23), (14,22), (14,21), (14,20), (14,19), (14,18), (14,17), (14,16), (14,15), (14,14), (14,13), (14,12), (14,11), (14,10), (14,9), (14,8), (14,7), (14,6), (14,5), (14,4), (14,3), (14,2), (14,1), (14,0)]
pathEsteNorte = [(14,28), (14,27), (14,26), (14,25), (14,24), (14,23), (14,22), (14,21), (14,20), (14,19), (14,18), (14,17), (13,16), (12,16), (11,16), (10,16), (9,16), (8,16), (7,16), (6,16), (5,16), (4,16), (3,16), (2,16), (1,16), (0,16)]
pathEsteSur = [(14,28), (14,27), (14,26), (14,25), (14,24), (14,23), (14,22), (14,21), (14,20), (14,19), (14,18), (14,17), (15,16), (16,15), (17,14), (18,14), (19,14), (20,14), (21,14), (22,14), (23,14), (24,14), (25,14), (26,14), (27,14), (28,14), (29,14)]

pathOesteEste = [(16,1), (16,2), (16,3), (16,4), (16,5), (16,6), (16,7), (16,8), (16,9), (16,10), (16,11), (16,12), (16,13), (16,14), (16,15), (16,16), (16,17), (16,18), (16,19), (16,20), (16,21), (16,22), (16,23), (16,24), (16,25), (16,26), (16,27), (16,28), (16,29)]
pathOesteSur = [(16,1), (16,2), (16,3), (16,4), (16,5), (16,6), (16,7), (16,8), (16,9), (16,10), (16,11), (16,12), (16,13), (17,14), (18,14), (19,14), (20,14), (21,14), (22,14), (23,14), (24,14), (25,14), (26,14), (27,14), (28,14), (29,14)]
pathOesteNorte = [(16,1), (16,2), (16,3), (16,4), (16,5), (16,6), (16,7), (16,8), (16,9), (16,10), (16,11), (16,12), (16,13), (15,14), (14,15), (13,16), (12,16), (11,16), (10,16), (9,16), (8,16), (7,16), (6,16), (5,16), (4,16), (3,16), (2,16), (1,16), (0,16)]




def crearCalle(model):
  size = model.size
  barrera = int((size - 6) / 2)
  range_calle = range(barrera+1, barrera+6, 1)
  for i in range(size):
    if i not in range_calle:
      street = Street(model)
      street.setup()
      model.grid.add_agents([street], positions = [(i, barrera)], empty=True)
      model.grid.add_agents([street], positions = [(i, barrera+6)], empty=True)
  
  for j in range(size):
    if j not in range_calle:
      street = Street(model)
      street.setup()
      model.grid.add_agents([street], positions = [(barrera, j)], empty=True)
      model.grid.add_agents([street], positions = [(barrera+6, j)], empty=True)
  
  for i in model.posSemaforo:
      model.grid.agents[i].color = 1
  

def escogerAccion(model):
  norte = 0
  sur = 0
  este = 0
  oeste = 0
  norte = len(model.grid.agents[0:12,14])
  sur = len(model.grid.agents[18:29,16])
  este = len(model.grid.agents[14,18:29])
  oeste = len(model.grid.agents[16,0:12])
  lista = [norte, este, sur, oeste]
  listaRecompensa = sorted(lista)
  if listaRecompensa[3] == norte:
    return 0
  elif listaRecompensa[3] == sur:
    return 2
  elif listaRecompensa[3] == este:
    return 1
  elif listaRecompensa[3] == oeste:
    return 3


class Street(ap.Agent):
  def setup(self):
    self.color = 4
    
    
class Semaforo(ap.Agent):
  def setup(self):
    self.action = 0
    self.availableActions =[(1,0,0,0), (0,1,0,0), (0,0,1,0),(0,0,0,1)]
    self.grid = self.model.grid
    self.valores = (0,0,0,0)
    self.listaValores = []
    self.count = 0
    
    
    
  def step(self):
    self.count += 1
    self.listaValores.append(self.valores)
    if self.count == 7:
      self.valores = (0,0,0,0)

    if self.model.t % 10 == 0:
      self.action = escogerAccion(self)
      self.valores = self.availableActions[self.action]
      self.count = 0
  


class Car(ap.Agent):
  
  def setup(self):
    self.color = 0
    self.grid = self.model.grid
    self.waitTime = 0
    self.Parar = False
    self.move = -1
    self.stepsAInter = 0
    self.llegoInter = False
    
  
  def setupPos(self):
    self.position = self.grid.positions[self]
    self.directionFrom = self.model.posIniciales.index(self.position)
    self.directionTo = random.randrange(0,4,1)
    self.path = []
    if self.directionFrom == self.directionTo and self.directionFrom == 3:
      self.directionTo = self.directionTo - 1
    elif self.directionFrom == self.directionTo:
      self.directionTo = self.directionTo + 1

    if self.directionFrom == 0 and self.directionTo == 1:
        self.path = pathNorteEste
    elif self.directionFrom == 0 and self.directionTo == 2:
        self.path = pathNorteSur
    elif self.directionFrom == 0 and self.directionTo == 3:
        self.path = pathNorteOeste
    elif self.directionFrom == 2 and self.directionTo == 1:
      self.path = pathSurEste
    elif self.directionFrom == 2 and self.directionTo == 0:
      self.path = pathSurNorte
    elif self.directionFrom == 2 and self.directionTo == 3:
      self.path = pathSurOeste
    elif self.directionFrom == 1 and self.directionTo == 3:
      self.path = pathEsteOeste
    elif self.directionFrom == 1 and self.directionTo == 0:
      self.path = pathEsteNorte
    elif self.directionFrom == 1 and self.directionTo == 2:
      self.path = pathEsteSur
    elif self.directionFrom == 3 and self.directionTo == 1:
      self.path = pathOesteEste
    elif self.directionFrom == 3 and self.directionTo == 2:
      self.path = pathOesteSur
    elif self.directionFrom == 3 and self.directionTo == 0:
      self.path = pathOesteNorte

  def update(self):
    if self.position in self.model.posFinales:
      self.color = 3
    else:
      self.position = self.grid.positions[self]
  
  def checarSemaforo(self):
    stop = False
    semaforo = self.model.semaforo
    if self.position in self.model.posIntersection:
      self.llegoInter = True
      if self.model.semaforo.valores[self.directionFrom] == 0:
        self.Parar = True
        self.waitTime = self.waitTime + 1
        return True
      else:
        return False
    if not self.llegoInter:
      self.stepsAInter += 1
    if self.position in self.model.posFinales:
      return True
    return False
    
  def getWaitingTime(self):
    if self.Parar == True:
      self.model.totalWaitTime += self.waitTime

  def avanzar(self):
    if self.position in self.model.posFinales or self.move + 1 >= len(self.path):
        return
    
    if not self.checarSemaforo():
      if self.path[self.move+1] in self.grid.empty or self.path[self.move+1] in self.model.posFinales or self.path[self.move+1] in self.model.posMedio:
        self.move += 1
        self.model.grid.move_to(self, self.path[self.move])
      else:
        self.Parar = True
        self.waitTime = self.waitTime + 1

    

class Intersection(ap.Model):
  def setup(self):
    self.direccion = "Alto"
    self.Esperaron = 0
    self.promedio = 0
    self.totalWaitTime = 0
    self.size = self.p.size
    m = int(self.size/2 - 1)
    k = int(self.size/2 + 1)
    self.norte = (0, m)
    self.sur = (self.size-1, k)
    self.este = (m, self.size-1)
    self.oeste = (k, 0)
    self.posIniciales = [self.norte, self.este, self.sur, self.oeste]
    self.posIntersection = [(k,12),(18,k),(m,18),(12,m)]
    self.posFinales = [(0,k),(self.size-1,m),(k,self.size-1),(m,0)]
    self.posMedio = [(13,13),(13,14),(13,15),(13,16),(13,17),(14,13),(14,14),(14,15),(14,16),(14,17),(15,13),(15,14),(15,15),(15,16),(15,17),(16,13),(16,14),(16,15),(16,16),(16,17),(17,13),(17,14),(17,15),(17,16),(17,17)]
    self.posSemaforo = [(12,12),(18,18),(12,18),(18,12)]
    self.grid = ap.Grid(self, (self.size, self.size),  track_empty= True)
    self.agents = ap.AgentList(self, 1, Car)
    self.semaforo = Semaforo(self)
    self.semaforo.setup()
    self.grid.add_agents(self.agents, positions = [self.norte, self.sur], empty=True)
    self.agents.setupPos()
    crearCalle(self)
    

  def addNewAgents(self):
        if self.t % 3 == 0:  
          newAgents = ap.AgentList(self, 1, Car)
          position = random.choice(self.posIniciales)
          self.grid.add_agents(newAgents, positions= [position], empty=True)
          newAgents.setupPos()
          self.agents.append(newAgents)


  def getDireccion(self):
    if self.semaforo.valores[0] == 1:
      self.direccion = "Norte"
    elif self.semaforo.valores[1] == 1:
      self.direccion = "Este"
    elif self.semaforo.valores[2] == 1:
      self.direccion = "Sur"
    elif self.semaforo.valores[3] == 1:
      self.direccion = "Oeste"
    else:
      self.direccion = "Alto"
  
  def step(self):
    self.agents.avanzar()
    self.semaforo.step()
    self.addNewAgents()
    
    
  

  def update(self):
    self.getDireccion()
    self.totalWaitTime = 0   
    self.agents.getWaitingTime()
    self.agents.update()
    if self.totalWaitTime > 0:
      self.promedio = round(self.totalWaitTime / len(self.agents))
    self.record('promedio')
    self.Esperaron = len(self.agents.select(self.agents.Parar == True))
    self.record('Esperaron')
    

  def end(self):
    # Measure segregation at the end of the simulation
    self.model.record('promedio')
    self.model.record('Esperaron')
    self.agents.record('stepsAInter')
    self.semaforo.record('listaValores')
    promedioCalculado.append(self.promedio)





parameters = {
    'size': 30,
    'steps': 250,
    'seed': 42,
    #Posibles posiciones para los carros
}


for i in range(100):
  model = Intersection(parameters)
  results = model.run()

plt.plot(promedioCalculado)
plt.ylabel('Promedio de tiempo sin moverse')
plt.xlabel('Iteración del modelo')
 
# displaying the title
plt.title("Modelo semáforo Calculando Flujo")
plt.show()


#%%
def animation_plot(model, ax):
  colorList = ['blue','red','green','gray','white']
  group_grid = model.grid.attr_grid('color')
  ap.gridplot(group_grid,cmap=colors.ListedColormap(colorList), ax=ax)
  ax.set_title(f"Modelo de semáforo Calculando Flujo \nTime-step: {model.t} | "
                 f"Tiempo de espera promedio: {model.promedio} | "
                 f"Interseccion en verde: {model.direccion} ")
  ax.set_facecolor('gray')

fig, ax = plt.subplots(figsize=(7,7))
model = Intersection(parameters)

animation = ap.animate(model, fig, ax, animation_plot)
IPython.display.HTML(animation.to_jshtml())



# %%
