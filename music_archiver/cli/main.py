import argparse
from music_archiver.importers.spotify_json import SpotifyJSONImporter
from music_archiver.providers.youtube import YouTubeProvider
from music_archiver.storage.filesystem import FileSystemStorage
from music_archiver.core.pipeline import Pipeline


def main():
    parser = argparse.ArgumentParser(description="Music Archiver CLI")

    parser.add_argument("input", help="Path to input file (e.g., Spotify JSON)")
    parser.add_argument("--output", default="output", help="Output directory")
    parser.add_argument("--format", default="mp3", help="Audio format (mp3, m4a, best)")

    args = parser.parse_args()

    importer = SpotifyJSONImporter()
    provider = YouTubeProvider(audio_format=args.format)
    storage = FileSystemStorage()

    playlists = importer.load(args.input)

    pipeline = Pipeline(provider, storage)
    pipeline.run(playlists, args.output)


if __name__ == "__main__":
    main()
