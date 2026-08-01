import os
from moviepy import AudioFileClip, VideoFileClip, concatenate_audioclips
from moviepy.video.fx import Loop

# --- 1. Шляхи до файлів ---
script_dir = os.path.dirname(os.path.abspath(__file__))

audio_files = [
    os.path.join(script_dir, "track1.mp3"),
    os.path.join(script_dir, "track2.mp3")
]

rain_video_file = os.path.join(script_dir, "rain.mp4")
output_video = os.path.join(script_dir, "final_lofi_video.mp4")

print("Починаємо обробку файлів...")

# --- 2. Об'єднання звуку ---
audio_clips = [AudioFileClip(track) for track in audio_files]
final_audio = concatenate_audioclips(audio_clips)

total_duration = final_audio.duration
print(f"Загальна тривалість буде: {total_duration / 60:.2f} хвилин(и)")

# --- 3. Обробка відео з дощем ---
bg_video = VideoFileClip(rain_video_file)

# У MoviePy 2.x використовуємо Loop(duration=...)
bg_video_looped = bg_video.with_effects([Loop(duration=total_duration)]).without_audio()

# Накладаємо гітарне аудіо
final_video = bg_video_looped.with_audio(final_audio)

# --- 4. Збереження готового MP4 ---
print("Розпочинається рендеринг відео з анімованим дощем. Зачекайте трохи...")

final_video.write_videofile(
    output_video,
    fps=24,
    codec="libx264",
    audio_codec="aac"
)

# Очищення пам'яті
final_audio.close()
bg_video.close()
bg_video_looped.close()
for clip in audio_clips:
    clip.close()

print(f"Успішно! Готове відео з живим фоном збережено у файлі: {output_video}")