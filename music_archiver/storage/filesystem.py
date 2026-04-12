import os
from music_archiver.core.models import Playlist
from music_archiver.utils.sanitize import sanitize


class FileSystemStorage:
    """
    Handles filesystem organization for playlists and tracks.
    """

    def prepare_playlist_dir(self, base_path: str, playlist: Playlist) -> str:
        safe_name = sanitize(playlist.name)
        path = os.path.join(base_path, safe_name)

        os.makedirs(path, exist_ok=True)
        return path
