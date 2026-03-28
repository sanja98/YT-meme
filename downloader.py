import os
import subprocess
import requests
import random

def setup_folders():
    folders = ['gameplay', 'music', 'memes', 'assets']
    for f in folders:
        if not os.path.exists(f):
            os.makedirs(f)
            print(f"✅ Folder Created: {f}")

def download_youtube_assets():
    # 🎮 Gameplay Links (Tere Diye Huye)
    gameplay_links = [
        "https://youtu.be/74voi0vlxHE",
        "https://youtu.be/VS3D8bgYhf4",
        "https://youtu.be/z121mUPexGc"
    ]
    
    # 🎵 Music Link (Tera Naya Phonk Link)
    music_url = "https://youtu.be/MbOk39AytPs"

    # Gameplay Download (Only if folder is empty)
    if not os.listdir('gameplay'):
        url = random.choice(gameplay_links)
        print(f"📥 Downloading Gameplay from: {url}")
        subprocess.run(['yt-dlp', '-f', 'bestvideo[height<=720]', '--no-playlist', '-o', 'gameplay/bg_gameplay.mp4', url])
    
    # Music Download (Extracting only Audio as MP3)
    if not os.listdir('music'):
        print(f"📥 Downloading Phonk Music from: {music_url}")
        subprocess.run(['yt-dlp', '-x', '--audio-format', 'mp3', '--no-playlist', '-o', 'music/bg_music.mp3', music_url])

def scrape_reddit_memes():
    print("🤖 Scraping Reddit for Fresh Memes...")
    # r/memes aur r/dankmemes se top images uthana
    subreddits = ['memes', 'dankmemes']
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    count = 0
    for sub in subreddits:
        try:
            url = f"https://www.reddit.com/r/{sub}/top/.json?limit=15&t=day"
            res = requests.get(url, headers=headers).json()
            posts = res['data']['children']
            
            for post in posts:
                img_url = post['data']['url']
                # Sirf images (jpg/png) download karega, videos/gifs nahi
                if img_url.endswith(('.jpg', '.png', '.jpeg')) and not post['data']['over_18']:
                    img_data = requests.get(img_url).content
                    with open(f'memes/meme_{count}.jpg', 'wb') as f:
                        f.write(img_data)
                    count += 1
                    if count >= 10: break # Max 10 memes ek baar mein
            if count >= 10: break
        except Exception as e:
            print(f"❌ Error scraping {sub}: {e}")

if __name__ == "__main__":
    setup_folders()
    download_youtube_assets()
    scrape_reddit_memes()
    print("🚀 All Assets Ready for Video Making!")
    
