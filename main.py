from fastapi import FastAPI
from yeelight import *
from typing import Literal
from pydantic import BaseModel

app = FastAPI()
bulb = Bulb('192.168.1.138')

Effect = Literal["smooth", "sudden"]

class TurnOnRequest(BaseModel):
    effect: Effect

class SetRgbRequest(BaseModel):
    red: int
    green: int
    blue: int
    effect: Effect


@app.get("/status")
async def status():
    global bulb
    try:
        status = bulb.get_properties()
    except:
        bulb = Bulb('192.168.1.138')
        print('i got an error but i will keep going')
    return {'message': status}



@app.post("/turn_on")
async def turn_on(request: TurnOnRequest):
    effect = request.effect
    print(effect)
    try:
        bulb.turn_on(effect=effect)
    except Exception:
        pass
    return {"message": f"Bulb turned on with effect: {effect}"}

@app.post("/turn_off")
async def turn_on():  # Expecting request body
    try:
        bulb.turn_off()
    except Exception:
        pass
    return {"message": f"Bulb turned off"}

@app.post("/set_rgb")
async def set_rgb(request: SetRgbRequest):
    red, green, blue, effect = request.red,request.green,request.blue,request.effect
    try:
        bulb.set_rgb(red, green, blue, effect=effect)
    except Exception:
        pass
    return {"message": f"Bulb changed color to {red} {green} {blue}"}