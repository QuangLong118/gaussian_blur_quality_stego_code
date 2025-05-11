from skimage import restoration
import numpy as np
import cv2
import sys

def richardson_lucy_deblur(input_path, output_path, ksize=3, sigma=0, iterations=30):
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    img = img / 255.0
    # Tạo kernel Gaussian đúng với kernel làm mờ
    psf_1d = cv2.getGaussianKernel(ksize, sigma)
    psf = psf_1d @ psf_1d.T
    # Áp dụng deconvolution
    deconvolved = restoration.richardson_lucy(img, psf, num_iter=iterations)
    deconvolved = np.clip(deconvolved * 255, 0, 255).astype(np.uint8)
    cv2.imwrite(output_path, deconvolved)
    print(f"Dehazed with Richardson-Lucy: '{output_path}'")

try:
    blur_path = sys.argv[1]
    recovery_path = sys.argv[2]
    print(1)
    richardson_lucy_deblur(blur_path,recovery_path)
except :
    print("Invalid!")



