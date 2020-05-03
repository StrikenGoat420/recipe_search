'''
collection.insert_many([
            {"recipe_name" : "Matar Paneer", "ingredients" : ["Peas", "Tomato", "Cottage Cheese", "Cashew"]},
            {"recipe_name" : "Gajar Halwa", "ingredients" : ["Carrots", "Milk", "Sugar"]},
            {"recipe_name" : "Aloo Baingan", "ingredients" : ["Potato", "Eggplant", "Garam Masala"]},
            {"recipe_name" : "Dal", "ingredients" : ["Lentils", "Water", "tomato"]},
            {"recipe_name" : "Paneer Bharta", "ingredients" : ["Cottage Cheese", "Tomato", "Milk"]}
])
'''

'''
#cursor = collection.find({"ingredients" : {"$all" : ["Cottage Cheese", "Tomato"]}})
#cursor = collection.find({"ingredients" : {"$or" : ["Cottage Cheese", "Milk"]}})
#cursor = collection.find({"$or" : [ "ingredients" : ["Cottage Cheese"], ["Milk"], ["Water"]]})
#cursor = collection.find( { "$or" : [ { "ingredients": { ["Cottage Cheese"] } }, { "ingredients": { ["Milk"] } }, { "ingredients": { ["Water"] } } ] } )
'''

'''
es = Elasticsearch()
doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}
res = es.index(index="test-index", id=1, body=doc)
#print(res['result'])
'''
