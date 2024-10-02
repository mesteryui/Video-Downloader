#!/usr/bin/python3 

from pytube import YouTube

def main():
    destination = "Descargas/" 
    link = input("Enter the link: ")
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    print("Downloading... " + yt.title)
    ys.download(destination)
    x = input("Do you want only the audio:")
    
        



if __name__ == "__main__":
    main()
