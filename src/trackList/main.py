from fastapi import APIRouter
from src.trackList.utils import get_tracks


TrackListRouter = APIRouter(
    prefix="/tracks", tags=["Tracks List"]
)


@TrackListRouter.get("/")
def index():
    return get_tracks()
