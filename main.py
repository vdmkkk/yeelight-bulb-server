from fastapi import FastAPI
from yeelight import *
from typing import Literal
from pydantic import BaseModel

app = FastAPI()
# bulb = Bulb('192.168.1.138')
#
# Effect = Literal["smooth", "sudden"]
#
#
# class TurnOnRequest(BaseModel):
#     effect: Effect
#
#
# class SetRgbRequest(BaseModel):
#     red: int
#     green: int
#     blue: int
#     effect: Effect
#
#
# @app.get("/status")
# async def status():
#     global bulb
#     try:
#         status = bulb.get_properties()
#     except:
#         bulb = Bulb('192.168.1.138')
#         print('i got an error but i will keep going')
#     return {'message': status}
#
#
# @app.post("/turn_on")
# async def turn_on(request: TurnOnRequest):
#     effect = request.effect
#     print(effect)
#     try:
#         bulb.turn_on(effect=effect)
#     except Exception:
#         pass
#     return {"message": f"Bulb turned on with effect: {effect}"}
#
#
# @app.post("/turn_off")
# async def turn_on():  # Expecting request body
#     try:
#         bulb.turn_off()
#     except Exception:
#         pass
#     return {"message": f"Bulb turned off"}
#
#
# @app.post("/set_rgb")
# async def set_rgb(request: SetRgbRequest):
#     red, green, blue, effect = request.red, request.green, request.blue, request.effect
#     try:
#         bulb.set_rgb(red, green, blue, effect=effect)
#     except Exception:
#         pass
#     return {"message": f"Bulb changed color to {red} {green} {blue}"}


coords = [[55.734488, 37.605805], [55.781189, 37.595551], [55.749999, 37.594829], [55.708759, 37.706815],
          [55.687765, 37.528482], [55.798520, 37.602290], [55.768811, 37.698641], [55.785615, 37.465945]]

origins=[
    'http://localhost',
    'http://localhost:8000',
    'http://localhost:3000',
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=true,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/get_geo')
async def get_geo():
    return coords
