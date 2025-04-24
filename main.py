import os
import spotipy
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")


date = input("Which year do you want to Travel? Type the date in this formate YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}/"
URL_INDIA = f"https://www.billboard.com/charts/india-songs-hotw/{date}/"

spotify_url ="https://accounts.spotify.com/authorize"
redirect_uri = "https://example.com/callback"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(URL, headers=header)
bill_board_web_page = response.text

soup = BeautifulSoup(bill_board_web_page, "html.parser")
a = soup.find(name="h3")
music_album = soup.find_all(name="h3",class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 "
                                             "lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 "
                                             "u-line-height-normal@mobile-max a-truncate-ellipsis "
                                             "u-max-width-330 u-max-width-230@tablet-only")

songs = [song.getText().strip() for song in music_album]
songs.append(a.getText().strip())

######################################################### Spotify ####################################################

uri_list =[]
song_links = []

## use this to generate the user_id.
scope =  "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                               client_secret=spotify_client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope,
                                               show_dialog=True,    
                                               cache_path="token.txt"
                                               ))

user_id = sp.current_user()["id"]# gives current user
year = date[:4]

for name in songs:
    result = sp.search(f"track:{name} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
    except IndexError:
        print(f"{name} doesn't exist in Spotify. Skipped.")

# create the playlist.
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist["id"])

sp.playlist_add_items(playlist_id=playlist["id"], items=uri_list)


