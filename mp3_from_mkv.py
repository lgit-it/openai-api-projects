from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_file_path, output_audio_path):
    # Carica il file video
    video = VideoFileClip(video_file_path)
    
    # Estrae l'audio dal video
    audio = video.audio
    
    # Salva l'audio in un file separato
    audio.write_audiofile(output_audio_path)

# Sostituisci con il percorso del tuo file video MKV
video_file_path = 'data\\2023-11-13 10-01-49.mkv'

# Sostituisci con il percorso dove vuoi salvare il file audio
output_audio_path = 'data\\2023-11-13 10-01-49.mp3'

# Chiama la funzione
extract_audio_from_video(video_file_path, output_audio_path)

print("Done!")
