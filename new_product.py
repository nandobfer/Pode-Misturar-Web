import json, requests, os

handler_url = 'http://localhost:5000/new_product/'

def color(color, text, reset = True):
    os.system('color')
    reset_color = '\033[0m'
    colors = {
        'red': '\033[0;31m',
        'green': '\033[0;32m',
        'yellow': '\033[0;33m',
        'blue': '\033[0;34m',
        'purple': '\033[0;35m'
    }
    if reset:
        return colors[color]+text+reset_color
    else:
        return colors[color]+text

def newProduct():
    global handler_url

    name = input("Digite o "+ color('yellow', 'nome') +" do produto: "+ color('blue', '', False))
    print(color('red', ''), end='')
    about = input(f"Digite uma {color('yellow', 'descrição')} sobre {color('blue', name)}: ")
    formula = input(f"Digite a {color('yellow', 'fórmula')} de {color('blue', name)}: ")
    
    data = {
        "Nome": name,
        "Sobre": about,
        "Formula": formula
    }
    
    new_data = json.dumps(data)
    
    print('\nConectando ao banco de dados, '+ color('yellow', 'aguarde.'))
    post = requests.post(handler_url, json = new_data)
    response = post.text
    if response:
        print(f"{color('blue', name)} cadastrado com {color('green', 'sucesso')}!\n")
    else:
        print(color('red', 'Não foi possível cadastrar o produto.\n'))
    
newProduct()