import speech_recognition as sr
from pytube import YouTube
from pydub import AudioSegment
import os


# Función para descargar el audio y convertirlo a WAV
def descargar_audio_y_convertir(url, output_filename):
    try:
        # Descargar el video
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        downloaded_filename = video.default_filename

        # Descargar el archivo de audio
        audio_file = video.download()

        # Obtener la ruta completa del archivo descargado
        downloaded_path = os.path.join(os.getcwd(), audio_file)

        # Cargar el audio descargado con pydub
        audio = AudioSegment.from_file(downloaded_path)

        # Crear el nombre de archivo de salida en formato WAV
        output_wav_filename = f"{output_filename}.wav"

        # Convertir el audio a WAV (formato sin comprimir)
        audio.export(output_wav_filename, format="wav")

        print(f"Audio convertido y guardado como {output_wav_filename}")

    except Exception as e:
        print(f"Error al procesar el archivo descargado: {e}")


# Ejemplo de uso
url = "https://www.youtube.com/watch?v=BQErsh_Iff8"  # URL del video de YouTube
output_filename = "audio_convertido"  # Nombre base del archivo de salida

descargar_audio_y_convertir(url, output_filename)
