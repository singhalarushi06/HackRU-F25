import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from PIL import Image, ImageDraw

def generate_palette(playlist):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())
    colors = []

    for song in playlist:
        # Extract track ID 
        match = re.search(r'track/([a-zA-Z0-9]+)', song['url'])
        if not match:
            print(f"⚠️ Could not extract track ID from URL: {song['url']}")
            continue
        track_id = match.group(1)

        # Get audio features 
        try:
            features = sp.audio_features([track_id])[0]
            if not features:
                print(f"⚠️ No features found for track ID: {track_id}")
                continue

            valence = features['valence']
            energy = features['energy']

            # mapping logic
            r = int(255 * valence)
            g = int(255 * energy)
            b = int(255 * (1 - valence))
            colors.append((r, g, b))

        except spotipy.exceptions.SpotifyException as e:
            print(f"⚠️ Spotify API error for {track_id}: {e}")
            continue

    for song in playlist:
        features = sp.audio_features(song['url'].split('/')[-1])[0]
        valence = features['valence']
        energy = features['energy']
        # Simple mapping logic
        r = int(255 * valence)
        g = int(255 * energy)
        b = int(255 * (1 - valence))
        colors.append((r, g, b))

    if not colors:
        raise ValueError("No valid audio features retrieved. Cannot generate palette.")

    # Create image
    img = Image.new("RGB", (500, 100))
    draw = ImageDraw.Draw(img)
    step = 500 // len(colors)
    for i, color in enumerate(colors):
        draw.rectangle([i * step, 0, (i+1) * step, 100], fill=color)
    
    return img
