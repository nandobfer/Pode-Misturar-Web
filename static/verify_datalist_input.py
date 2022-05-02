from browser import document, alert, html, bind

# getting database from script id and attribute in html
database = eval(document['build_datalist'].attrs['database'])

@bind(".inputs", "change")
def image(ev):
    match = False
    # print(ev.target.value)
    for item in database:
        
        if ev.target.value == database[item]["Nome"]:
            match = True
            # print(database[item]["Nome"])
            print(ev.target.id)
            if ev.target.id == "product-1":
                document["product-1-image"].clear()
                document["sum"].clear()
                document["product-1-image"] <= html.IMG(src=database[item]["Imagem"])
                document["sum"] <= html.IMG(src="/static/images/mais.png", height=100, id='sum')
            elif ev.target.id == "product-2":
                document["product-2-image"].clear()
                document["sum"].clear()
                document["sum"] <= html.IMG(src="/static/images/mais.png", height=100, id='sum')
                document["product-2-image"] <= html.IMG(src=database[item]["Imagem"])
        
    if not match:
        alert('Selecione um item da lista')