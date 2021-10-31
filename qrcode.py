# qrcode

import qrcode

data = "GeeksforGeeks"

img = qrcode.make(data)
  
# Saving as an image file
img.save('MyQRCode1.png')


from PIL import Image
  
filename = "image.png"
with Image.open('MyQRCode1.png') as image:
    width, height = image.size
