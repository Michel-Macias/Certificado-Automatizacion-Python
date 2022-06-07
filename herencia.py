class Clothing:
    # Creamos clase 
  stock={ 'name': [],'material' :[], 'amount':[]}
  # Se crea un diccionario al instanciar el objeto de clase Clothing
  '''
    Se crean el método inicializador que crea los atributos (material, y name, para el
    que le pasamos el sufijo self)
    para el objeto instanciado y el método add_item para añadir el objeto al diccionario
    de la clase con unos nuevos atributos (material, amount o cantidad).
    El método Stock_by_Material nos cuenta mediante un for e iterando por el diccionario
    la cantidad de prendas que tenemos en el diccionario que almacena el stock que son
    del material pasado como argumento
  '''

  def __init__(self,name):
    material = ""
    self.name = name
  
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
    
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock['material']:
      if item == material:
        count += Clothing.stock['amount'][n]
        n+=1
    return count

class shirt(Clothing):
  material="Cotton"

class pants(Clothing):
  material="Cotton"
  
polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)
# IMPORTANTE probar code in Python Tutor