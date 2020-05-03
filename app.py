from pymongo import MongoClient
from datetime import datetime
from elasticsearch import Elasticsearch
from flask import Flask, request
import re

#mongodb connection setup
mongouri = "mongodb+srv://shubham:MongoUser@cluster0-dv5i4.mongodb.net/test?retryWrites=true&w=majority"
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
    cursor = collection.find({ "ingredients": {"$in": params } })

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


    return 'Try making ' +str(list(recipes_to_make))
