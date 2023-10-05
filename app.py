from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.websockets import WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from sqlmodel import SQLModel

class LLM(BaseModel):
    prompt: str
    max_length: int = 64
    temperature: float = 0.5
    top_k: int = 5
    top_p: float = 0.95
    repetition_penalty: float = 1.2
    presence_penalty: float = 0.6
    num_return_sequences: int = 1
    pad_token_id: int = 0
    bos_token_id: int = 1
    eos_token_id: int = 2
    unk_token_id: int = 3
    mask_token_id: int = 4
    cls_token_id: int = 5
    sep_token_id: int = 6
    pad_token_label: str = "<pad>"

app = FastAPI()

@app.get("/")
async def root():
    return JSONResponse({"message": "Hello World"}, 200)

@app.post("/")
async def insert(data: LLM):
    return JSONResponse(data.__dict__, status_code=201)

@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    while True:
        try:
            message = await websocket.receive_json()
            print(message)
            await websocket.send_text(message)
        except WebSocketDisconnect:
            pass

# http://127.0.0.1:8000/
# ws://127.0.0.1:8000/