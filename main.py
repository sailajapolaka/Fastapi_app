from fastapi import FastAPI
from routers import user

app = FastAPI()

# Include the user router
app.include_router(user.router)

@app.get("/")
def root():
    return {"hello": "world"}
