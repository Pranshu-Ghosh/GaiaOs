from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/home")    
def home():
    return "Welcome to Gaia OS " 