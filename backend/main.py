from fastapi import FastAPI, Request
from calendar_utils import book_event

app = FastAPI()

@app.post("/book")
async def book(request: Request):
    data = await request.json()
    response = book_event(data['summary'], data['start'], data['end'])
    return {"message": response}
