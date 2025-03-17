from Models.recipe import *

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
]

class Category(BaseModel):
    nameCategory: str
    status: int

class Recipe(BaseModel):
    nameRecipe: str
    preparation: str
    idCategory: int
    status: int

class Ingredient(BaseModel):
    nameIngredient: str
    idRecipe: int
    status: int

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

@app.get("/")
def welcome():
    return {"message":"Bienvenido a la API de recetas de Rub"}

@app.get("/recipes")
def getRecipesData():
    response = getRecipes()
    return response

@app.post("/recipes")
def addRecipe(recipe: Recipe):
    response = insertRecipe(recipe.nameRecipe,recipe.preparation,recipe.idCategory)
    return response

@app.get("/categories")
def getCategoriesData():
    response = getCategories()
    return response

@app.post("/categories")
def addCategory(category: Category):
    response = insertCategory(category.nameCategory,category.status)
    return response

@app.get("/ingredients")
def getIngredientsData():
    response = getIngredients()
    return response

@app.post("/ingredients")
def addIngredient(ingredient: Ingredient):
    response = insertIngredient(ingredient.nameIngredient,ingredient.idRecipe)
    return response