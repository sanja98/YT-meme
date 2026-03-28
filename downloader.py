import os
import subprocess
import requests
import random

def setup_folders():
    # Folder structure ensure karna
    folders = ['gameplay', 'music', 'memes', 'assets']
    for f in folders:
        if not os.path.exists(f):
            os.makedirs(f)

def download_youtube_assets():
    # 🎮 Fresh Gameplay Links
    gameplay_links = [
        "https://youtu.be/74voi0vlxHE",
        "https://youtu.be/VS3D8bgYhf4",
        "https://youtu.be/z121mUPexGc"
    ]
    
    # 🎵 Music Link
    music_url = "https://youtu.be/MbOk39AytPs"

    # FORCE DOWNLOAD (Checking files explicitly)
    print("📥 Downloading Gameplay...")
    url = random.choice(gameplay_links)
    # -f 'bestvideo[height<=480]' speed ke liye (GitHub Actions ke liye kaafi hai)
    subprocess.run(['yt-dlp', '-f', 'bestvideo[height<=480]', '--no-playlist', '-o', 'gameplay/bg_gameplay.mp4', url])
    
    print("📥 Downloading Music...")
    subprocess.run(['yt-dlp', '-x', '--audio-format', 'mp3', '--no-playlist', '-o', 'music/bg_music.mp3', music_url])

def get_memes_from_imgflip():
    print("🤖 Fetching Trending Memes...")
    try:
        url = "https://api.imgflip.com/get_memes"
        response = requests.get(url).json()
        if response['success']:
            memes = response['data']['memes']
            selected_memes = random.sample(memes, 10)
            for i, meme in enumerate(selected_memes):
                img_data = requests.get(meme['url']).content
                with open(f'memes/meme_{i}.jpg', 'wb') as f:
                    f.write(img_data)
            print("✅ Memes Downloaded!")
    except Exception as e:
        print(f"❌ Error fetching memes: {e}")

if __name__ == "__main__":
    setup_folders()
    download_youtube_assets()
    get_memes_from_imgflip()
    print("🚀 All Assets Ready!")
    
