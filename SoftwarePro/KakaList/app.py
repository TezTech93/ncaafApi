from fastapi import FastAPI
import sys, os
sys.path.append(os.path.dirname((__file__)) + "/")
from databases import *

app = FastAPI()

@app.get("/kakalist/jobs/{location}")
def get_post(location):
    result = getJobs(location)
    return {"Data":result}

@app.post("kakalist/post")
def make_post(postClient,datetime,content,location):
    postJobs(postClient,datetime,content,location)
    return "Successful"

@app.get("/kakalist/services/{location}")
def get_post(location):
    getServices(location)
    return {"Data":"Set"}

@app.post("kakalist/services")
def make_post(postClient,datetime,content,location):
    postJobs(postClient,datetime,content,location)
    return "Successful"

@app.get("/kakalist/events/{location}")
def get_post(location):
    getEvents(location)
    return {"Data":"Set"}

@app.post("kakalist/events")
def make_post(postClient,datetime,content,location):
    postJobs(postClient,datetime,content,location)
    return "Successful"
