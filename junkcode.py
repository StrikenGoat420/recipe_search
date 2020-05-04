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

#cursor = collection.find({ "ingredients": {"$in": params } }, {"_id" : 0, "ingredients" : 1, "picture_link" : 1})


'''
    for i in range(len(recipes_to_make)):
        all_response.append(json_response)

    for i in range(len(all_response)):
        r_name = recipes_to_make[i]
        picture_link = ""
        for items in all_recipes:
            if items['recipe_name'] == r_name:
                picture_link = items["picture_link"]
        print("after iteration i " +str(i))
        print("\n picture link is " + picture_link)
        print("\n r_name is " +r_name)
        all_response[i]["recipe_name"] = r_name
        all_response[i]["picture_link"] = picture_link
        print("\n values inside dictionary are " )
        for ele in all_response:
            print(ele)
        print()
'''
