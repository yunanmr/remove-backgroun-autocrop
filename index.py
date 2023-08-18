from rembg import remove
from autocrop import Cropper
from PIL import Image
import os

cropper = Cropper(width=400, height=470, face_percent=1)

input_folder = 'input'
output_folder = 'output'
cropped_folder = 'cropped'
files = os.listdir(input_folder)
index = 0
while index < len(files):
    filename = files[index]
    if filename.lower().endswith('.jpg'):
        print(filename)
        input_path  = os.path.join(input_folder, filename)
        cropped_path = os.path.join(cropped_folder, filename)
        new_filename = filename[:-4] + '.png'
        output_path = os.path.join(output_folder, new_filename)

        # Get a Numpy array of the cropped image
        cropped_array = cropper.crop(input_path)

        # Save the cropped image with PIL if a face was detected:
        # if cropped_array:
        cropped_image = Image.fromarray(cropped_array)
        cropped_image.save(cropped_path)

        input = Image.open(cropped_path) # load image
        output = remove(input) # remove background
        output.save(output_path) # save image
        os.remove(input_path)
        os.remove(cropped_path)
    
    if filename.lower().endswith('.png'):
        print(filename)
        input_path  = os.path.join(input_folder, filename)
        cropped_path = os.path.join(cropped_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Get a Numpy array of the cropped image
        cropped_array = cropper.crop(input_path)

        # Save the cropped image with PIL if a face was detected:
        # if cropped_array:
        cropped_image = Image.fromarray(cropped_array)
        cropped_image.save(cropped_path)

        input = Image.open(cropped_path) # load image
        output = remove(input) # remove background
        output.save(output_path) # save image
        os.remove(input_path)
        os.remove(cropped_path)
    index += 1
