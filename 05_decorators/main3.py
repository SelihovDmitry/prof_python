
import requests
from main2 import logger

@logger('herolog.txt')
def smartest_hero(heroes): # получаем список героев из которых надо выбрать самого умного (intelligence)
    hero_intelligense = {}
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    data = response.json()
    for hero in data:
        if hero['name'] in heroes:
            hero_intelligense[hero['name']] = hero['powerstats']['intelligence']
    smartest = max(hero_intelligense)
    print(f'Самый умный супергерой {smartest}, его уровень intelligence = {hero_intelligense[smartest]}')
    return smartest

if __name__ == '__main__':
    smartest_hero(['Hulk', 'Captain America', 'Thanos'])