#!/usr/bin/python3 
from gi.repository import GLib
from pathlib import Path
from pytube import YouTube

def main():
    destination = Path(GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DOWNLOAD))
    link = input("Enter the link: ")
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    print("Downloading... " + yt.title)
    ys.download(destination)
    x = input("Do you want only the audio:")
    if x == "Yes" or "yes":
        convert()
        
        



if __name__ == "__main__":
    main()