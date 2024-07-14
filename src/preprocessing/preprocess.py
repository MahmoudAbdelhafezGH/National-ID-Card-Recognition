import cv2
def convert_to_gray(colored):
    gray_image = cv2.cvtColor(colored, cv2.COLOR_BGR2GRAY) 
    return gray_image

def filter_image(img, diameter = 11, sigmaColor = 21, sigmaSpace = 7):
    blurred = cv2.bilateralFilter(img, diameter, sigmaColor, sigmaSpace)
    return blurred
    