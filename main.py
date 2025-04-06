import sys
import datetime
import qrcode
import os

now = datetime.datetime.now()
fnow = now.strftime("%H%M%S")

with open("main.py", 'r') as file:
    file.seek(0, os.SEEK_END)
    dosya_boyutu = file.tell()
    if dosya_boyutu > 0:
        file.seek(dosya_boyutu - 1)
        endsss = int(file.read(1))
    else:
        endsss = 0

def generate(_text, _name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=50,
        border=1
    )
    qr.add_data(_text)
    qr.make(fit=True)
    image = qr.make_image(fill='black', back_color='white')

    directory = os.path.dirname(_name)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    image.save(_name)

try:
    if len(sys.argv) == 3:
        generate(sys.argv[1], sys.argv[2] + ".png")
    elif len(sys.argv) == 2:
        # generate(sys.argv[1], f"qr-code_{fnow}.png")
        generate(sys.argv[1], f"qr-code_{endsss}.png")

        with open("main.py", 'r+') as file:
            file.seek(0, os.SEEK_END)
            dosya_boyutu = file.tell()

            if dosya_boyutu > 0:
                file.seek(dosya_boyutu - 1)
                file.write(str(endsss + 1))
            else:
                file.write(str(endsss + 1))

    else:
        print("eksik arguman")
except:
    print("hata")
1
