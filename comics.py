import requests
import bs4
import random
import os
import urllib.request
import webbrowser


def fileExistence(title):
    for x in os.listdir('./pics/'):
        if x == (title + '.png'):
            return True
    return False


startInt = random.randint(1, 2187)

print('How many comics do you want(1-100)')
numCom = input()
print('And do you wish to save them(y|n):')
save = input()

try:
    os.makedirs('pics')
except FileExistsError:
    print('Directory already created!')

for i in range(startInt, startInt + int(numCom)):
    res = requests.get('https://xkcd.com/' + str(i))
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elem = soup.select('#ctitle')
    nameOfFile = elem[0].text.replace(' ', '_').replace('\'', '').lower()
    webbrowser.open('https://imgs.xkcd.com/comics/' + nameOfFile + '.png')
    print(nameOfFile)
    if save.lower() == 'y' and not fileExistence(nameOfFile):
        urllib.request.urlretrieve(
            'https://imgs.xkcd.com/comics/' + nameOfFile + '.png', './pics/' + nameOfFile + '.png')
        print(nameOfFile + ' comic saved!')
