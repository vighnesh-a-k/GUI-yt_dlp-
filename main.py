import yt_dlp
URLS = ["https://youtu.be/nPIOrlO-KM4"]

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now post-processing ...')
  

ydl_opts = {
    
    'progress_hooks': [my_hook],
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    meta = ydl.extract_info(URLS[0], download=False)
    formats=meta.get('formats', [meta])
    for i in range(len(formats)):
        print(formats[i]["format"],formats[i]["resolution"])

    


