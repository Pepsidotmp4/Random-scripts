import requests
from spotipy.oauth2 import SpotifyOAuth
import os

# Replace these with your Spotify API credentials
SPOTIPY_CLIENT_ID = 'your_client_id'
SPOTIPY_CLIENT_SECRET = 'your_client_secret'
SPOTIPY_REDIRECT_URI = 'your_redirect_uri'
SCOPE = 'user-read-currently-playing'

# Replace with your Discord webhook URL
DISCORD_WEBHOOK_URL = 'your_discord_webhook_url'

# Specify a custom cache path
CACHE_PATH = '.spotify_cache'

def get_access_token():
    sp_oauth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                            client_secret=SPOTIPY_CLIENT_SECRET,
                            redirect_uri=SPOTIPY_REDIRECT_URI,
                            scope=SCOPE,
                            cache_path=CACHE_PATH)
    token_info = sp_oauth.get_cached_token()
    
    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        print(f"Please navigate here: {auth_url}")
        response = input("Enter the URL you were redirected to: ")
        code = sp_oauth.parse_response_code(response)
        token_info = sp_oauth.get_access_token(code)
    else:
        if sp_oauth.is_token_expired(token_info):
            token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])

    return token_info['access_token']

def get_current_playing_track(access_token):
    CURRENT_PLAYING_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(CURRENT_PLAYING_URL, headers=headers)
    
    if response.status_code == 200:
        current_track = response.json()
        if current_track and current_track['is_playing']:
            track_name = current_track['item']['name']
            artist_name = ', '.join([artist['name'] for artist in current_track['item']['artists']])
            album_cover = current_track['item']['album']['images'][0]['url']
            return {
                'track_name': track_name,
                'artist_name': artist_name,
                'album_cover': album_cover
            }
        else:
            return None
    else:
        print(f"Failed to get current playing track. Status code: {response.status_code}")
        return None

def send_to_discord(webhook_url, track_info):
    data = {
        "content": f"**Now Playing:**\n**Track:** {track_info['track_name']}\n**Artist:** {track_info['artist_name']}\n**Album Cover:** {track_info['album_cover']}"
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Successfully sent to Discord.")
    else:
        print(f"Failed to send to Discord. Status code: {response.status_code}")

if __name__ == "__main__":
    access_token = get_access_token()
    track_info = get_current_playing_track(access_token)
    if track_info:
        print(f"Track Name: {track_info['track_name']}")
        print(f"Artist: {track_info['artist_name']}")
        print(f"Album Cover: {track_info['album_cover']}")
        send_to_discord(DISCORD_WEBHOOK_URL, track_info)
    else:
        print("No track currently playing.")

