import os
import subprocess

def download_assets():
    # Folder structure setup
    folders = ['gameplay', 'sigma_clips', 'music', 'assets']
    for f in folders:
        if not os.path.exists(f): os.makedirs(f)

    # 📝 Working Links ki List (Updated)
    links = [
        "https://youtu.be/z121mUPexGc?si=OE1N5iiCZvOWTSqZ", # Fresh Minecraft Parkour
        "https://youtu.be/VS3D8bgYhf4?si=VoEbZ8u79rjBsC0S", # Subway Surfers
        "https://youtu.be/74voi0vlxHE?si=pJouMlxcBq33VsOd"  # GTA V Ramp
    ]

    if not os.listdir('gameplay'):
        for url in links:
            print(f"📥 Trying to download: {url}")
            # --no-playlist isliye taaki poori list download na hone lage
            res = subprocess.run(['yt-dlp', '-f', 'bestvideo[height<=720]', '--no-playlist', '-o', 'gameplay/bg_gameplay.mp4', url])
            if res.returncode == 0:
                print("✅ Gameplay Downloaded!")
                break
    
    # 🏎️ Sigma Clips (Pexels - Always Working)
    if not os.listdir('sigma_clips'):
        print("📥 Downloading Sigma Clip from Pexels API...")
        # Ye direct high-quality drifting car video ka link hai
        os.system("curl -L -o sigma_clips/sigma1.mp4 'https://www.pexels.com/video/854671/download/'")

if __name__ == "__main__":
    download_assets()
