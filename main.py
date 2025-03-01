from contextlib import asynccontextmanager
from fastapi import FastAPI, BackgroundTasks
from apps.docker import StrifeBackend
from apps.pull import pull_strife_backend
from dotenv import load_dotenv

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    StrifeBackend.ensure_started()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "This is the strife infrastructure service"}

@app.get("/webhook/strife-backend/{asset_id}")
async def webhook_strife_backend(asset_id: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(pull_strife_backend, asset_id)
    return {"message": f"Webhook received for Asset ID: {asset_id}"}
