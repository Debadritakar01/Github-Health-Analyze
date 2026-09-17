from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "GitHub Health Analyzer API is running"
    }