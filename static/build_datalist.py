from browser import document, alert, html

# getting database from script id and attribute in html
database = eval(document['build_datalist'].attrs['database'])

def addDatalist(element):
    global database
    for item in database:
        element <= html.OPTION(value=database[item]["Nome"])
        
for element in document.select('.datalist-root'):
    addDatalist(element)