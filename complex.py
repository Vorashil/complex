# complex.py

import math
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Use 'Agg' backend for non-GUI image rendering
plt.switch_backend('Agg')

def generate_complex_image(function_str, size=400, x_range=6, threshold=0.0):
    res = np.linspace(-(x_range / 2), x_range / 2, size * 2 + 1)
    ims = np.linspace(-(x_range / 2), x_range / 2, size * 2 + 1)

    coordinates = np.zeros((len(res) - 1, len(ims) - 1), dtype=np.complex128)

    for i in range(-size, size):
        for j in range(-size, size):
            coordinates[i + size, j + size] = complex(ims[i + size], res[j + size])

    # Safely evaluate the function string passed by the user
    def safe_eval_function(z):
        return eval(function_str, {"np": np, "math": math, "z": z})

    nums = safe_eval_function(coordinates)

    phase = np.angle(nums, True)
    magnitude = np.abs(nums)

    H = np.interp(phase, (-180, 180), (0, 360))
    S = 0.7 + (1 / 3) * (np.log(magnitude) / np.log(1.6) - np.floor(np.log(magnitude) / np.log(1.6)))
    V = ((np.abs(np.sin(math.pi * nums.real)) ** threshold) * (np.abs(np.sin(math.pi * nums.imag)) ** threshold)) * 255

    HSV = np.dstack((H, S, V)).astype("float32", copy=False)
    image = np.rot90(cv2.cvtColor(HSV, cv2.COLOR_HSV2BGR) / 255, 3)

    # Save the image as PNG using OpenCV for color transformation
    temp_image_path = "temp_image.png"
    cv2.imwrite(temp_image_path, image * 255)

    # Now, use Matplotlib to add axes, ticks, and labels
    fig, ax = plt.subplots(figsize=(6, 6))  # Ensure the plot is square
    img = cv2.imread(temp_image_path)

    # Add the image to the plot
    ax.imshow(img, extent=[-x_range / 2, x_range / 2, -x_range / 2, x_range / 2])

    # Add axis labels, ticks, and grid
    ax.set_xlabel('Re(z)', fontsize=12)
    ax.set_ylabel('Im(z)', fontsize=12)
    ax.set_title('Complex Function Plot', fontsize=14)

    # Set the limits for the plot to ensure the axis and grid appear correctly
    ax.set_xlim([-x_range / 2, x_range / 2])
    ax.set_ylim([-x_range / 2, x_range / 2])

    # Configure the ticks and grid
    ax.set_xticks(np.linspace(-x_range / 2, x_range / 2, 5))
    ax.set_yticks(np.linspace(-x_range / 2, x_range / 2, 5))
    ax.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)

    # Ensure aspect ratio is square so axes and grid align properly
    ax.set_aspect('equal')

    # Save final image with axis and labels
    output_image_path = "static/complex_function_plot_with_axis.png"
    plt.savefig(output_image_path)

    return output_image_path
