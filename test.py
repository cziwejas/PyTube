from pytube import YouTube

function_patterns = [

    r'a\.[A-Z]&&\(b=a\.get\("n"\)\)&&\(b=([^(]+)\(b\)',
]

url = 'https://www.youtube.com/watch?v=dSPiDFZmAnQ'

yt = YouTube(url)

yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename='Pobrane.mp4')
