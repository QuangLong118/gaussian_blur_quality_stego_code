import cv2
import numpy as np
from scipy.signal import convolve2d
import sys

def unsharp_mask_gaussian(input_path, output_path, ksize=3, sigma=0, amount=1.5):
    img = cv2.imread(input_path)
    blurred = cv2.GaussianBlur(img, (ksize, ksize), sigma)
    sharpened = cv2.addWeighted(img, 1 + amount, blurred, -amount, 0)
    cv2.imwrite(output_path, sharpened)
    print(f"Sharpened with Unsharp Mask: '{output_path}'")

try:
    blur_path = sys.argv[1]
    recovery_path = sys.argv[2]
    unsharp_mask_gaussian(blur_path,recovery_path)
except :
    print("Invalid!")