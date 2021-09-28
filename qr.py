import pyqrcode
import png

str = "https://www.youtube.com/watch?v=-Ra6hmW9Iew"

url = pyqrcode.create(str)
url.png ("myqrcode.png",scale = 20)