from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Add a watermark to all images in a folder

# Set up the folder paths
INPUT_FOLDER = Path("images")  # "images" folder in the current directory
OUTPUT_FOLDER = Path("watermarked")

# Create the output folder if it doesn't exist
OUTPUT_FOLDER.mkdir(exist_ok=True)

# Watermark settings
WATERMARK_TEXT = "Hello World"

FONT_PATH = r"C:\Windows\Fonts\arialbd.ttf"  # Arial Bold font
FONT_SIZE = 60  # Font size
ROTATE_ANGLE = 20  # Rotation angle for the watermark

# Supported image file extensions
IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png"]

# Add a watermark to an image
def add_watermark(image_path):

    image = Image.open(image_path).convert("RGBA")
    overlay = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    # Calculate the text size
    bbox = draw.textbbox((0, 0), WATERMARK_TEXT, font=font)

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (image.width - text_width) // 2
    y = (image.height - text_height) // 2

    # Draw the watermark text
    draw.text(
        (x, y),                      
        WATERMARK_TEXT,              
        font=font,                  
        fill=(255, 255, 255, 70)     
    )
  
    overlay = overlay.rotate(ROTATE_ANGLE)
  
    watermarked = Image.alpha_composite(image, overlay)
    watermarked.show()

    output_path = OUTPUT_FOLDER / image_path.name

    watermarked.convert("RGB").save(output_path)

    print(f"[DONE] {image_path.name}")

# Process all images in the folder
def process_images():

    print("\n=== Watermark Process Start ===\n")

    for image_path in INPUT_FOLDER.iterdir():
        if image_path.is_file():
            if image_path.suffix.lower() in IMAGE_EXTENSIONS:
                add_watermark(image_path)  # Add a watermark

    print("\n=== All Images Processed ===")

# Main
if __name__ == "__main__":
    process_images()
  
