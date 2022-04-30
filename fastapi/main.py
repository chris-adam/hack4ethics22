from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run("main:app",  host="0.0.0.0", port=80, reload=True, debug=False)