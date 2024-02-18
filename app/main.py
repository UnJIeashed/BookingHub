from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
def hello_wolrd():
    return "Hello, World!"


if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)
