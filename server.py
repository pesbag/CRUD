from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import requests
import main
import json
import logging

logger=logging.getLogger('shape')
from main import shape_manager

shape_manage=shape_manager.ShapeManager()

app=FastAPI()

@app.get("/shapes")
def return_all_shapes():
    logger.info("enter to return_all_shapes in web server")
    result=shape_manage.get_all_shapes()
    if not result:
        logger.exception("Errror ")
        raise HTTPException(status_code=404, detail="Shape id was not found")
    return result

@app.get("/shapes/total-area")
def sum_of_all_area_shapes():
    result= shape_manage.get_sum_of_all_area()
    if not result:
        raise HTTPException(status_code=404, detail="There is not shapes to calculate area")
    return result

@app.get("/shapes/{id}")
def return_shape_by_id(id:int):
    shape=shape_manage.get_shape_by_id(id)
    if not shape:
        raise HTTPException(status_code=404,detail="Shape id was not found")
    return shape

# class Item(BaseModel):
#     shape_id: int
#     shape_type: str | None = None
#     side_length: int
#     area: int | None = None
#     preimeter: int | None = None

@app.delete("/shapes/{id}")
def delete_shape(id:int):
    deleted=shape_manage.delete_shape(id)
    if not deleted:
        raise HTTPException(status_code=404,detail="Shape id was not found")
    return deleted

@app.post("/shapes")
async def create_new_shape(data: dict):
    result=shape_manage.create_shape_1(data)
    if not result:
        raise HTTPException(status_code=400, detail="Faild to create a new shape")
    return result

@app.put("/shapes/{id}")
def change_params(id:int,data:dict):
     result=shape_manage.update_shape(id,data)
     if not result:
         raise HTTPException(status_code=404, detail="Shape id was not found")
     return {'message': "updated successfully"}


