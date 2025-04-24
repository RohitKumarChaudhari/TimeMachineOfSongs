# ⏳🎶 TimeMachineOfSongs

**TimeMachineOfSongs** is a Python app that lets you "travel back in time" to your favorite year, month, and day — then scrapes the Top 100 Billboard songs of that date and creates a Spotify playlist with them using the Spotify Web API.

---

## 🧠 What It Does

1. Asks the user to enter a date (YYYY-MM-DD)
2. Scrapes the **Billboard Hot 100** chart for that date
3. Uses the **Spotify API** (via `spotipy`) to search for those songs
4. Creates a **Spotify playlist** with the found tracks

---

## 🛠️ Tech Stack

- Python 🐍
- `requests` – for sending HTTP requests
- `BeautifulSoup` – for scraping Billboard
- `spotipy` – for interacting with Spotify API
- `dotenv` – for managing credentials securely

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/RohitKumarChaudahari/TimeMachineOfSongs.git
cd TimeMachineOfSongs
```
### 2. Install Dependencies 

```bash
pip install -r requirements.txt
```

### 3. Set Up Spotify Developer Account

- Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
- Create an app and get your:
  - `CLIENT_ID`
  - `CLIENT_SECRET`
  - `REDIRECT_URI` (e.g., http://localhost:8888/callback)

### 4. Create .env File
```env
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
```
# ▶️ How to Use  
```bash
python main.py
```
You will be prompted:
```
Which year do you want to travel to? Type the date in this format YYYY-MM-DD:
```
Example:
```
2001-05-10
```
The app will:

- Scrape the Billboard Hot 100 for that date
- Search for each song on Spotify
- Create a playlist named: Billboard Top 100 - 2001-05-10

# 🎵 Note
- Some songs may not be found on Spotify due to name mismatches or unavailability.
- You must have a Spotify account to use this app and create playlists.

# Built By
```
🎧 Built with Python, nostalgia, and APIs by Rohit. Travel back in time — one song at a time. ⏱️
```

# 📬 Contact
```
Have feedback or want to contribute? Open an issue
```
