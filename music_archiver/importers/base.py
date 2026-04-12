from abc import ABC, abstractmethod
from typing import List
from music_archiver.core.models import Playlist


class BaseImporter(ABC):
    """
    Base interface for all importers.

    Importers are responsible for converting external data formats
    (e.g., Spotify JSON, CSV, etc.) into normalized Playlist objects.
    """

    @abstractmethod
    def load(self, source: str) -> List[Playlist]:
        pass
