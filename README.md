# Music Archiver

A CLI tool to archive your Spotify playlists as local audio files. Built for personal use after deleting a Spotify account — reads your exported playlist data and downloads each track from YouTube via `yt-dlp`.

## How It Works

```
Spotify JSON export → parse tracks → search YouTube → download audio → organize by playlist
```

The pipeline deduplicates tracks across playlists and organizes downloads into folders named after each playlist.

## Getting Started

**Prerequisites:**

- Python 3.10+
- `yt-dlp` installed and available in PATH (`pip install yt-dlp`)
- `ffmpeg` installed (required by `yt-dlp` for audio conversion)

**Install:**

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools
pip install -e .
```

**Export your Spotify data:**

Go to Spotify → Account → Privacy Settings → Download your data. You'll receive a ZIP containing `Playlist1.json` (and others) with your playlist and track information.

**Run:**

```bash
music-archiver path/to/your/playlist.json
music-archiver path/to/your/playlist.json --output ~/Music --format m4a
```

Available formats: `mp3` (default), `m4a`, `best`.

## Project Structure

```
music_archiver/
├── cli/            # Argument parsing and entry point
├── core/           # Domain models (Track, Playlist) and pipeline orchestration
├── importers/      # Converts external formats into normalized Playlist objects
├── providers/      # Resolves and downloads tracks (YouTube via yt-dlp)
├── storage/        # Filesystem organization
└── utils/          # Shared utilities (filename sanitization)
```

The importer/provider architecture makes it straightforward to add new sources — a `LastFMImporter`, a `SoundCloudProvider`, or a CSV importer would each slot in without touching the core pipeline.

## Disclaimer

This tool is intended for personal archiving of music you have legitimate access to. Users are responsible for ensuring their use complies with applicable copyright laws and the terms of service of the platforms involved. The author does not condone copyright infringement.

## License

MIT
