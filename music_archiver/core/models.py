from dataclasses import dataclass
from typing import List


@dataclass
class Track:
    """
    Represents a normalized track across any provider.
    """
    title: str
    artist: str


@dataclass
class Playlist:
    """
    Represents a normalized playlist containing tracks.
    """
    name: str
    tracks: List[Track]
