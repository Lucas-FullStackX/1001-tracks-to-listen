from fastapi import FastAPI
from src.trackList.main import TrackListRouter
# Run API:
# uvicorn main:app --reload
app = FastAPI()

# Add Routers
app.include_router(TrackListRouter)
