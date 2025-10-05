import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from PIL import Image, ImageDraw

def generate_palette(playlist):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())
    colors = []
    for song in playlist:
        features = sp.audio_features(song['url'].split('/')[-1])[0]
        valence = features['valence']
        energy = features['energy']
        # Simple mapping logic
        r = int(255 * valence)
        g = int(255 * energy)
        b = int(255 * (1 - valence))
        colors.append((r, g, b))
    # Create image
    img = Image.new("RGB", (500, 100))
    draw = ImageDraw.Draw(img)
    step = 500 // len(colors)
    for i, color in enumerate(colors):
        draw.rectangle([i * step, 0, (i+1) * step, 100], fill=color)
    return img
