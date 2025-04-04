from Models.statement import *

def getRecipes():
    query = "SELECT a.id_recipe,a.name_recipe,a.preparation, a.url_image, b.name_category  FROM recipes a, categories b WHERE a.category = b.id_category";
    recipes = selectData(query)
    dataRecipes = recipes["data"]
    for recipe in dataRecipes:
        recipe['ingredients'] = getIngredients(recipe['id_recipe'])
        recipe['ingredients'] = recipe['ingredients']['data']
        dataRecipes[dataRecipes.index(recipe)] = recipe
    
    recipes['data'] = dataRecipes
    return recipes

def insertRecipe(nameRecipe,preparation,idCategory,urlImage,status = 1):
    query = "INSERT INTO recipes (name_recipe,preparation,category,url_image,status) VALUES(%s,%s,%s,%s,%s)"
    values = (nameRecipe,preparation,idCategory,urlImage,status)
    response = excuteStatement(query,values)
    if(response['code'] == "000"):
        return {"data": {"code": "000","description": "Receta insertada correctamente","id_recipe": response['id']}}
    return response

def insertCategory(nameCategory,status = 1):
    query  = "INSERT INTO categories (name_category,status) VALUES(%s,%s)"
    values = (nameCategory,status)
    response = excuteStatement(query,values)
    if(response['code'] == "000"):
        return {"code": "000","description": "Categoria insertada correctamente"}
    return response

def getCategories():
    query = "SELECT * FROM categories WHERE status = 1"
    categories = selectData(query)
    return categories

def getIngredients(idRecipe = 0):
    if(idRecipe != 0):
        query = "SELECT * FROM ingredients WHERE id_recipe = %s AND status = 1"
        values = (idRecipe,)
        ingredients = selectData(query,values)
        return ingredients
    query = "SELECT * FROM ingredients WHERE status = 1"
    ingredients = selectData(query)
    return ingredients

def insertIngredient(nameIngredient,idRecipe,status = 1):
    query = "INSERT INTO ingredients (name_ingredient,id_recipe,status) VALUES(%s,%s,%s)"
    values = (nameIngredient,idRecipe,status)
    response = excuteStatement(query,values)
    if(response['code'] == "000"):
        return {"data":{"code": "000","description": "Ingrediente insertado correctamente"}}
    return response