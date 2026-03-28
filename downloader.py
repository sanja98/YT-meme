import os
import subprocess

def download_assets():
    # Zaruri folders check karna
    folders = ['gameplay', 'sigma_clips', 'music', 'assets']
    for f in folders:
        if not os.path.exists(f): os.makedirs(f)

    # Aapke diye hue fresh links
    links = [
        "https://youtu.be/74voi0vlxHE",
        "https://youtu.be/VS3D8bgYhf4",
        "https://youtu.be/z121mUPexGc"
    ]

    # Gameplay download logic
    if not os.listdir('gameplay'):
        for url in links:
            print(f"📥 Downloading from: {url}")
            # yt-dlp GitHub ke internet se download karega
            res = subprocess.run(['yt-dlp', '-f', 'bestvideo[height<=720]', '--no-playlist', '-o', 'gameplay/bg_gameplay.mp4', url])
            if res.returncode == 0:
                print("✅ Gameplay ready!")
                break
    
    # Sigma clip backup (Pexels se automatic)
    if not os.listdir('sigma_clips'):
        print("📥 Fetching Sigma template...")
        os.system("curl -L -o sigma_clips/sigma1.mp4 'https://www.pexels.com/video/854671/download/'")

if __name__ == "__main__":
    download_assets()
