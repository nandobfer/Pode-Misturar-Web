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
    
def newProduct(new_data):
    data = getData()
    id = len(data)
    
    data[id] = new_data
    
    try:
        writeDatabase(data)
        return True
    except:
        return False