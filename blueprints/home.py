from flask import Blueprint, render_template, session
from services.spotify_oauth import get_spotify_object
import spotipy

home_bp = Blueprint('home', __name__)

@home_bp.route('/home')
def home():
    sp = get_spotify_object()
    if not isinstance(sp, spotipy.Spotify):
        return sp  

    try:
        user_info = sp.current_user()
        playlists = sp.current_user_playlists()["items"]
    except Exception:
        return redirect(url_for("auth.login"))

    return render_template("home.html", user_info=user_info, playlists=playlists)


def playlist(playlist_id):
    sp = get_spotify_client()
    if not isinstance(sp, spotipy.Spotify):
        return sp  
    
    try:
        playlist_data = sp.playlist(playlist_id)
        tracks_data = playlist_data["tracks"]["items"]
        tracks = [
            {
                "name": track["track"]["name"],
                "artist": track["track"]["artists"][0]["name"],
                "album": track["track"]["album"]["name"],
                "cover": track["track"]["album"].get("images", [{}])[0].get("url")
            }
            for track in tracks_data if track.get("track")
        ]
    except Exception:
        return redirect(url_for("auth.login"))

    return render_template("playlist.html", tracks=tracks)
