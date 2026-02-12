# 1. Import the library needed to create QR codes
import qrcode

# 2. The data that you want to store inside the QR code
data = "https://www.naver.com"

# 3. Create a QRCode object 
qr = qrcode.QRCode(
    version=1,                    # Controls the size of the QR code (1 = smallest)
    box_size=10,                  # Size of each small square
    border=5,                     # Thickness of the white border around the QR code 
    error_correction=qrcode.constants.ERROR_CORRECT_M   # How much damage the QR can survive
)

# 4. Put the data into the QR code object
qr.add_data(data)

# 5. Generate the QR code pattern
#    fit=True means: automatically choose the smallest version that can hold the data
qr.make(fit=True)

# 6. Turn the QR code into an actual image with custom colors
img = qr.make_image(
    fill_color="#025C6C",     # Color of the QR pattern
    back_color="white"        # Background color
)

# 7. Save the image to a file
img.save("myqr02.png")
