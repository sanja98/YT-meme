import os
import subprocess
import requests
import random

def setup_folders():
    # Zaruri folders create karna
    folders = ['gameplay', 'music', 'memes', 'assets']
    for f in folders:
        if not os.path.exists(f):
            os.makedirs(f)
            print(f"✅ Folder Created: {f}")

def download_youtube_assets():
    # 🎮 Aapke working Gameplay Links
    gameplay_links = [
        "https://youtu.be/74voi0vlxHE",
        "https://youtu.be/VS3D8bgYhf4",
        "https://youtu.be/z121mUPexGc"
    ]
    
    # 🎵 Aapka working Phonk Music Link
    music_url = "https://youtu.be/MbOk39AytPs"

    # Gameplay Download (Agar folder khali hai toh)
    if not os.listdir('gameplay'):
        url = random.choice(gameplay_links)
        print(f"📥 Downloading Gameplay from: {url}")
        # bestvideo[height<=720] speed ke liye rakha hai
        subprocess.run(['yt-dlp', '-f', 'bestvideo[height<=720]', '--no-playlist', '-o', 'gameplay/bg_gameplay.mp4', url])
    else:
        print("✅ Gameplay already exists.")
    
    # Music Download (Extracting only Audio)
    if not os.listdir('music'):
        print(f"📥 Downloading Phonk Music from: {music_url}")
        subprocess.run(['yt-dlp', '-x', '--audio-format', 'mp3', '--no-playlist', '-o', 'music/bg_music.mp3', music_url])
    else:
        print("✅ Music already exists.")

def scrape_reddit_memes():
    print("🤖 Scraping Reddit for Fresh Memes...")
    subreddits = ['memes', 'dankmemes', 'shitposting']
    
    # Solid User-Agent to bypass Reddit blocks
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    count = 0
    for sub in subreddits:
        try:
            # Adding a random parameter 'z' to prevent cache issues
            url = f"https://www.reddit.com/r/{sub}/top/.json?t=day&z={random.randint(1,999)}"
            response = requests.get(url, headers=headers)
            
            if response.status_code != 200:
                print(f"⚠️ Reddit returned {response.status_code} for r/{sub}")
                continue

            res = response.json()
            posts = res['data']['children']
            
            for post in posts:
                data = post['data']
                img_url = data['url']
                
                # Check if it's a direct image link and not NSFW
                if any(img_url.endswith(ext) for ext in ['.jpg', '.png', '.jpeg']):
                    if not data.get('over_18', False):
                        print(f"📸 Found Meme: {img_url}")
                        img_data = requests.get(img_url, headers=headers).content
                        with open(f'memes/meme_{count}.jpg', 'wb') as f:
                            f.write(img_data)
                        count += 1
                        if count >= 10: break # Ek baar mein max 10 memes
            if count >= 10: break
        except Exception as e:
            print(f"❌ Error scraping {sub}: {e}")

if __name__ == "__main__":
    setup_folders()
    download_youtube_assets()
    scrape_reddit_memes()
    print("🚀 All Assets Ready for Video Making!")
                        
