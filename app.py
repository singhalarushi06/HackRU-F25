import streamlit as st

from playlist_generator import generate_playlist
from color_palette import generate_palette

#import spotipy
#from spotipy.oauth2 import SpotifyOAuth

st.title("Moodify: Immerse Yourself in Music")

def main():
    input = get_user_input()

    # add a carousel to show the playlist
    # build playlist in playlist_generator.py
    playlist = generate_playlist(input)
    st.write("Generated Playlist:")
    st.write(playlist)

    # add a carousel to show the color palette
    # build playlist in color_palette.py
    colors = generate_palette(playlist)
    st.write("Asspciated Colors:")
    st.write(colors)
    st.image(colors, width=100)
    


def get_user_input():
    return input("How are you feeling today? ")



"""
def main():
    # Spotify API authenticatio
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id="your_client_id",
        client_secret="your_client_secret",
        redirect_uri="http://localhost:8888/callback",
        scope="playlist-modify-public"
    ))

    # Get user input
    user_input = get_user_input()

    # Generate playlist
    
    # Generate color palette
    


def generate_playlist(sp, user_input):
    # Generate a playlist based on user input using Spotify API.
    # Placeholder for playlist generation logic
    print(f"Generating playlist for you! ")
    # Example: Search for tracks or create a playlist
    results = sp.search(q=user_input, type='track', limit=10)
    tracks = [track['name'] for track in results['tracks']['items']]
    return tracks

def generate_color_palette(playlist):
    # Generate a color palette based on the playlist.
    # Placeholder for color palette generation logic
    print(f"Generating color palette for playlist: {playlist}")
    # Example: Map songs to colors (this is just a stub)
    return ["#FF5733", "#33FF57", "#3357FF"]

"""