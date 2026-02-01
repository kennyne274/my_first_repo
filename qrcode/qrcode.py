import qrcode
import os

# Get the data to encode in the QR code
data = input("Enter the content for the QR code: ").strip()

if not data:
    print("No data was entered.")
else:
    # Ask user for desired filename 
    filename = input("Enter desired filename (without .png - it will be added automatically): ").strip()

    # Build full file path in the current working directory
    file_path = os.path.join(os.getcwd(), f"{filename}.png")

    # Create QR code instance
    qr = qrcode.QRCode(
        version=None,                      # Let the library choose the version automatically
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # ~15% error correction capability
        box_size=10,                       # Size of each box in pixels
        border=4,                          # Thickness of the border (quiet zone)
    )

    # Add data and generate the QR code matrix
    qr.add_data(data)
    qr.make(fit=True)                      # Automatically adjust version to fit the data

    # Create image (custom color + white background)
    img = qr.make_image(fill_color="#9D00FF", back_color="white")

    # Save the image to file
    img.save(file_path)

    print("QR code saved successfully!")
    print("Location:", os.getcwd())
    print(f"File: {file_path}")

