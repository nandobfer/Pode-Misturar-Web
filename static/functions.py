import json
from static.config import *

def getData():
    with open(DATABASE, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data
    
def writeDatabase(data):
    with open(DATABASE, "w") as write_file:
            json.dump(data, write_file, indent=4)
    return True

def addDontMix(data, dont_mix, new_item):
    for item in dont_mix:
        for product in data:
            if data[product][NOME] == item:
                if not new_item in data[product][PERIGO]:
                    data[product][PERIGO].append(new_item)
    
def newProduct(new_data):
    data = getData()
    id = len(data)
    
    data[id] = new_data
    addDontMix(data, new_data[PERIGO], new_data[NOME])
    try:
        writeDatabase(data)
        return True
    except:
        return False