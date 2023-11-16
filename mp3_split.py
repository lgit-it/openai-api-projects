import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Carica il file audio
def load_audio(file_path):
    return AudioSegment.from_file(file_path)

# Suddividi l'audio sui momenti di silenzio
def split_audio(audio_segment, min_silence_len=1000, silence_thresh=-16, min_seg_len=300000, max_seg_len=480000):
    """
    :param audio_segment: AudioSegment object
    :param min_silence_len: lunghezza minima del silenzio per essere considerato come punto di suddivisione (in ms)
    :param silence_thresh: sotto questa soglia, il suono è considerato silenzio (in dBFS)
    :param min_seg_len: lunghezza minima del segmento (in ms)
    :param max_seg_len: lunghezza massima del segmento (in ms)
    :return: lista di segmenti audio
    """
    chunks = split_on_silence(
        audio_segment,
        min_silence_len=min_silence_len,
        silence_thresh=silence_thresh,
        keep_silence=500
    )

    # Unisci i segmenti troppo brevi e spezza quelli troppo lunghi
    segmented = []
    temp_segment = AudioSegment.empty()
    for chunk in chunks:
        if len(temp_segment) + len(chunk) <= max_seg_len:
            temp_segment += chunk
        else:
            if len(temp_segment) >= min_seg_len:
                segmented.append(temp_segment)
            temp_segment = chunk

    if len(temp_segment) >= min_seg_len:
        segmented.append(temp_segment)

    return segmented

# Salva i segmenti in file separati
def save_segments(segments, base_filename):
    for i, segment in enumerate(segments):
        segment.export(f"{base_filename}_part{i}.mp3", format="mp3")

# Esempio di utilizzo dello script
audio_path = 'data\\2023-11-13_10-01-49.mp3'
audio = load_audio(audio_path)
segments = split_audio(audio)
save_segments(segments, "output_filename")
