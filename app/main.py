from fastapi import FastAPI, Response
from starlette.websockets import WebSocket
from fastapi.middleware.cors import CORSMiddleware
from controllers import routes
from services import services
import time
import asyncio
import json

app = FastAPI()

# Define CORS middleware options
origins = ["*"]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)

@app.websocket("/realtime")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = services.get_realtime_data()
            await websocket.send_text(json.dumps(data))  # Converta os dados para JSON antes de enviá-los
            await asyncio.sleep(1)  # Adicione um atraso para evitar sobrecarga
    except RuntimeError:
        pass
    finally:
        await websocket.close()


# @app.get("/realtime/data")
# async def get_realtime_data():
#     time.sleep(5)  # Simula um atraso na resposta
#     return services.get_realtime_data()