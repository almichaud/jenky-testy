from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hewwo World, and also I'm an avid consumer of big buts and I can not lie"}

