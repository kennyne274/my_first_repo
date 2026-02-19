
import qrcode

data = "https://www.naver.com"

# Create qrcode object
qr = qrcode.QRCode(
    version=1,                   
    box_size=10,                 
    border=5,                    
    error_correction=qrcode.constants.ERROR_CORRECT_M  
)


qr.add_data(data)

qr.make(fit=True)


img = qr.make_image(
    fill_color="#025C6C",     
    back_color="white"      
)

# Save the image to a file
img.save("myqr02.png")
