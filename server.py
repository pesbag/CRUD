from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import requests
import main
from main import shape_manager

shape_manage=shape_manager.ShapeManager()

app=FastAPI()
@app.get("/shapes")
def return_all_shapes():
    return shape_manage.get_all_shapes()
@app.get("/shapes/{id}")
def return_shape_by_id(id:int):
    shape=shape_manage.get_shape_by_id(id)
    if not shape:
        raise HTTPException(status_code=404,detail="Shape id was not found")
    return shape

class Item(BaseModel):
    shape_id: int
    shape_description: str | None = None
    side_length: int
    area: int | None = None
    preimeter: int

@app.delete("/shapes/{id}")
def delete_shape(id:int):
    deleted=shape_manage.delete_shape(id)
    if not deleted:
        raise HTTPException(status_code=404,detail="Shape id was not found")
    return deleted

@app.post("/shapes")
def create_new_shape(data: dict):
    result=shape_manage.create_shape_1(data)
    return result
@app.put("/shapes/{id}")
def change_params(id:int,data:dict):
    return shape_manage.update_shape(id,data)
@app.get("/shapes/total-area")
def sum_of_all_area_shapes():
    pass