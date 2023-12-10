from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from controllers import routes

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