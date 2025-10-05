import os
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()  # this reads .env automatically

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id = os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
))

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
