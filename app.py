import streamlit as st

from playlist_generator import generate_playlist
from color_palette import generate_palette

st.set_page_config(page_title="Moodify", page_icon="🎧", layout="centered")
st.title("Moodify: Immerse Yourself in Music")

def main():
    mood = st.text_input("Enter your mood (e.g., chill evening, study grind):")

    if st.button("Generate Playlist & Palette"):
        playlist = generate_playlist(mood)
        palette = generate_palette(playlist)
        
        st.subheader("🎧 Your Playlist")
        for song in playlist:
            st.markdown(f"**{song['name']}** — {song['artist']}  \n[Open in Spotify]({song['url']})")

        st.subheader("🎨 Mood Palette")
        st.image(palette, caption="Generated from your playlist")

        # give option to save playlist to Spotify
        if st.button("Save Playlist to Spotify"):
            st.info("Feature coming soon!")
            
if __name__ == "__main__":
    main()
