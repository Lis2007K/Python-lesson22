from fastapi import FastAPI

app = FastAPI()

@app.get('/items')
def read_items():
    return{"items":["item1", "item2", "item3"]}

@app.post('/items/')
def create_item(name: str, price:float):
    return {"item_name":name, "itemprice": price}

@app.put('/items/{item_id}')
def update_post(item_id:int, name: str, price:float):
    return{"item_id":item_id,"item_name":name, "itemprice": price}

@app.delete('/items/{item_id}')
def delete_post(item_id:int, name: str, price:float):
    return{"Message":f"Item{item_id} has been deleted"}