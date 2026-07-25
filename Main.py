from fastapi import FastAPI, status


app= FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/home")    
def home():
    return {"Message":"Welcome to Gaia OS"} 

@app.get("/about")    
def about():
    return {"name":"Gaia OS",
    "version":"0.1",
    "author":"Pranshu Ghosh"}


@app.get("/health",status_code=status.HTTP_200_OK)
def health_check():
    return {"status":"ok"}