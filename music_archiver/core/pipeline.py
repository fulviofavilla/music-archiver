import logging
from typing import List
from music_archiver.core.models import Playlist
from music_archiver.providers.base import BaseProvider
from music_archiver.storage.filesystem import FileSystemStorage


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


class Pipeline:
    """
    Orchestrates the full flow:
    Import -> Resolve -> Download -> Store
    """

    def __init__(self, provider: BaseProvider, storage: FileSystemStorage):
        self.provider = provider
        self.storage = storage

    def run(self, playlists: List[Playlist], output_dir: str):
        seen = set()

        for playlist in playlists:
            logging.info(f"Processing playlist: {playlist.name}")

            playlist_dir = self.storage.prepare_playlist_dir(output_dir, playlist)
            total = len(playlist.tracks)

            for idx, track in enumerate(playlist.tracks, 1):
                key = f"{track.artist.lower()}::{track.title.lower()}"

                if key in seen:
                    logging.info(f"[{idx}/{total}] Skipping duplicate: {track.artist} - {track.title}")
                    continue

                seen.add(key)

                try:
                    logging.info(f"[{idx}/{total}] Downloading: {track.artist} - {track.title}")

                    result = self.provider.search(track)
                    self.provider.download(track, result, playlist_dir)

                except Exception as e:
                    logging.error(f"Failed: {track.artist} - {track.title} | {e}")
