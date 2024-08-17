import yt_dlp
import os

musica = "/mnt/storage/media/music"
music_playlist = "/mnt/storage/media/music"
pelis = "/mnt/storage/media/pelis"
series = "/mnt/storage/media/pelis"

topic = "respuestas"


def descargar_audios(url):
    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(musica, "%(title)s.%(ext)s"),
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            result = f"Descarga de audio completada: {info['title']}"
            print(result)
            return result
    except Exception as e:
        result = f"Ocurrió un error descargando audios: {str(e)}"
        print(result)
        return result


# descargar_audios("https://www.youtube.com/watch?v=Dwvh96a7Gq0")


def descargar_videos(url):
    try:
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": os.path.join(pelis, "%(title)s.%(ext)s"),
            "merge_output_format": "mp4",
            "postprocessors": [
                {
                    "key": "FFmpegVideoConvertor",
                    "preferedformat": "mp4",
                }
            ],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            video_path = os.path.join(pelis, f"{info['title']}.mp4")
            audio_path = os.path.join(pelis, f"{info['title']}.mp3")
            result = f"Descarga de video completada: {info['title']}"
            print(result)
            return result
    except Exception as e:
        result = f"Ocurrió un error descargando el video: {str(e)}"
        print(result)
        return result


# descargar_videos("https://www.youtube.com/watch?v=Dwvh96a7Gq0")


def descargar_video(url, ruta_destino):
    try:
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": os.path.join(ruta_destino, "%(title)s.%(ext)s"),
            "merge_output_format": "mp4",
            "postprocessors": [
                {
                    "key": "FFmpegVideoConvertor",
                    "preferedformat": "mp4",
                }
            ],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            video_path = os.path.join(ruta_destino, f"{info['title']}.mp4")
            audio_path = os.path.join(ruta_destino, f"{info['title']}.mp3")
            ruta_salida = os.path.join(ruta_destino, f"{info['title']}_mix.mp4")
            if os.path.exists(video_path) and os.path.exists(audio_path):
                os.system(
                    f"ffmpeg -i '{video_path}' -i '{audio_path}' -c:v copy -c:a aac -y '{ruta_salida}'"
                )
                os.remove(video_path)
                os.remove(audio_path)
                result = f"Descarga de video completada: {info['title']}"
            else:
                result = "No se encontraron los archivos de video o audio."
            print(result)
            return result
    except Exception as e:
        result = f"Ocurrió un error: {str(e)}"
        return result


def descargar_audio(url, ruta_destino):
    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(ruta_destino, "%(title)s.%(ext)s"),
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            result = f"Descarga de audio completada: {info['title']}"
            return result
    except Exception as e:
        result = f"Ocurrió un error: {str(e)}"
        return result


def descargar_playlist(url_playlist):
    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(musica, "%(playlist)s/%(title)s.%(ext)s"),
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url_playlist])
            playlist_title = ydl.extract_info(url_playlist, download=False)["title"]
            result = f"Descarga de la playlist '{playlist_title}' completada!"
            return result
    except Exception as e:
        result = f"Ocurrió un error: {str(e)}"
        return result


def descargar_series(url_playlist):
    try:
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": os.path.join(series, "%(playlist)s/%(title)s.%(ext)s"),
            "merge_output_format": "mp4",
            "postprocessors": [
                {
                    "key": "FFmpegVideoConvertor",
                    "preferedformat": "mp4",
                }
            ],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url_playlist])
            playlist_title = ydl.extract_info(url_playlist, download=False)["title"]
            result = f"Descarga de la serie '{playlist_title}' completada!"
            return result
    except Exception as e:
        result = f"Ocurrió un error: {str(e)}"
        return result
