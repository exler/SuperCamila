import os

import discord
import youtube_dl
import urllib.parse

from utils import log


def url_validator(url: str) -> bool:
    """Validate if a given string is a URL"""
    try:
        result = urllib.parse.urlparse(url)
        return all([result.scheme, result.netloc, result.path])
    except:
        return False


def youtube_download(query) -> dict:
    """Downloads a given URL from YouTube using youtube-dl.
       Returns dict if success, otherwise None"""
    ytdl_opts = {
        "quiet": "True",
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "outtmpl": os.path.join(
            os.path.abspath(os.getcwd()), "data", "audio", "%(title)s.%(ext)s"
        ),
    }

    with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
        if url_validator(query):
            result = ytdl.extract_info(query)
        else:
            result = ytdl.extract_info(f"ytsearch:{query}")["entries"][0]
        title = result.get("title", None)
        duration = result.get("duration", None)
        # log.debug(f"Downloading YouTube audio, title: {title}")

    if not title:
        return None

    return {"title": title, "duration": duration}
