from browser import document, alert, html, bind

database = eval(document['build_datalist'].attrs['database'])
clicked = False

def mix(products):
    for item in products:
        for next_item in products:
            if item["Nome"] in next_item["Perigo"]:
                return False
            
    return True

def resetApp(button = False):
    # resetting mix button
    document['mix-btn'].style.backgroundColor = ""
    document['mix-btn'].text = "Misturar"
    document['mix-btn'].style.color = ""
    
    if button: 
        # reseting inputs
        for element in document.select('.inputs'):
            element.value = ''   
            
        # reseting images
        for child in document.select('.images-container'):
           for element in child:
               element.clear()

@bind("#mix-btn", "click")
def buttonClicked(ev):
    global clicked
    if not clicked:
        clicked = True
        elements = []
        for element in document.select('.inputs'):
            elements.append(element.value)
        
        # getting object from inserted string 
        products = []   
        for item in elements:
            for product in database:
                if item == database[product]["Nome"]:
                    item = database[product]
                    products.append(item)
        
        # mixing them            
        result = mix(products)
        ev.target.style.color = "#121051"
        if result:
            ev.target.style.backgroundColor = "#03FF89"
            ev.target.text = "Pode!"
        else:
            ev.target.style.backgroundColor = "#ef5b5b"
            ev.target.text = "Não Pode!"
    else:
        clicked = False
        resetApp(True)
        
@bind(".inputs", "focus")
def focusInputs(ev):
    resetApp()
        
        