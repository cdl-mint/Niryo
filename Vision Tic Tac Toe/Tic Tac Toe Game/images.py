from PIL import Image
import asyncio 
opencv 
filename = "Gewonnen.png"

with Image.open(filename) as img:
    img.load()
    img.show()


