import yt_dlp
import pdb

def youtube_movie_downloader(search_keyword):
  keyword_search = search_keyword
  url_to_search = f"ytsearch:{keyword_search}"
  yt_config = {
      'format': 'best',  # Download the best quality
      'noplaylist': True,  # Ensure only a single video is downloaded
  }

  with yt_dlp.YoutubeDL(yt_config) as ydl:
      ydl.download([url_to_search])

keyword_to_search = "super mario movie trailer"
youtube_movie_downloader(keyword_to_search)