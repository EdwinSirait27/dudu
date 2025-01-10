import yt_dlp

def download(playlist_url, save_path="downloads"):
    ydl_opts = {
        'outtmpl': f'{save_path}/%(playlist_index)s - %(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'noplaylist': False,
        'playlist_items': '1-',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

# Contoh penggunaan
playlist_url = input("Masukkan URL playlist YouTube: ")
download(playlist_url)


# from pytube import Playlist
# import os

# def download_playlist(url, output_folder="downloads"):
#     playlist = Playlist(url)
#     print(f"Downloading playlist: {playlist.title}")
    
#     # Buat folder output jika belum ada
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     for video in playlist.videos:
#         print(f"Downloading: {video.title}")
#         video.streams.get_highest_resolution().download(output_folder)
    
#     print("Download selesai.")

# if __name__ == "__main__":
#     # Contoh URL playlist (ganti dengan URL playlist lain jika perlu)
#     playlist_url = "https://youtube.com/playlist?list=PLFIM0718LjIW-XBdVOerYgKegBtD6rSfD&si=-fMifhX8zH_u-BRO"
    
#     folder = input("Masukkan folder output (default: 'downloads'): ") or "downloads"
#     download_playlist(playlist_url, folder)
