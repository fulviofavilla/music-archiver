from abc import ABC, abstractmethod
from music_archiver.core.models import Track


class BaseProvider(ABC):
    """
    Providers are responsible for resolving and downloading tracks
    from external services (e.g., YouTube, SoundCloud).
    """

    @abstractmethod
    def search(self, track: Track) -> str:
        """Return a provider-specific search query for a track."""
        pass

    @abstractmethod
    def download(self, track: Track, query: str, output_dir: str) -> None:
        """Download the resolved track into the output directory."""
        pass
