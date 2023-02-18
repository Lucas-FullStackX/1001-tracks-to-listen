from fastapi import FastAPI
from src.trackList.main import TrackListRouter
# Run API:
# uvicorn main:app
app = FastAPI()

# Add Routers
app.include_router(TrackListRouter)
