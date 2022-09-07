from pytube import YouTube
filesize = 1

def get_yt(yt_list):
    while True:
        url = input('Enter video URL:')
        if url == '':
            break
        yt = YouTube(url)
        print(yt.title)
        yt_list.append(yt)

def download(yt_list: list[YouTube]):
    for yt in yt_list:
        print('Downloading: ' + yt.title)
        stream = yt.streams.get_by_itag(22)
        mb = stream.filesize / 1048576
        print('Size: ' + "%.2f" % mb +' megabytes')
        try:
            stream.download()
        except Exception as e:
            print('Could not download:' + yt.title)
            print(e)
            continue
        print('Finished: ' + yt.title)

yt_list: list[YouTube] = []
get_yt(yt_list)
download(yt_list)
print('All downloads completed!')
input('Press enter to exit.')