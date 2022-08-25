##### PYTHON POSTGRES FASTAPI

#### Virtual Environment setup

> python -m venv env

---

### Activate the virtual environment

> source env/Scripts/activate

#### Install project dependencies

> pip install fastapi uvicorn

---

#### Create fastapi server

<!-- In main.py -->

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"message":"world"}
```

---

#### Running the server

We need an asynchronous [ASGI] server called `uvicorn`

> pip install uvicorn

To run use: uvicorn main:app --reload
main is referring main.py file
app is referring to the FASTAPI instance

---

#### Creating routes

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# schema
class Item(BaseModel): #serializer
    id:int
    name:str
    description:str
    price:int
    on_offer:bool


@app.get("/")
async def index():
    return {"message":"world"}


@app.get("/greet/{name}")
async def greet_name(name:str): # type inference
    return f"hello {name}!"

# Query string http://localhost:8000?name=user
@app.get("/greet/")
def greet_optional_name(name:Optional[str]="user"):
    return {"message":f"hello {name}!"}


# {
#   "id": 1,
#   "name": "milk",
#   "on_offer": false,
#   "description": "nice milk",
#   "price": 7878
# }
@app.put("/item/{item_id}")
async def update_item(item_id:int,item:Item):
    return {
        "name":item.name,
        "description":item.description,
        "price":item.price,
        "on_offer":item.on_offer
        }
```

---

#### Connecting to Database

Install sqlalchemy and postgres driver

> pip install sqlalchemy
> pip install psycopg2-binary --> postgres binary

---

Then create a database for the application using the terminal connection

> psql -U postgres
> CREATE DATABASE [database name]

---

#### Migrate the db

> python create_db.py
