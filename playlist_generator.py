import os
import re
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()  # this reads .env automatically

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id = os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    )
)

def generate_playlist(mood):
    results = sp.search(q=mood, type='track', limit=10)
    playlist = []
    for track in results['tracks']['items']:
        playlist.append({
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'url': track['external_urls']['spotify']
        })
    return playlist

def get_audio_features(song_url):
    # Extracts the Spotify track ID from a track URL
    
    match = re.search(r'track/([a-zA-Z0-9]+)', song_url)
    if not match:
        print(f"⚠️ Could not extract track ID from URL: {song_url}")
        return None

    track_id = match.group(1)

    # Fetch audio features
    try:
        features = sp.audio_features([track_id])[0]
        return features
    except spotipy.exceptions.SpotifyException as e:
        print(f"⚠️ Spotify API error for {track_id}: {e}")
        return None
