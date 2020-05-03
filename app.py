from pymongo import MongoClient
from datetime import datetime
from elasticsearch import Elasticsearch
from flask import Flask, request
import re

mongo_username = 'shubham'
mongo_password = 'MongoUser'
#mongodb connection setup
mongouri = "mongodb+srv://"+mongo_username+":"+mongo_password+"@cluster0-dv5i4.mongodb.net/test?retryWrites=true&w=majority"
client = MongoClient(mongouri)
db = client.Pakalo
collection = db.Recipes

app = Flask(__name__)

@app.route('/ingredients/')
def ingredients():
    arg1 = request.args['arg1']
    params = arg1.split()
    for i in range(len(params)):
        params[i] = params[i].replace('_', ' ')
    #returns me all the document which contains the queried ingredients
    #cursor = collection.find({ "ingredients": {"$in": params } })
    cursor = collection.find({ "ingredients": {"$in": params } }, {"recipe_name" : 1, "_id" : 0, "ingredients" : 1, "picture_link" : 1})

    #all_recipes is a list of dictionary
    all_recipes = list(cursor)
    recipes_to_make = []

    for recipes in all_recipes:
        #total_ingredients is the total number of ingredients required to make the recipe
        total_ingredients = len(recipes["ingredients"])
        #this is the count of ingredients which the user has, to make the recipe
        avail_ingredients = 0
        for items in recipes["ingredients"]:
            if items in params:
                avail_ingredients += 1
        if total_ingredients == avail_ingredients:
            recipes_to_make.append(recipes["recipe_name"])

    json_response = {"recipe_name" : "", "picture_link" : ""}
    all_response = []

    for i in range(len(recipes_to_make)):
        all_response.append(json_response)


    for i in range(len(all_response)):
        all_response[i]['recipe_name'] = recipes_to_make[i]
        print('recipe which was appended is ' +str(recipes_to_make[i]))
        for items in all_recipes:
            if items['recipe_name'] == recipes_to_make[i]:
                all_response[i]["picture_link"] = items["picture_link"]

    for elements in all_response:
        print(elements)


    return 'Try making ' +str(list(recipes_to_make))
