import os
import requests
import random
import time

def setup_folders():
    for f in ['gameplay', 'music', 'memes', 'assets']:
        if not os.path.exists(f): os.makedirs(f)

def download_open_assets():
    # Permanent Backup Links
    v_url = "https://raw.githubusercontent.com/intel-iot-devkit/sample-videos/master/car-detection.mp4"
    m_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    
    print("📥 Downloading Video & Music...")
    with open('gameplay/bg_gameplay.mp4', 'wb') as f: f.write(requests.get(v_url).content)
    with open('music/bg_music.mp3', 'wb') as f: f.write(requests.get(m_url).content)
    print("✅ Base Assets Ready!")

def get_reddit_memes_stealth():
    print("🕵️ Entering Reddit Stealth Mode...")
    # Trending Subreddits for Roasts & Memes
    subs = ['backroomslore', 'wholesomememes', 'Funnymemes', 'AdviceAnimals']
    
    # Real Browser Headers to bypass 403
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
        'Accept': 'application/json'
    }

    count = 0
    random.shuffle(subs)
    
    for sub in subs:
        try:
            url = f"https://www.reddit.com/r/{sub}/top/.json?t=day&limit=20"
            response = requests.get(url, headers=headers, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                posts = data['data']['children']
                for post in posts:
                    img_url = post['data']['url']
                    # Sirf high quality images uthayega
                    if img_url.endswith(('.jpg', '.png', '.jpeg')) and not post['data']['over_18']:
                        print(f"📸 Found Reddit Gold: {img_url}")
                        img_res = requests.get(img_url, headers=headers)
                        with open(f'memes/meme_{count}.jpg', 'wb') as f:
                            f.write(img_res.content)
                        count += 1
                        if count >= 10: return True
            else:
                print(f"⚠️ Sub r/{sub} blocked us with status {response.status_code}")
                time.sleep(2) # Thoda gap taaki ban na ho
        except Exception as e:
            print(f"❌ Error in r/{sub}: {e}")
    return count > 0

if __name__ == "__main__":
    setup_folders()
    download_open_assets()
    success = get_reddit_memes_stealth()
    if not success:
        print("🚩 Reddit blocked all, falling back to Imgflip...")
        # Yahan aapka purana Imgflip wala code backup mein rahega
        
