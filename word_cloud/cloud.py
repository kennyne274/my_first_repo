from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

# Windows
font_path = "C:/Windows/Fonts/arial.ttf"

text = """
Artificial intelligence is changing the way people work, learn, create, and communicate.
By analyzing large amounts of information, AI can recognize patterns, generate ideas,
understand language, and assist people with complex problems.

Modern AI systems can learn from examples and improve their performance as they process
new information. They are being used in education, science, healthcare, business,
transportation, entertainment, and many other areas of everyday life.

AI is not simply a machine that replaces human effort.
It can also become a powerful tool that extends human creativity, knowledge, and decision-making.

The most important question is not whether machines will become intelligent,
but how humans will choose to use that intelligence.

As artificial intelligence continues to develop, society will need to think carefully
about responsibility, privacy, fairness, creativity, and the relationship between humans and machines.

The future of AI will ultimately depend on the choices people make today.
"""


# Load the Korea map image
icon = Image.open("korea_map.png")

# Convert the image into a NumPy array
korea_mask = np.array(icon)

# Create the WordCloud 
wc = WordCloud(
    background_color="white",
    width=1000,
    height=700,
    font_path=font_path,
    mask=korea_mask
)

img_wordcloud = wc.generate(text)

# Extract colors from the original Korea map image
image_colors = ImageColorGenerator(korea_mask)

img_wordcloud = img_wordcloud.recolor(
    color_func=image_colors
)


# Display the WordCloud
plt.figure(figsize=(10, 7))
plt.imshow(img_wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
