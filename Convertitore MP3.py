# Convertitore da File Audio a MP3

from pydub import AudioSegment
import os

def converti(file):

    mp4_file = file
    mp3_file = file.split('.')[-2]+'.mp3'

    sound = AudioSegment.from_file(mp4_file)
    sound.export(mp3_file, format="mp3", bitrate="128k")

# AVVIO
print('\||| Convertitore di Audio da MP4 a MP3 |||/')
print()

# CARICO I FILE DA CONVERTIRE
print('Inserisci i file da convertire')
folder_path = input('Path: ')
folder_path = folder_path.replace('\\', '')
print('Cerco i file da convertire in: ' + folder_path)
print()

# INDIVIDUO I SINGOLI FILE AUDIO E LI CONVERTO
for file in os.listdir(folder_path):
    if file.split('.')[-1] in ('mp4', 'wav'):
        file_path = folder_path + '/' + file
        print('Preparo ' + file_path)
        print('Conversione...')
        try:
            converti(file_path)
            os.remove(file_path) # ELIMINO IL FILE MP4
        except:
            print('Fallito\n')
        else:
            print('Conversione avvenuta con successo!\n')

# CHIUSURA
print()
print('Bye Bye! :)')
print('\||| Convertitore di Audio in MP3 |||/')
