# main.py

import os
import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from templates import HTML_CONTROLLER, HTML_DASHBOARD

app = FastAPI()

@app.get("/")
async def get_dashboard():
    return HTMLResponse(content=HTML_DASHBOARD)

@app.get("/phone")
async def get_phone():
    return HTMLResponse(content=HTML_CONTROLLER)

connected_clients = set()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for client in connected_clients:
                if client != websocket:
                    await client.send_text(data)
    except Exception as e:
        pass
    finally:
        try:
            connected_clients.remove(websocket)
        except:
            pass

if __name__ == "__main__":
    # Render немесе Railway беретін динамикалық ПОРТ-ты автоматты түрде ұстау
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
