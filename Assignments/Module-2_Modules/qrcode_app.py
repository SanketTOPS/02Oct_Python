import pyqrcode

url="tops-int.com"

qr=pyqrcode.create(url)

qr.png("tops.png")