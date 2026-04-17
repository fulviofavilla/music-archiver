import logging
import subprocess
from music_archiver.providers.base import BaseProvider
from music_archiver.core.models import Track
from music_archiver.utils.sanitize import sanitize


class YouTubeProvider(BaseProvider):
    """
    YouTube provider implementation using yt-dlp.

    Relies on yt-dlp being installed and available in PATH.
    Install with: pip install yt-dlp
    """

    def __init__(self, audio_format: str = "mp3"):
        self.audio_format = audio_format

    def search(self, track: Track) -> str:
        return f"ytsearch1:{track.artist} - {track.title} official audio"

    def download(self, track: Track, query: str, output_dir: str) -> None:
        safe_artist = sanitize(track.artist)
        safe_title = sanitize(track.title)

        filename = f"{safe_artist} - {safe_title}.%(ext)s"
        output_template = f"{output_dir}/{filename}"

        cmd = [
            "yt-dlp",
            "-f", "bestaudio",
            "-x",
            "--no-post-overwrites",
            "--embed-metadata",
            "--embed-thumbnail",
            "--no-keep-video",
        ]

        if self.audio_format != "best":
            cmd += ["--audio-format", self.audio_format]

        cmd += ["-o", output_template, query]

        result = subprocess.run(cmd, check=False)

        if result.returncode != 0:
            logging.warning(
                f"yt-dlp exited with code {result.returncode} "
                f"for: {track.artist} - {track.title}"
            )
