import cv2
import numpy as np
from scipy.signal import convolve2d
import sys

def wiener_deblur_image(input_path, output_path, ksize=3, sigma=0, K=0.01):
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    img = img.astype(np.float32) / 255.0

    # Tạo kernel Gaussian chuẩn
    psf_1d = cv2.getGaussianKernel(ksize, sigma)
    psf = psf_1d @ psf_1d.T
    psf /= psf.sum()

    # FFT
    img_fft = np.fft.fft2(img)
    psf_fft = np.fft.fft2(psf, s=img.shape)
    psf_fft_conj = np.conj(psf_fft)

    # Wiener deconvolution
    deblur_fft = (psf_fft_conj / (np.abs(psf_fft) ** 2 + K)) * img_fft
    deblur = np.fft.ifft2(deblur_fft).real

    deblur = np.clip(deblur * 255, 0, 255).astype(np.uint8)
    cv2.imwrite(output_path, deblur)
    print(f"[+] Đã khử mờ bằng Wiener Filter: '{output_path}'")

try:
    blur_path = sys.argv[1]
    recovery_path = sys.argv[2]
    wiener_deblur_image(blur_path,recovery_path)
except :
    print("Invalid!")