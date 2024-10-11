import os
from dotenv import load_dotenv
from novita_client import NovitaClient
from novita_client.utils import base64_to_image
from PIL import Image
from base64 import b64encode
import io

def resize_img(width, height, target):
    # This function used to give a size that less then the maximum size that allowed 
    scale_factor = min(target / width, target / height)
    width *= scale_factor
    height *= scale_factor
    return round(width), round(height)

def image(image_path):
    # Open and resize the images
    img = Image.open(os.path.normpath(image_path)) # This will convert the user input to binary
    width,height = resize_img(img.size[0],img.size[1],1024)
    new_img = img.resize((width,height),Image.LANCZOS) # LANCZOS is the best resampling in term of image quality
    
    # Create buffer to store image so that we don't need to store the resized images
    buffer = io.BytesIO()
    new_img.save(buffer,format="jpeg")

    # Encode value in buffer to base 64 binary and then decode to string
    image = b64encode(buffer.getvalue()).decode("utf-8")
    return image

def main():
    # Receive the PATH of images folder and destination folder
    folder_path = os.path.normpath(input("Your folder images PATH: ").replace('"',"")) # replace "" if the user copy the PATH
    destination_path = os.path.normpath(input("Destination PATH (you need to create new folder): ").replace('"',""))
    listdir = os.listdir(folder_path)

    for image_path in listdir:
        img = image(os.path.join(folder_path,image_path))
        try:
            #Load the Api_key and run the client
            load_dotenv(".env")
            Api_key = os.getenv("API") 
            client = NovitaClient(Api_key)
            res = client.remove_text(
                image= img
            )

            # Save the images
            base64_to_image(res.image_file).save(os.path.join(destination_path,image_path))
        except Exception as e:
            print(f"There's an error: {e}")
        else:
            print(f"text in {image_path} successfuly removed")

if __name__ == '__main__':
    main()