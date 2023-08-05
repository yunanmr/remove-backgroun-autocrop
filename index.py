from rembg import remove
from autocrop import Cropper
from PIL import Image

cropper = Cropper(width=400, height=470, face_percent=1)

input_path = 'input.jpg' # input image path
cropped_path = 'cropped.jpg' # cropped image path
output_path = 'output.png' # output image path

# Get a Numpy array of the cropped image
cropped_array = cropper.crop(input_path)

# Save the cropped image with PIL if a face was detected:
# if cropped_array:
cropped_image = Image.fromarray(cropped_array)
cropped_image.save(cropped_path)

input = Image.open(cropped_path) # load image
output = remove(input) # remove background
output.save(output_path) # save image