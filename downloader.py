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
    gameplay_links = [
        "https://youtu.be/74voi0vlxHE",
        "https://youtu.be/VS3D8bgYhf4",
        "https://youtu.be/z121mUPexGc"
    ]
    music_url = "https://youtu.be/MbOk39AytPs"

    if not os.listdir('gameplay'):
        url = random.choice(gameplay_links)
        print(f"📥 Downloading Gameplay from: {url}")
        subprocess.run(['yt-dlp', '-f', 'bestvideo[height<=720]', '--no-playlist', '-o', 'gameplay/bg_gameplay.mp4', url])
    
    if not os.listdir('music'):
        print(f"📥 Downloading Phonk Music from: {music_url}")
        subprocess.run(['yt-dlp', '-x', '--audio-format', 'mp3', '--no-playlist', '-o', 'music/bg_music.mp3', music_url])

def get_memes_from_imgflip():
    print("🤖 Fetching Trending Memes from Imgflip...")
    try:
        # Imgflip API for top 100 popular memes
        url = "https://api.imgflip.com/get_memes"
        response = requests.get(url).json()
        
        if response['success']:
            memes = response['data']['memes']
            # Random 10 memes pick karte hain
            selected_memes = random.sample(memes, 10)
            
            for i, meme in enumerate(selected_memes):
                img_url = meme['url']
                print(f"📸 Downloading Meme {i}: {img_url}")
                img_data = requests.get(img_url).content
                with open(f'memes/meme_{i}.jpg', 'wb') as f:
                    f.write(img_data)
            return True
    except Exception as e:
        print(f"❌ Error fetching memes: {e}")
    return False

if __name__ == "__main__":
    setup_folders()
    download_youtube_assets()
    # Reddit block hai toh Imgflip use karenge
    get_memes_from_imgflip()
    print("🚀 All Assets Ready!")
    
