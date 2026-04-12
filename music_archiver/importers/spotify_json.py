import json
from typing import List
from music_archiver.core.models import Playlist, Track
from music_archiver.importers.base import BaseImporter


class SpotifyJSONImporter(BaseImporter):
    """
    Importer for Spotify exported playlist JSON files.

    This implementation handles Spotify's real export format where
    tracks are nested under `items` and may include multiple media types.
    """

    def load(self, source: str) -> List[Playlist]:
        with open(source, "r", encoding="utf-8") as f:
            data = json.load(f)

        playlists: List[Playlist] = []

        for p in data.get("playlists", []):
            tracks = []

            for item in p.get("items", []):
                track_data = item.get("track")

                # Skip non-track entries (episodes, local files, etc.)
                if not track_data:
                    continue

                title = track_data.get("trackName")
                artist = track_data.get("artistName")

                # Defensive validation
                if not title or not artist:
                    continue

                tracks.append(Track(title=title, artist=artist))

            playlists.append(
                Playlist(
                    name=p.get("name", "unknown"),
                    tracks=tracks,
                )
            )

        return playlists
