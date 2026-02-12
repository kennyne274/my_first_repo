# pip install qrcode[pil]

# Import the library we need to create QR codes
import qrcode

# The web address (URL) you want to put inside the QR code
data = "https://www.google.com/"

# Actually create the QR code image from the data (URL)
img = qrcode.make(data)

# Save the created QR code as a file named "myqr.png"
img.save("myqr.png")
