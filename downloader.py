import os
import requests
import random

def setup_folders():
    folders = ['gameplay', 'music', 'memes', 'assets']
    for f in folders:
        if not os.path.exists(f):
            os.makedirs(f)

def download_open_assets():
    # 🏎️ 1. Gameplay/Background Video (Pexels se)
    # Maine ye 3 best vertical drifting/gameplay clips ke direct links nikaale hain
    video_links = [
        "https://www.pexels.com/video/854671/download/", # Car Drift
        "https://www.pexels.com/video/5752458/download/", # Aesthetic City
        "https://www.pexels.com/video/3041933/download/"  # Highway Drive
    ]
    
    print("📥 Downloading Background Video from Pexels...")
    v_url = random.choice(video_links)
    v_data = requests.get(v_url, stream=True)
    with open('gameplay/bg_gameplay.mp4', 'wb') as f:
        for chunk in v_data.iter_content(chunk_size=1024*1024):
            if chunk: f.write(chunk)
    print("✅ Video Ready!")

    # 🎵 2. Music (Pixabay/Direct MP3)
    # Ye ek trending aesthetic music ka direct link hai
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
    
