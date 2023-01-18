from __future__ import division
from ast import Div
from tkinter import ANCHOR
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import os

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

#Dining Hall Info
url = "https://dining.umich.edu/menus-locations/dining-halls/mosher-jordan/"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
[breakfast, lunch, dinner] = soup.select('div#mdining-items div.courses') 

#MDaily info
url2 = "https://www.michigandaily.com/"
req2 = requests.get(url2, headers)
soup2 = BeautifulSoup(req2.content, 'html.parser')

#MAthletics info
url3 = "https://mgoblue.com/"
req3 = requests.get(url3, headers)
soup3 = BeautifulSoup(req3.content, "html.parser")

def starterMessage(dt_string):
    print("\n" + "Hello! It is " + dt_string + "." + "\n" + "\n" + "Here's Mojo's menu today:" + "\n")

def get_pretty_time(): 
    now = datetime.now()
    dt_string = now.strftime("%H:%M")
    dt_string = dt_string.replace(":", "")
    easyreadtime = int(dt_string)

    if (int(dt_string) > 1300):
        easyreadtime-= 1200
    if (len(str(easyreadtime)) == 4):
        easyreadtime = str(easyreadtime)[:2] + ':' + str(easyreadtime)[2:]
    if (len(str(easyreadtime)) == 3):
        easyreadtime = str(easyreadtime)[:1] + ':' + str(easyreadtime)[1:]

    return str(easyreadtime);

def get_numerical_time(): 

    now = datetime.now()
    dt_string = now.strftime("%H:%M")
    dt_string = dt_string.replace(":", "")

    return int(dt_string);

def printAllBreakfast(dt_string):

    print("Hello! It is " + dt_string + "." + "\n" + "\n" + "Here's Mojo's breakfast menu today:" + "\n")
    brekFoods = breakfast.select('div.item-name')

    if (datetime.today().isoweekday() == 4):
        for food in brekFoods:
            if ("Scrambled Eggs" not in food.text):
                print(food.text)
        print("\n" + "And of course..." + "\n" + "Powdered eggs.")
    if (datetime.today().isoweekday() != 4):
        for food in brekFoods:
            print('\t' + food.text)

def printAllLunch(dt_string):
    print("Hello! It is " + dt_string + "." + "\n" + "\n" + "Here's Mojo's lunch menu today:" + "\n")
    pizzaCounter = 0
    lunchFoods = lunch.select('div.item-name')
    for food in lunchFoods:
        foodstr = food.text
        if ("Pizza" not in foodstr):
            print('\t' + food.text)
    print("\n" + "And here are the pizzas:" + "\n")

    for food in lunchFoods:
        foodstr = food.text
        if ("Pizza" in foodstr):
            pizzaCounter += 1
    if (pizzaCounter >= 1):
        for food in lunchFoods:
            foodstr = food.text
            if ("Pizza" in foodstr):
                print('\t' + food.text)
    if (pizzaCounter == 0):
        print("and no pizza :(")

def printAllDinner(dt_string):

    print("Hello! It is " + dt_string + "." + "\n" + "\n" + "Here's Mojo's dinner menu today:" + "\n")
    pizzaCounter = 0

    dinnerFoods = dinner.select('div.item-name')
    for food in dinnerFoods:
        foodstr = food.text
        if ("Pizza" not in foodstr):
            print('\t' + food.text)
    print("\n" + "And here are the pizzas:" + "\n")

    for food in dinnerFoods:
        foodstr = food.text
        if ("Pizza" in foodstr):
            pizzaCounter += 1
    if (pizzaCounter >= 1):
        for food in dinnerFoods:
            foodstr = food.text
            if ("Pizza" in foodstr):
                print('\t' + food.text)
    if (pizzaCounter == 0):
        print("and no pizza :(")

def dailyArticleTitle(): 
    print ("\n" + "And the headline from the Michigan Daily:" + "\n")
    print(soup2.select('h2.entry-title')[0].text + "\n")
    #for article in articleTitles:
        #print(article.text)

# def sportsTitle(): 
#     print ("\n" + "And here's the headline from the Michigan Athletics Page:" + "\n")
#     print(soup3.find_all('div.c-stories__title')[0].text)
#     #for article in articleTitles:
#         #print(article.text)


meal = ""
print("What meal do you want?" + '\n')
meal = input("I want the menu for ")
print()
if (meal == "dinner") or (meal == "Dinner") or (meal == "din") or (meal == "Din"):
    printAllDinner(get_pretty_time())
if (meal == "lunch") or (meal == "Lunch"):
    printAllLunch(get_pretty_time())
if (meal == "breakfast") or (meal == "Breakfast") or (meal == "Brek") or (meal == "brek"):
    printAllBreakfast(get_pretty_time())
dailyArticleTitle()
#sportsTitle()