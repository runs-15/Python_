import pafy         # modul untuk interaksi dengan YouTube
import locale       # modul untuk membuat delimiter angka agar mudah dibaca
import clipboard    # modul untuk copy link url ke clipboard
import os           # modul pause commandprompt, bila dieksekusi nantinya
import requests     # modul untuk mendownload file dari link
import tqdm         # modul untuk membuat proggress bar dari proses download

url = input("Masukkan link konten youtube yang ingin anda unduh : ")
video = pafy.new(url)
locale.setlocale(locale.LC_ALL, '')

def convert_bytes(num):
    # this function will convert bytes to MB.... GB... etc
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

streams = video.streams
best = video.getbest()

print("Judul                : {}".format(video.title))
print("Channel              : {}".format(video.author))
print("Durasi video         : {}".format(video.duration))
print("Jumlah ditonton      : {0:n}".format(video.viewcount))
if video.likes != None:
    print("Disukai oleh         : {0:n}".format(video.likes))
if video.dislikes != None:
    print("Tidak disukai oleh   : {0:n}".format(video.dislikes))
print("Ukuran video         : {}".format(convert_bytes(best.get_filesize())))
klip = input("Simpan link ke clipboard? y/n ")
if klip.upper() == 'Y':
    clipboard.copy(best.url)
else:
    print("\nLink direct          : {}".format(best.url))

konfirmasi = input("\nKetik Y untuk mengunduh file... : ")

if konfirmasi.upper() == 'Y':
    chunk_size = 1024
    alamat = best.url
    r = requests.get(alamat, stream = True)
    total_size = int(r.headers['content-length'])
    with open(video.title+".mp4", 'wb') as f:
        for data in tqdm.tqdm(iterable = r.iter_content(chunk_size = chunk_size), total = int(total_size/chunk_size), unit = 'KB', colour='green'):
            f.write(data)
    print("Unduhan Selesai!!!")
    os.system("pause")

    #konfirmasi = input("\nKetik Y untuk mengunduh file... : ")
    #if konfirmasi.upper() == 'Y':
    #    best.download(quiet=False)
    #    print("Unduhan Selesai!!!")
    #    os.system("pause")
else:
    print("Selamat tinggal!")
    os.system("pause")