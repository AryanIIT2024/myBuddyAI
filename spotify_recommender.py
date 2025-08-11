import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Replace these with your actual credentials
SPOTIPY_CLIENT_ID = "2c38cb31d21448ef965b645c5bfba7d8"
SPOTIPY_CLIENT_SECRET = "b8b5c2bf424f4370a569e5ad4f0b1760"

client_credentials_manager = SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET
)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


MOOD_PLAYLISTS = {
    "sad": "7zNvXEjgmE1110slXAuZie",       # Motivational Songs India
    "fear": "1q3uUZUSYmro5IxJnQYD8y",      # Peaceful Piano
    "angry": "0cELuDbnKCAK4rM0TwAFIM",     # Chill Vibes India
    "radiant": "0zc6Hq9OIAengtGG6a3lfs",   # Mood Booster (renamed from happy to radiant)
    "neutral": "4zZz660QngrSW1hj6U075q?si=vTdBMgSBRTi9sZ5bgg6Qiw",    # Happy Hits
    "joy": "7DABXCuuPXgzogqy3OJIgH",        # joyful songs 
    "anger": "0cELuDbnKCAK4rM0TwAFIM",     # Chill Vibes India
}

def get_tracks_for_emotion(mood, limit=5):
    """Fetch tracks from the playlist mapped to the given mood."""
    mood = mood.lower().strip()
    playlist_id = MOOD_PLAYLISTS.get(mood)

    if not playlist_id:
        raise ValueError(f"Unknown mood '{mood}'. Available moods: {', '.join(MOOD_PLAYLISTS.keys())}")

    results = sp.playlist_tracks(playlist_id, limit=limit)
    tracks = []
    for item in results['items']:
        track = item.get('track')
        if track:
            tracks.append({
                "name": track['name'],
                "artist": track['artists'][0]['name'],
                "url": track['external_urls']['spotify']
            })
    return tracks


if __name__ == "__main__":
    for mood in MOOD_PLAYLISTS.keys():
        print(f"\nFetching songs for mood: {mood}")
        for t in get_tracks_for_emotion(mood):
            print(f"{t['name']} - {t['artist']} ({t['url']})")

