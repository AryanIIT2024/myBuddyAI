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

def get_tracks_for_emotion(emotion, limit=5):
    results = sp.search(q=emotion, type='track', limit=limit)
    tracks = []
    for item in results['tracks']['items']:
        tracks.append({
            'name': item['name'],
            'artist': item['artists'][0]['name'],
            'url': item['external_urls']['spotify']
        })
    return tracks