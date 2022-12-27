#! /usr/bin/env python3
# coding=utf-8

from pytube import YouTube, Playlist
import os

#path_folder = '/Users/andreamarinelli/Desktop/'
path_folder = './'

def try_download(formato):
    if formato == '1':
        DownloadAudio(link)
    elif formato == '2':
        DownloadVideo(link)
    elif formato == '3':
        DownloadPlaylist(link)
    else:
        print('Valore non valido\n')
        
def DownloadAudio(link, path=path_folder):
    yt = YouTube(link)
    yt = yt.streams.get_audio_only()

    folder_path = path_folder + 'Musica'
    try:
        os.mkdir(path=folder_path)
        print('path: ' + folder_path)
    except:
        print('path: ' + folder_path)

    try:
        yt.download(output_path=folder_path)
    except:
        print('C\'è stato un errore :(')
    print("Download completato")

def DownloadVideo(link, path=path_folder):
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()

    folder_path = path_folder + 'Video'
    try:
        os.mkdir(path=folder_path)
        print('path: ' + folder_path)
    except:
        print('path: ' + folder_path)
    
    try:
        yt.download(output_path=folder_path)
    except:
        print('C\'è stato un errore :(')
    print("Download completato")

def DownloadPlaylist(link, path=path_folder):
    plst = Playlist(link)

    folder_path = path_folder + plst.title
    os.mkdir(path=folder_path)

    for video in plst.videos:
        video = video.streams.get_audio_only()
        try:
            video.download(output_path=folder_path)
        except:
            print('C\'è stato un errore :(')
        print("Download completato")

# WELCOM MESSAGE
print('||| Youtube Downloader |||\n')

working = True

while working:
    # GET URL
    print('Incolla l\'url del video che vuoi scaricare. Scrivi ESC per uscire')
    link = input('URL: ')

    # (if ESC) GOODBYE MESSAGE
    if link.upper() == 'ESC':
        working = False
        break

    # CHOOSE FORMAT
    print('\nScegli un formato:\n[1] Musica\n[2] Video\n[3] Playlist\n')
    formato = input('formato: ')
    print()
    formato = formato.lower()

    # TRY DOWNLOAD
    try_download(formato)

print('\nGrazie per aver usato YT Downloader. Bye Bye! :)')
print('||| Youtube Downloader |||\n')