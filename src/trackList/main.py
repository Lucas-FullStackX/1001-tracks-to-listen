from fastapi import APIRouter
from src.trackList.utils import get_tracks
from src.constant import DEFAULT_URL

TrackListRouter = APIRouter(
    prefix="/tracks", tags=["Tracks List"]
)


@TrackListRouter.get("/")
def index(url: str = DEFAULT_URL):
    return get_tracks(url)
