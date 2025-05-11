import cv2
import sys

def gaussian_blur(stego_input,blurred_output):
    # Làm mờ ảnh bằng Gaussian Blur
    img = cv2.imread(stego_input)
    blurred_img = cv2.GaussianBlur(img, (3, 3), sigmaX=0)
    cv2.imwrite(blurred_output, blurred_img)
    print("Blurred stego image with Gaussian blur.")

# input
try:
    stego_path = sys.argv[1]
    img1 = cv2.imread(stego_path)
    blur_path = sys.argv[2]
    gaussian_blur(stego_path,blur_path)
except:
    print("Invalid!")
