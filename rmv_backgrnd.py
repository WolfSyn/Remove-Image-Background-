from rembg import remove
from PIL import Image

# This applicaiotion is ment for removing image backgrounds
# Please choose an image of your choide to remove background 
# Make sure that your path exists & that you have image saved!

input_path = 'Insert you Image Here' #replace with actaul path of your images 
output_path = 'Insert your Image Here Again' #replace with actual path of your images

inp = Image.open(input_path)

output =remove(inp)
output.save(output_path)
image.open("Insert Image Path Here") # replace with actual path of your images in 'output_path'


# Note: The above code uses the "rembg" library to remove background from images.
