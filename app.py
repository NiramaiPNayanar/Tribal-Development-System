import pprint
from http.client import HTTPException

from fastapi import FastAPI
from main import tribal_memb, health_data, counsil_memb, business_data, locality_data, community_data, admin_data
from pydantic import BaseModel
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from uvicorn import run

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)


@app.get("/updatememb")
def updatememb(m_id: int, name: str):
    tribal_memb.update_one({"member_id": m_id}, {"$set": {"member_name": name}})

@app.get("/deletememb")
def deletememb(m_id: int):
    tribal_memb.delete_one({"member_id":m_id})



# @app.get("/search")
# def find_tribal(name: str):
#     results = list(tribal_memb.find({"name": name}))
#     return [TribalMemb(**result) for result in results]

@app.get("/")
async def hello():
    return "Hello"


@app.get("/statename")
def getstate():
    data = list(locality_data.find({}, {"_id": False, "state": True}))
    return data



def search_name(name: str):
    datas = list(tribal_memb.find({"member_name": name}, {"_id": False}))
    return datas


@app.get('/getbusiness')
def bus_data():
    data = list(locality_data.find({}, {"_id": False, "state": True}))
    return data






@app.get('/addmember')
def add(id: int, name: str, edst: str, age: int, dob: str, cid: int, lid: int):
    tribal_memb.insert_one({"member_id": id,
                            "member_name": name,
                            "educational_status": edst,
                            "age": age,
                            "dob": dob,

                            "community_id": cid,
                            "locality_id": lid})

    return JSONResponse(content={"success": True})





@app.get("/showall")
async def show():
    result_1 = list(health_data.find({}, {"_id": 0}))
    result_2 = list(counsil_memb.find({}, {"_id": 0}))
    result_3 = list(business_data.find({}, {"_id": 0}))
    result_4 = list(locality_data.find({}, {"_id": 0}))
    result_5 = list(community_data.find({}, {"_id": 0}))
    result_6 = list(tribal_memb.find({}, {"_id": 0}))
    response_data = {
        "result_1": result_1,
        "result_2": result_2,
        "result_3": result_3,
        "result_4": result_4,
        "result_5": result_5,
        "result_6": result_6,
    }

    return JSONResponse(content=response_data)


if __name__ == "__main__":
    run(app, host="127.0.0.1", port=8000)

# [[Health(**result) for result in result_1], [CounsilMemb(**result) for result in result_2], [
#         BusinessData(**result) for result in result_3], [LocalityData(**result) for result in result_4], [
#         CommunityData(**result) for result in result_5], [TribalMemb(**result) for result in result_6]]
