import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp_oauth = SpotifyOAuth(
    client_id="4a2cbb97c5504b7dbe7a2efc0c840bf2",
    client_secret="0fb3aa1797704da5925b662d34732f95",
    redirect_uri="https://5000-t0mm4s0bry-spotify-lnvu9gwu5vc.ws-eu117.gitpod.io/callback",
    scope = "user-read-private playlist-read-private"
)

def get_spotify_object():
    return spotipy.Spotify(auth_manager=sp_oauth)