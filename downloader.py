import subprocess

def download_background_assets():
    # YouTube se gameplay download karne ke liye (Zero Data use)
    # Ye link ek no-copyright gameplay ka hai
    url = "https://www.youtube.com/watch?v=n_Dv47ToG8M" 
    print("📥 Downloading Gameplay from YT (GitHub Server)...")
    subprocess.run(['yt-dlp', '-f', 'bestvideo[height<=720]', '-o', 'gameplay/bg_gameplay.mp4', url])

# Hum ise main script ke shuru mein call karenge
