import os
import random
import moviepy.editor as mp
from PIL import Image

def make_meme_video():
    # 1. Assets uthao
    gameplay_file = "gameplay/bg_gameplay.mp4"
    music_file = "music/bg_music.mp3"
    
    # Reddit memes folder se koi bhi ek random image
    all_memes = [f for f in os.listdir('memes') if f.endswith(('.jpg', '.png'))]
    if not all_memes:
        print("❌ No memes found!")
        return
    random_meme = os.path.join('memes', random.choice(all_memes))

    # 2. Gameplay ka random 10-second clip kaato
    video = mp.VideoFileClip(gameplay_file)
    start_time = random.randint(0, int(video.duration) - 12)
    video_clip = video.subclip(start_time, start_time + 10).resize(height=1920)
    video_clip = video_clip.crop(x_center=video_clip.w/2, width=1080, height=1920)

    # 3. Meme Overlay (Center mein chipkana)
    meme_img = mp.ImageClip(random_meme).set_duration(10)
    # Center mein position karna
    if meme_img.w > 900:
    meme_img = meme_img.resize(width=900)

    meme_clip = meme_img.set_position(("center", "center"))

    # 4. Music add karna
    audio = mp.AudioFileClip(music_file)
    audio_start = random.randint(0, int(audio.duration) - 12)
    final_audio = audio.subclip(audio_start, audio_start + 10)

    # 5. Sabko merge karna
    final_video = mp.CompositeVideoClip([video_clip, meme_clip])
    final_video = final_video.set_audio(final_audio)

    # 6. Export
    final_video.write_videofile("final_meme_short.mp4", fps=30, codec="libx264")
    print("✅ Video Generated: final_meme_short.mp4")

if __name__ == "__main__":
    make_meme_video()
