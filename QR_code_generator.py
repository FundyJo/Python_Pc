import io

import pyqrcode
import os

link = input("URL: ")

qr_code = pyqrcode.create(link)

qr_code.svg("qr_code.svg", scale=10)
buffer = io.BytesIO()
qr_code.svg(buffer)
print("Done!!")
