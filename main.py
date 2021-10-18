import os
from generator import qr_code


if __name__ == '__main__':
    url = "https://www.google.co.kr/search?q=qrcode"
    img = qr_code(url)

    img_format = "png"
    img_name = "test"
    img_file = f"{os.getcwd()}/{img_name}.{img_format}"

    img.save(img_file, format=img_format)
