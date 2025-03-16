from .connection import *

def excuteStatement(query,values):
    dbCon = connect()
    mycursor = dbCon.cursor()
    query = query
    mycursor.execute(query, values)
    dbCon.commit()
    return {"code":"000","description": "Se ejecuto query correctamente"}

def selectData(query):
    dbCon = connect()
    myCursor = dbCon.cursor()
    myCursor.execute(query)
    column_names = [i[0] for i in myCursor.description]
    data = myCursor.fetchall()
    result = [dict(zip(column_names, row)) for row in data]
    response = {
            "code": "000",
            "description": "Se extrayeron correctamente los datos",
            "data": result
    }
    return response 