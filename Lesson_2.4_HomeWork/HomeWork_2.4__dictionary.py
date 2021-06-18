############################
#Англо-Французкий Словарь
############################
from pprint import pprint


vocabulary = {
    "Apple":"Pomme",
    "table":"lampe",
    "lamp":"stylo",
    "ruska":"une voiture"
}
pprint(vocabulary)
#добавление
vocabulary ["flower"] = ["fleur"]
pprint(vocabulary)

#удаление
del vocabulary ["Apple"]
pprint(vocabulary)
#Поиск
pprint(vocabulary["lamp"])
pprint(vocabulary.get("ruska"))
pprint(vocabulary.get("Apple", "нет ключа"))

#Замена

vocabulary["ruska"] = "не правда"

pprint(vocabulary)

######################
#Вывод
######################
# {'Apple': 'Pomme', 'lamp': 'stylo', 'ruska': 'une voiture', 'table': 'lampe'}
# {'Apple': 'Pomme',
#  'flower': ['fleur'],
#  'lamp': 'stylo',
#  'ruska': 'une voiture',
#  'table': 'lampe'}
# {'flower': ['fleur'], 'lamp': 'stylo', 'ruska': 'une voiture', 'table': 'lampe'}
# 'stylo'
# 'une voiture'
# 'нет ключа'
# {'flower': ['fleur'], 'lamp': 'stylo', 'ruska': 'не правда', 'table': 'lampe'}
#
# Process finished with exit code 0



