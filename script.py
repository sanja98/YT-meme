import os
import random
import moviepy.editor as mp

def make_meme_video():
    print("🎬 Starting Video Generation...")
    
    # 1. Check if folders and files exist
    gameplay_file = "gameplay/bg_gameplay.mp4"
    music_file = "music/bg_music.mp3"
    meme_folder = "memes"

    if not os.path.exists(gameplay_file) or not os.path.exists(music_file):
        print("❌ Error: Gameplay or Music file missing!")
        return

    # 2. Random Meme pick karna
    all_memes = [f for f in os.listdir(meme_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]
    if not all_memes:
        print("❌ No memes found in folder!")
        return
    
    selected_meme_path = os.path.join(meme_folder, random.choice(all_memes))
    print(f"📸 Using Meme: {selected_meme_path}")

    # 3. Gameplay Processing (10 Seconds)
    video = mp.VideoFileClip(gameplay_file)
    # Random start point dhundna (last 12 sec chhod kar)
    start_time = random.randint(0, max(0, int(video.duration) - 12))
    
    # Video ko 9:16 (Shorts) format mein lana
    video_clip = video.subclip(start_time, start_time + 10)
    video_clip = video_clip.resize(height=1920) # Height fix kar di
    
    # Center se 1080 width crop karna
    w, h = video_clip.size
    video_clip = video_clip.crop(x_center=w/2, y_center=h/2, width=1080, height=1920)

    # 4. Meme Overlay Setup
    meme_clip = mp.ImageClip(selected_meme_path).set_duration(10)
    
    # Meme Resize Logic (Screen se bada na ho)
    if meme_clip.w > 900:
        meme_clip = meme_clip.resize(width=900)
    elif meme_clip.h > 1200:
        meme_clip = meme_clip.resize(height=1200)

    # Meme ko center mein rakhna
    meme_clip = meme_clip.set_position(("center", "center"))

    # 5. Audio Processing
    audio = mp.AudioFileClip(music_file)
    audio_start = random.randint(0, max(0, int(audio.duration) - 12))
    final_audio = audio.subclip(audio_start, audio_start + 10)

    # 6. Final Assembly
    final_video = mp.CompositeVideoClip([video_clip, meme_clip])
    final_video = final_video.set_audio(final_audio)

    # 7. Write File
    # threads=4 speed ke liye hai
    final_video.write_videofile("final_meme_short.mp4", fps=30, codec="libx264", audio_codec="aac", threads=4)
    print("✅ Successfully Created: final_meme_short.mp4")

if __name__ == "__main__":
    try:
        make_meme_video()
    except Exception as e:
        print(f"❌ Script Failed: {e}")
        
