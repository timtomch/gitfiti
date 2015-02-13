# Convert a 4-color PNG image into a textfile suitable for use
# with gitfiti.py
# For the time being, this will only work if the image is exactly
# 52 pixels wide and 7 pixels high and if the four colors used
# are the colors listed in the colormap below.
#
# For use with gitfiti.py by Eric Romano (@gelstudios)
# https://github.com/gelstudios/gitfiti

from PIL import Image

print "Enter image to be converted (PNG):"
imgpath = raw_input('> ')

# Load the image
pngimg = Image.open(imgpath)
pixels = pngimg.load() # this is not a list, nor is it list()'able
width, height = pngimg.size

## TODO: handle images larger than 52x7

## TODO: insert ability to load custom colormap
colormap = {"#d6e685":1,
                "#8cc665":2,
                "#44a340":3,
                "#1e6823":4,
                "#000000":0,
}
## TODO: handle colors that are not in the colormap

# Loop through all pixels
all_pixels = []
for y in range(height):
    line_pixels = []
    for x in range(width):
        rgbpixel = pixels[x, y]
		# Convert to hex
        hexpixel = '#%02x%02x%02x' % rgbpixel[0:3]
		# Convert to 0-4 map
        numpixel = colormap[hexpixel]
        line_pixels.append(numpixel)
    all_pixels.append(line_pixels)

## TODO: output in the format needed by gitfiti
print all_pixels