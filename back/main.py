from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from fastapi import FastAPI
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import pandas as pd
import numpy as np
from voronoi import voronoi
from sum import sum1
from typing import Optional







app = FastAPI()

class sql_req(BaseModel):
    city: str = ""
    category: str = ""
    subcategory: str = ""
    name: str = ""
    condition_1: str = ""
    condition_2: str = ""
    condition_3: str = ""

class sql_query(BaseModel):
    query_1: str = ""
    query_2: str = ""
    query_3: str = ""
    query_4: str = ""
    

app.mount("/static", StaticFiles(directory="static"), name="static")

while True:
    try:
        conn = psycopg2.connect(host = 'localhost',
                                database = 'fastapi', 
                                user ='postgres',
                                password = 'zhylekeev7', 
                                cursor_factory= RealDictCursor)
        cursor = conn.cursor()
        print("database connection is establihsed")
        break

    except Exception as error:
        print("Connectng to database failed; error: ", error)
        time.sleep(2)
# cursor.execute("""SELECT * FROM gis_sme_objects""")
# posts =  cursor.fetchall()

dict = {
    '1': 'медицина / здоровье / красота', 
    '2': "автосервис / автотовары", 
    '3': 'продукты питания / напитки',
    '4': 'одежда / обувь', 
    '5': "досуг / развлечения / общественное питание", 
    '6': 'образование / работа / карьера',
    '7': 'юридические / финансовые / бизнес-услуги'
    }

@app.get("/")
def read_html():
    conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user ='postgres', password = 'zhylekeev7', cursor_factory= RealDictCursor)
    cur = conn.cursor()
    cur.execute(f"""select longitude, latitude, 1 value, LEFT(name, 30) name from gis_sme_objects where 1=1 
        and city_name = 'Алматы' 
        and longitude is  not null 
        and longitude !='None' 
        and lower(category) like '%медицина / здоровье / красота%'  
         limit 1000""")
    df = cur.fetchall()
    col_names = [desc[0] for desc in cur.description]

# Create a pandas dataframe from the data and column names
    df = pd.DataFrame(df, columns=col_names)

# Close the cursor and connection
    cur.close()
    conn.close()
       
    print(df.head())
    
    conn.close()

    print("start def vornoi")
    
    voronoi(df)
    with open('static/voronoi_generated.html', 'r', encoding='utf-8') as f:
        html = f.read()

    return HTMLResponse(content=html, status_code=200)


@app.post("/city/")
def root(sql_req: sql_req):
    # value = dict[category] 
    print(sql_req.category)
    conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user ='postgres', password = 'zhylekeev7', cursor_factory= RealDictCursor)
    cur = conn.cursor()
    cur.execute(f"""select longitude, latitude, 1 value, LEFT(name, 30) name from gis_sme_objects where 1=1 
        and lower(category) like '%{sql_req.city}%' 
        and longitude is  not null 
        and longitude !='None' 
        and lower(category) like '%{sql_req.category}%'  
        and lower(subcategory) like '%{sql_req.subcategory}%'  
         limit 1000""")
    df = cur.fetchall()
    col_names = [desc[0] for desc in cur.description]

# Create a pandas dataframe from the data and column names
    df = pd.DataFrame(df, columns=col_names)

# Close the cursor and connection
    cur.close()
    conn.close()
       
    print(df.head())
    
    conn.close()
    

    voronoi(df)
    
    with open('static/voronoi_generated.html', 'r', encoding='utf-8') as f:
        html = f.read()

    return HTMLResponse(content=html, status_code=200)

@app.post("/query/")
def root(sql_query: sql_query):
    # value = dict[category] 
    # print(sql_query.query)
    conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user ='postgres', password = 'zhylekeev7', cursor_factory= RealDictCursor)
    cur = conn.cursor()
    cur.execute(f"""select longitude, latitude, 1 value, LEFT(name, 30) name from gis_sme_objects where 1=1 
        
        {sql_query.query_1}  
        {sql_query.query_2}  
        {sql_query.query_3}  
        {sql_query.query_4}  
         limit 1000""")
    df = cur.fetchall()
    col_names = [desc[0] for desc in cur.description]

# Create a pandas dataframe from the data and column names
    df = pd.DataFrame(df, columns=col_names)

# Close the cursor and connection
    cur.close()
    conn.close()
       
    print(df.head())
    
    conn.close()
    

    voronoi(df)
    
    with open('static/voronoi_generated.html', 'r', encoding='utf-8') as f:
        html = f.read()

    return HTMLResponse(content=html, status_code=200)
