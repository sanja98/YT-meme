import os
import requests
import random

def setup_folders():
    folders = ['gameplay', 'music', 'memes', 'assets']
    for f in folders:
        if not os.path.exists(f):
            os.makedirs(f)

def download_open_assets():
    # 🏎️ 1. Direct Video Links (High Speed & Permanent)
    # Ye samples hamesha available rehte hain testing aur automation ke liye
    video_links = [
        "https://v.redd.it/3041933/DASH_480.mp4", 
        "https://www.w3schools.com/html/mov_bbb.mp4", # Backup link
        "https://raw.githubusercontent.com/intel-iot-devkit/sample-videos/master/car-detection.mp4"
    ]
    
    print("📥 Downloading Background Video...")
    try:
        v_url = random.choice(video_links)
        r = requests.get(v_url, stream=True, timeout=30)
        r.raise_for_status()
        with open('gameplay/bg_gameplay.mp4', 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        print("✅ Video File Saved!")
    except:
        # Emergency Backup: Agar upar wale fail hue toh ye pakka chalega
        print("⚠️ Primary links failed, using emergency backup...")
        os.system("curl -L -o gameplay/bg_gameplay.mp4 'https://github.com/intel-iot-devkit/sample-videos/raw/master/bottle-detection.mp4'")

    # 🎵 2. Music (Stable Link)
    music_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" 
    print("📥 Downloading Music...")
    try:
        m_data = requests.get(music_url, timeout=20)
        with open('music/bg_music.mp3', 'wb') as f:
            f.write(m_data.content)
        print("✅ Music Ready!")
    except:
        print("⚠️ Music download failed, creating silent audio...")
        # Agar music fail hua toh 10 sec ka silent file bana dega script crash hone se bachane ke liye
        os.system("ffmpeg -f lavfi -i anullsrc=r=44100:cl=stereo -t 10 -q:a 9 -acodec libmp3lame music/bg_music.mp3")

def get_memes_from_imgflip():
    print("🤖 Fetching Trending Memes...")
    try:
        url = "https://api.imgflip.com/get_memes"
        response = requests.get(url, timeout=15).json()
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
    print("🚀 All Assets Ready!")
    
