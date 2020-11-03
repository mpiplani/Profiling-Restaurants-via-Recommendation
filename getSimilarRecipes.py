import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import copy
import pickle as pkl
import itertools
from difflib import SequenceMatcher
from difflib import get_close_matches
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
# def getMaxMatch(nameList,inputList):
#     max_prob = 0
#
#     similar_sentence_index = -1
#     length = len(inputList)
#     for i in nameList:
#         print(i)
#         similar_sentence = None
#         for j in range(len(inputList)):
#             match_ratio = SequenceMatcher(None, i.lower(), inputList[j].lower(),autojunk=False).ratio()
#             if match_ratio > max_prob:
#                 max_prob = match_ratio
#                 similar_sentence = inputList[j]
#                 similar_sentence_index = j
#         if similar_sentence is not None:
#             print("******************")
#             print(similar_sentence)
#             print("This is similiar to original sentence ")
#             print("******************** \n")


# def getMaxMatch(nameList,inputList):
#     max_prob = 0
#
#     similar_sentence_index = -1
#     length = len(inputList)
#     for i in nameList:
#         print(i)
#         similar_sentence = None
#         for j in range(len(inputList)):
#             match_ratio = fuzz.token_sort_ratio( i, inputList[j])
#             if match_ratio > max_prob:
#                 max_prob = match_ratio
#                 similar_sentence = inputList[j]
#                 similar_sentence_index = j
#         if similar_sentence is not None:
#             print("******************")
#             print(similar_sentence)
#             print("This is similiar to original sentence ")
#             print("******************** \n")

def getMaxMatch(nameList,inputList):
    max_prob = 0

    similar_sentence_index = -1
    length = len(inputList)
    for i in nameList:
        print(i)
        similar_sentence = None
        similar_sentence = process.extractOne(i,inputList,scorer=fuzz.partial_token_sort_ratio)

        if similar_sentence is not None:
            print("******************")
            print(similar_sentence)
            print("This is similiar to original sentence ")
            print("******************** \n")



recipes_RAW = pd.read_csv("RAW_recipes.csv")
recipes_RAW = recipes_RAW.rename({"id": "recipe_id"}, axis=1)

recipes_RAW_name = recipes_RAW["name"]

recipes_RAW_ingredients = recipes_RAW["ingredients"]
finalProcessedIngredients = []
for i in recipes_RAW_ingredients:
    s = set(i)
    finalProcessedIngredients.append(s)

# for i in range(2):
#     print(recipes_RAW_name[i], " ingredients are ", recipes_RAW_ingredients[i])

mehakOutput = [['Burgers, Mocktails, Pasta, Cocktails, Beef Steak, Lunch Buffet, Chicken Steak'], ['Kamikaze, Long Island Iced Tea, Pizza, Hefeweizen, Cocktails, Belgian Brew Beer, Chicken Bbq Wings'], ['English Breakfast, Burgers, Sandwiches, Chicken Burger, Pasta, Veg Burger, Chicken Sausages'], ['English Breakfast, French Fries, Burgers, Pancakes, Corn Sandwich, Chicken Burger, Bacon Fry'], ['Masala Fries, Cocktails, Chicken Wings, Beer, Onion Rings, Pizza, Nachos'], ['Beer, Cocktails, Tiramisu, Tawa Chicken, Mocktails, Chicken Satay, Sea Food'], ['Pizza, Cheesecake, Burgers, Pasta, Waffles, Veg Burger, Chocolate Cake'], ['Pizza, Beef Chilli, Craft Beer, Apple Crumble, Pork Chilli, Chips, Wheat Beer'], ['Burgers, Sandwiches, Peanut Butter Smoothie, Margherita Pizza, Ravioli, Cocktails, Hot Chocolate'], ['Burgers, Sandwiches, Peanut Butter Smoothie, Margherita Pizza, Ravioli, Cocktails, Salad']]



mehakOutputTokens = []

for i in range(len(mehakOutput)):
    a = mehakOutput[i][0].split(', ')
    mehakOutputTokens = mehakOutputTokens + a

print(mehakOutputTokens)

recipes_RAW_name = [str(i) for i in recipes_RAW_name]
getMaxMatch(mehakOutputTokens,recipes_RAW_name)
