import yt_dlp


def download_video(url):
    ydl_opts = {
        "outtmpl": "video.mp4",  # Ruta de destino del archivo
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("¡Descarga completa!")
    except Exception as e:
        print(f"Error: {e}")


download_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
