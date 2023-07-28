import requests

#def para obtener un chiste random
def getRandomJoke ():
    url_random = "https://api.chucknorris.io/jokes/random"
    get_joke = requests.get (url_random)
    if get_joke.status_code == 200:
        print ("Chiste random\n",get_joke.json()["value"])
    else:
        print ("error al realizar la solicitud")

#def para obtener la lista de categorias
def getCategoriesList ():
    url_list = "https://api.chucknorris.io/jokes/categories"
    get_catergories = requests.get (url_list)
    if get_catergories.status_code == 200:
        list = get_catergories.json ()
        return list
    else:
        print ("error al realizar la solicitud")

#def para obtener un chiste de una categoria especifica       
def getCategoryJoke (category):
    url_catergory = f"https://api.chucknorris.io/jokes/random?category={category}"
    category_selected = requests.get (url_catergory)
    if category_selected.status_code == 200:
        print (category_selected.json ()["value"])
    else:
        print ("error al realizar la solicitud")


