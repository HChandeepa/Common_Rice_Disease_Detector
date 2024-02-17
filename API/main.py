from fastapi import FastAPI
import uvicorn
app=FastAPI()

@app.get("/ping")
async def ping():
    return "Hello,I am alive"

@app.post("/ping")
async def ping():

if __name__=="__main__":
    uvicorn.run(app,host='localhost',port=8000)