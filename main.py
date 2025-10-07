from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def root():
    print("Endpoint called")
    return "Timeweb Cloud + FastAPI = ❤️"
