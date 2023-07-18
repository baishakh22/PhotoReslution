import cv2
from PIL import Image


def increase_resolution(image_path, scale):
    # Read the image using OpenCV
    original = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Get the original image's dimensions
    original_dimensions = original.shape[:2]

    # Calculate the higher resolution dimensions
    higher_res_dimensions = (original_dimensions[1]*scale, original_dimensions[0]*scale)

    # Resize the image
    higher_res = cv2.resize(original, higher_res_dimensions, interpolation = cv2.INTER_LINEAR)

    # Save the image
    cv2.imwrite('higher_res_image.jpg', higher_res)

    # Open and show the image using Pillow
    img = Image.open('higher_res_image.jpg')
    img.show()

# Call the function
increase_resolution('Matter.jpg', 2)  # Replace 'your_image.jpg' with your image's path

