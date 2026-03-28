import os
import requests
import random

def setup_folders():
    folders = ['gameplay', 'music', 'memes', 'assets']
    for f in folders:
        if not os.path.exists(f):
            os.makedirs(f)

def download_open_assets():
    # 🏎️ 1. Direct Video Links (No Redirects)
    # Ye Pixabay ke direct CDN links hain jo seedha mp4 download karte hain
    video_links = [
        "https://cdn.pixabay.com/video/2021/04/12/70796-536130421_tiny.mp4", # Car drifting
        "https://cdn.pixabay.com/video/2023/10/22/186050-877312154_tiny.mp4", # City Drive
        "https://cdn.pixabay.com/video/2020/09/11/49607-458392186_tiny.mp4"  # Highway
    ]
    
    print("📥 Downloading Background Video...")
    v_url = random.choice(video_links)
    # Stream=True taaki badi file sahi se download ho
    with requests.get(v_url, stream=True) as r:
        r.raise_for_status()
        with open('gameplay/bg_gameplay.mp4', 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print("✅ Video File Saved!")

    # 🎵 2. Music (Direct MP3)
    music_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" 
    print("📥 Downloading Music...")
    m_data = requests.get(music_url)
    with open('music/bg_music.mp3', 'wb') as f:
        f.write(m_data.content)
    print("✅ Music Ready!")

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
    download_open_assets()
    get_memes_from_imgflip()
    print("🚀 All Assets Ready for Video Making!")
    
