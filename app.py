from pymongo import MongoClient
from datetime import datetime
from elasticsearch import Elasticsearch
from flask import Flask, request, jsonify
import re

#append to url
#/ingredients/?arg1=Lentils+Water+Tomato+Cottage_Cheese+Milk
#/recipe/Dal

mongo_username = 'add_username_here'
mongo_password = 'add_password_here'
#mongodb connection setup
mongouri = "mongodb+srv://"+mongo_username+":"+mongo_password+"@cluster0-dv5i4.mongodb.net/test?retryWrites=true&w=majority"
client = MongoClient(mongouri)
db = client.Pakalo
collection = db.Recipes

app = Flask(__name__)

@app.route('/ingredients/')
def suggest_recipes():
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

    #json_response = {"recipe_name" : "", "picture_link" : ""}
    all_response = {}

    for i in range(len(recipes_to_make)):
        r_name = recipes_to_make[i]
        picture_link = ""
        for items in all_recipes:
            if items['recipe_name'] == r_name:
                picture_link = items["picture_link"]
        json_response_value = {"recipe_name" : r_name, "picture_link" : picture_link}
        all_response[i] = json_response_value

    json_response = jsonify(all_response)

    return json_response

@app.route('/recipe/<recipe_name>')
def get_recipeInfo (recipe_name):
    recipe_name = recipe_name.replace('_', ' ')
    cursor = collection.find({ "recipe_name": recipe_name}, {"_id" : 0})
    resp = list(cursor)
    return jsonify(resp)
