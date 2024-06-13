# descargar_video.py
from pytube import YouTube, Playlist
import os
import re


musica = "/mnt/storage/media/music"
music_playlist = "/mnt/storage/media/music"
pelis = "/mnt/storage/media/pelis"
series = "/mnt/storage/media/pelis"


def descargar_videos(url):
    try:
        yt = YouTube(url)
        nombre_video = yt.title
        print(yt.captions, "aqui los captions")
        print(yt.caption_tracks, "aqui los captions tracks")
        stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
        stream.download(output_path=pelis, filename=yt.title + ".mp4")

        print("La descarga de video se completó correctamente.")
    except Exception as e:
        print("Ocurrió un error durante la descarga de video:", e)


def descargar_video(url, ruta_destino):
    try:
        yt = YouTube(url)
        nombre_video = yt.title
        print(yt.captions, "aqui los captions")
        print(yt.caption_tracks, "aqui los captions tracks")
        stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
        stream.download(output_path=ruta_destino, filename=yt.title + ".mp4")

        print("La descarga de video se completó correctamente.")
    except Exception as e:
        print("Ocurrió un error durante la descarga de video:", e)


def descargar_audios(url):
    try:
        # Crear un objeto YouTube
        yt = YouTube(url)

        # Filtrar por el formato de audio
        audio = yt.streams.filter(only_audio=True).first()

        # Descargar el audio
        audio.download(output_path=musica, filename=yt.title + ".mp3")

        print("Descarga completada!")
    except Exception as e:
        print("Ocurrió un error:", str(e))


def descargar_audio(url, ruta_destino):
    try:
        # Crear un objeto YouTube
        yt = YouTube(url)

        # Filtrar por el formato de audio
        audio = yt.streams.filter(only_audio=True).first()

        # Descargar el audio
        audio.download(output_path=ruta_destino, filename=yt.title + ".mp3")

        print("Descarga completada!")
    except Exception as e:
        print("Ocurrió un error:", str(e))


def ver_atributos_video(video):
    print("Atributos:")
    for attr in dir(video):
        print(attr)
    print()

    print("Pistas de subtítulos (captions):")
    for caption in video.caption_tracks:
        print(caption)

    print()


# def ver_atributos_video(video):
#     print("Atributos:")
#     for attr in dir(video):
#         print(attr)
#     print()
#


def descargar_playlist(url_playlist):
    try:
        playlist = Playlist(url_playlist)
        # Obtener el nombre de la playlist
        nombre_playlist = playlist.title
        print(nombre_playlist)
        ruta_descarga = os.path.join(musica, nombre_playlist)
        print(ruta_descarga)
        if not os.path.exists(ruta_descarga):
            os.makedirs(ruta_descarga)

        for video in playlist.videos:
            # Descargar el audio (aquí debes implementar la lógica para descargar el audio)
            descargar_audio(video.watch_url, ruta_descarga)

        print("La descarga de la playlist de audio se completó correctamente.")
    except Exception as e:
        print("Ocurrió un error durante la descarga de la playlist de audio:", e)


def descargar_series(url_playlist):
    try:
        playlist = Playlist(url_playlist)
        # Obtener el nombre de la playlist
        nombre_playlist = playlist.title
        print(nombre_playlist)
        ruta_descarga = os.path.join(series, nombre_playlist)
        print(ruta_descarga)
        if not os.path.exists(ruta_descarga):
            os.makedirs(ruta_descarga)

        for video in playlist.videos:
            # Descargar el audio (aquí debes implementar la lógica para descargar el audio)
            descargar_video(video.watch_url, ruta_descarga)

        print("La descarga de la playlist de audio se completó correctamente.")
    except Exception as e:
        print("Ocurrió un error durante la descarga de la playlist de audio:", e)
