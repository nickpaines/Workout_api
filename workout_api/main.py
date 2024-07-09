from fastapi import FastAPI
from workout_api.routers import api_router

app = FastAPI(title="WorKoutApi")
app.include_router(api_router)

