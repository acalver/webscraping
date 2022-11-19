# Import libraries
import requests
import re
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth



# Create an URL object - must be page of 6 music radio show
url = 'https://www.bbc.co.uk/sounds/play/m001dc67'
# Create object page
page = requests.get(url).text

#get track IDs
tracks = re.findall(r"https://open\.spotify\.com/track/[0-9a-zA-Z]+", page)
tracks = [s.replace('https://open.spotify.com/track/', '') for s in tracks]


#this is private information
#to obtain these, see the spotipy documentation
SPOTIFY_CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]

#set up link to Spotify API
auth_manager = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, 
                            client_secret= SPOTIFY_CLIENT_SECRET,
                            redirect_uri='http://localhost:9000',
                            scope=['playlist-modify-private', 'playlist-modify-public'])
sp = spotipy.Spotify(auth_manager=auth_manager)

#sp.user_playlist_create('os.environ["SPOTIFY_NAME"]', '6Music Webscraping', public=False)
sp.playlist_add_items(playlist_id='insert_playlist_id_here',items=tracks)