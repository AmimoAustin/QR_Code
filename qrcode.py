# part A - encoding a QRCode
import qrcode  # library for encoding a qrcode

from pyzbar.pyzbar import decode  # two libraries used for decoding a qrcode
from PIL import Image  # 'pip install pillow, to install the PIL library

data = "Don't forget to subscribe"

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='red', back_color='white')

img.save('C:/Users/Azimuthal/Desktop/python resources/myqrcode.png')

# img = qrcode.make(data)

# img.save('C:/Users/Azimuthal/Desktop/python resources/myqrcode.png')  # this is a copied path from the pc
# change backslash to forward slash whenever working with python directories


# part B - decoding a QRCode
# to decode a qrcode (extract data) use a python library called pyzbar ('pip install pyzbar')


img = Image.open('C:/Users/Azimuthal/Desktop/python resources/myqrcode.png')

result = decode(img)

print(result)
