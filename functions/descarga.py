# descargar.py
from pytube import YouTube, Playlist
import os

# import productor

musica = "./media/music"
music_playlist = "./media/music"
pelis = "./media/pelis"
series = "./media/pelis"

topic = "respuestas"


def descargar_audios(url):
    try:
        # Crear un objeto YouTube
        yt = YouTube(url)

        # Filtrar por el formato de audio
        audio = yt.streams.filter(only_audio=True).first()

        # Descargar el audio
        audio.download(output_path=musica, filename=yt.title + ".mp3")
        result = f"Descarga de audio completada  { yt.title}"
        print(result)
        return result
    except Exception as e:
        result = f"Ocurrió un error descargando audios:{str(e)}"
        print(result)
        return result


descargar_audios("https://www.youtube.com/watch?v=Dwvh96a7Gq0")


def descargar_videos(url):
    try:
        yt = YouTube(url)
        nombre_video = yt.title
        print(f"kamilito pruena obtener nombre :  {nombre_video}")

        # Filtrar los streams que sean progresivos y tengan extensión mp4
        streams = yt.streams.filter(file_extension="mp4").order_by("resolution")
        # print("quite el assc para ver que muestra ", streams)

        highest_resolution_stream = None
        max_resolution = 0

        for stream in streams:
            resolution = int(stream.resolution[:-1])  # Convierte '1080p' a 1080
            if resolution > max_resolution:
                max_resolution = resolution
                highest_resolution_stream = stream

        # Verificar si se encontró algún stream con resolución
        if highest_resolution_stream:
            # Filtrar por el formato de audio
            audio = yt.streams.filter(only_audio=True).first()

            # Descargar el audio
            audio.download(output_path=pelis, filename=f"{nombre_video}.mp3")

            # Descargar el video utilizando el stream con la resolución más alta
            highest_resolution_stream.download(
                output_path=pelis, filename=f"{nombre_video}.mp4"
            )
            ruta_video = os.path.join(pelis, f"{nombre_video}.mp4")
            ruta_audio = os.path.join(pelis, f"{nombre_video}.mp3")
            ruta_salida = os.path.join(pelis, f"{nombre_video}_mix.mp4")
            print(ruta_video)
            print(ruta_audio)
            os.system(
                f"ffmpeg -i '{ruta_video}' -i '{ruta_audio}' -c:v copy -c:a aac -y '{ruta_salida}'"
            )
            os.remove(ruta_video)
            os.remove(ruta_audio)
            result = f"Descarga de video  completada {nombre_video} "
            print(result)
            return result
        else:
            result = f" se encontró ningún stream con resolución para descargar.{nombre_video}"
            print(result)
            return result

    except Exception as e:
        result = f"'Ocurrió un error descargando el video :', {str(e)}"
        print(result)
        return result


descargar_videos("https://www.youtube.com/watch?v=Dwvh96a7Gq0")


def descargar_video(url, ruta_destino):
    try:
        yt = YouTube(url)
        nombre_video = yt.title

        streams = yt.streams.order_by("resolution").asc()

        highest_resolution_stream = None
        max_resolution = 0

        for stream in streams:
            resolution = int(stream.resolution[:-1])  # Convierte '1080p' a 1080

            # Comparar la resolución actual con la máxima encontrada hasta ahora
            if resolution > max_resolution:
                max_resolution = resolution
                highest_resolution_stream = stream

        # Verificar si se encontró algún stream con resolución
        if highest_resolution_stream:
            print(
                f"El stream con la resolución más alta es: {highest_resolution_stream}"
            )

            # Filtrar por el formato de audio
            audio = yt.streams.filter(only_audio=True).first()
            # Descargar el audio
            audio.download(output_path=ruta_destino, filename=f"{nombre_video}.mp3")
            # Descargar el video utilizan`do el stream con la resolución más alta
            highest_resolution_stream.download(
                output_path=ruta_destino, filename=f"{nombre_video}.mp4"
            )

            ruta_video = os.path.join(ruta_destino, f"{nombre_video}.mp4")
            ruta_audio = os.path.join(ruta_destino, f"{nombre_video}.mp3")
            ruta_salida = os.path.join(ruta_destino, f"{nombre_video}_mix.mp4")
            # print(ruta_video)
            # print(ruta_audio)
            os.system(
                f"ffmpeg -i '{ruta_video}' -i '{ruta_audio}' -c:v copy -c:a aac -y '{ruta_salida}'"
            )
            # Borrar los archivos originales
            os.remove(ruta_video)
            os.remove(ruta_audio)
            # print("La descarga de video se completó correctamente.")

            result = f"Descarga de video {nombre_video} completada!"
            return result

        else:
            result = f"se encontró ningún stream con resolución para descargar.{nombre_video}"
            return result

    except Exception as e:
        result = f"Ocurrió un error: { str(e)}"
        return result


def descargar_audio(url, ruta_destino):
    try:
        # Crear un objeto YouTube
        yt = YouTube(url)

        # Filtrar por el formato de audio
        audio = yt.streams.filter(only_audio=True).first()

        # Descargar el audio
        audio.download(
            output_path=ruta_destino,
            filename=yt.title + ".mp3",
        )
        result = f"descarga de audio{yt.title}"
        return result

        # print("Descarga completada!")
    except Exception as e:
        result = f"Ocurrió un error: {str(e)}  "
    return result


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

        result = f"Descarga de {nombre_playlist} completada!"
        return result

    except Exception as e:
        result = f"Ocurrió un error:{ str(e)}"
    return result


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

        result = f"Descarga completada de {nombre_playlist}"

        return result
    except Exception as e:
        result = f"Ocurrió un error: { str(e)}"
        return result
