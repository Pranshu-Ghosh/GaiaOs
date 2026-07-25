from fastapi import FastAPI, status
from mockdata import users


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


@app.get("/users")
def get_users():
    return users 

@app.get("/users/{id}")
def get_user(id:int):
    if id>len(users) or id<=0:
        return {"message":"user not found"}
    for user in users:
        if user["id"]==id:
            return user
   

@app.post("/create_user")
def create_user(name:str,email:str):
    users.append({"id":len(users)+1,"name":name,"email":email})
    return users









@app.get("/health",status_code=status.HTTP_200_OK)
def health_check():
    return {"status":"ok"}