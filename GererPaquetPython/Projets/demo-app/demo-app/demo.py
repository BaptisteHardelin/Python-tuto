import requests

r = requests.get('https://openclassrooms.com/fr/courses/6951236-mettez-en-place-votre-environnement-python/7014018-creez-votre-premier-environnement-virtuel')
print(r.status_code)