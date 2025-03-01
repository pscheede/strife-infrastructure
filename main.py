from contextlib import asynccontextmanager
from dotenv.main import dotenv_values
from fastapi import FastAPI, BackgroundTasks
from apps.docker import StrifeBackend
from apps.pull import pull_strife_backend
from dotenv import load_dotenv

load_dotenv()
config = dotenv_values(".env")
print(config)

@asynccontextmanager
async def lifespan(app: FastAPI):
    StrifeBackend.ensure_started()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/ping")
async def ping():
    return {"message": "Pong"}

@app.get("/webhook/strife-backend/{asset_id}")
async def webhook_strife_backend(asset_id: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(pull_strife_backend, asset_id)
    return {"message": f"Webhook received for Asset ID: {asset_id}"}
