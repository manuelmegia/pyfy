import tkinter as tk
from pygame import mixer
import requests

LASTFM_API_KEY = "your_lastfm_api_key"

def play_pause():
    if mixer.music.get_busy():
        mixer.music.pause()
    else:
        mixer.music.unpause()

def search_song():
    query = search_entry.get()
    url = f"http://ws.audioscrobbler.com/2.0/?method=track.search&track={query}&api_key={LASTFM_API_KEY}&format=json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extract song information from the API response
        track = data["results"]["trackmatches"]["track"][0]
        artist = track["artist"]
        title = track["name"]

        # Display the search results in the song information label
        song_info_label.config(text=f"Search results for: {query}\n{artist} - {title}")

        # Placeholder: Play the first search result (adjust as needed)
        play_selected_song(artist, title)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        # Handle the error, display an error message, or log the issue

def play_selected_song(artist, title):
    try:
        # Replace this with your logic to play the selected song
        # For example, use an appropriate music library or API
        print(f"Playing: {artist} - {title}")

    except Exception as e:
        print(f"Error: {e}")
        # Handle the error, display an error message, or log the issue

# Initialize the mixer module
mixer.init()

# Create the main window
window = tk.Tk()
window.title("Python Spotify Replica")

# Search entry and button
search_entry = tk.Entry(window, width=30)
search_entry.pack(pady=10)

search_button = tk.Button(window, text="Search", command=search_song)
search_button.pack(pady=10)

# Song information display label
song_info_label = tk.Label(window, text="Now Playing: Artist - Song Title")
song_info_label.pack(pady=10)

# Play/Pause button
play_pause_button = tk.Button(window, text="▶️", command=play_pause)
play_pause_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
