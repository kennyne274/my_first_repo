import qrcode
from PIL import Image


url = 'https://www.google.com'
QRcode = qrcode.QRCode(error_correction = qrcode.constants.ERROR_CORRECT_H)
QRcode.add_data(url)
QRcode.make()

QRcolor = "#E504E5"
QRimg = QRcode.make_image(fill_color = QRcolor, back_color = 'white').convert('RGB')

# Path to your logo image
logoUrl = "apple.png" 
# Open the logo image using PIL
try:
    logo = Image.open(logoUrl)
except FileNotFoundError:
    print("Logo file not found..")
    exit()

# Resize the logo to a reasonable size
base_width = QRimg.size[0] // 4
width_percent = base_width / logo.size[0]
new_height = int(logo.size[1] * width_percent)

logo = logo.resize((base_width, new_height), Image.Resampling.LANCZOS)

# Calculate center position so the logo sits in the middle of the QR
center_x = (QRimg.size[0] - logo.size[0]) // 2
center_y = (QRimg.size[1] - logo.size[1]) // 2

# Paste the logo onto the QR code imag
QRimg.paste(logo, (center_x, center_y))

QRimg.save('test3.png')
QRimg.show(
