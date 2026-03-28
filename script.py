import os
import random
import moviepy.editor as mp
from PIL import Image

# MoviePy aur Pillow fix
if not hasattr(Image, 'ANTIALIAS'):
    Image.ANTIALIAS = Image.LANCZOS

def make_meme_video():
    print("🎬 Starting Video Generation...")
    
    gameplay_file = "gameplay/bg_gameplay.mp4"
    music_file = "music/bg_music.mp3"
    meme_folder = "memes"

    if not os.path.exists(gameplay_file) or not os.path.exists(music_file):
        print("❌ Error: Files missing!")
        return

    all_memes = [f for f in os.listdir(meme_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]
    if not all_memes:
        print("❌ No memes found!")
        return
    
    selected_meme_path = os.path.join(meme_folder, random.choice(all_memes))
    print(f"📸 Using Meme: {selected_meme_path}")

    # 1. Video Processing
    video = mp.VideoFileClip(gameplay_file)
    duration = min(10, int(video.duration))
    start_time = random.randint(0, max(0, int(video.duration) - duration))
    
    # Simple Resize for Shorts
    video_clip = video.subclip(start_time, start_time + duration).resize(height=1920)
    
    # 2. Meme Overlay
    meme_clip = mp.ImageClip(selected_meme_path).set_duration(duration)
    if meme_clip.w > 900:
        meme_clip = meme_clip.resize(width=900)
    meme_clip = meme_clip.set_position(("center", "center"))

    # 3. Audio Processing
    audio = mp.AudioFileClip(music_file)
    audio_start = random.randint(0, max(0, int(audio.duration) - duration))
    final_audio = audio.subclip(audio_start, audio_start + duration)

    # 4. Assembly
    final_video = mp.CompositeVideoClip([video_clip, meme_clip])
    final_video = final_video.set_audio(final_audio)

    # 5. Export
    final_video.write_videofile("final_meme_short.mp4", fps=24, codec="libx264", audio_codec="aac")
    print("✅ Successfully Created: final_meme_short.mp4")

if __name__ == "__main__":
    try:
        make_meme_video()
    except Exception as e:
        print(f"❌ Script Failed: {e}")
        
