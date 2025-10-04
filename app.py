import streamlit as st

from playlist_generator import generate_playlist
from color_palette import generate_palette

st.title("Moodify: Immerse Yourself in Music")

def main():
    mood = st.text_input("Enter your mood (e.g., chill evening, study grind):")

    if st.button("Generate Playlist & Palette"):
        playlist = generate_playlist(mood)
        palette = generate_palette(playlist)
        
        st.subheader("🎧 Your Playlist")
        for song in playlist:
            st.write(f"{song['name']} by {song['artist']}")
        
        st.subheader("🎨 Mood Palette")
        st.image(palette)

        # give option to save playlist to Spotify
        if st.button("Save Playlist to Spotify"):
            st.info("Feature coming soon!")
            # Uncomment and implement the following code to enable Spotify saving functionality
            """
            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                client_id='YOUR_CLIENT_ID',
                client_secret='YOUR_CLIENT_SECRET',
                redirect_uri='YOUR_REDIRECT_URI',
                scope='playlist-modify-public'
            ))
            user_id = sp.current_user()['id']
            playlist_name = f"Moodify: {mood}"
            new_playlist = sp.user_playlist_create(user_id, playlist_name)
            track_uris = [song['uri'] for song in playlist]
            sp.playlist_add_items(new_playlist['id'], track_uris)
            st.success(f"Playlist '{playlist_name}' saved to your Spotify account!")
            """
