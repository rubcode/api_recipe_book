from Models.statement import *

def getRecipes():
    query = "SELECT a.name_recipe,a.preparation, b.name_category  FROM recipes a, categories b WHERE a.id_category = b.id_category";
    recipes = selectData(query)
    return recipes

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