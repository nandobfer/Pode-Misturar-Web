import json
from config import *

def getData():
    with open(DATABASE, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data
    
def writeDatabase(data):
    with open(DATABASE, "w") as write_file:
            json.dump(data, write_file, indent=4)
    return True
    
def newProduct():
    data = getData()
    id = len(data)
    name = input("Digite o nome do produto: ")
    about = input(f"Digite uma descrição sobre '{name}': ")
    formula = input(f"Digite a formula de '{name}': ")
    
    data[id] = {
        NOME: name,
        SOBRE: about,
        FORMULA: formula
    }
    
    writeDatabase(data)
    
        
newProduct()