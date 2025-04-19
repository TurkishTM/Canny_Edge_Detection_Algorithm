# Canny Edge Detection Module

This Python module implements the Canny edge detection algorithm, a widely used method for identifying edges in images. The algorithm is particularly effective for applications like plant disease detection and agricultural monitoring, as it can detect sharp edges with low sensitivity to noise. This implementation includes enhancements such as automatic threshold selection and edge tracking by hysteresis, making it more accurate and adaptable for various image types, including leaf images.

## Features

- **Gaussian Smoothing**: Reduces image noise using a Gaussian filter.
- **Gradient Calculation**: Computes image gradients using Sobel filters to find edge strength and direction.
- **Non-Maximum Suppression**: Thins edges by suppressing pixels that are not local maxima in the gradient direction.
- **Double Thresholding with Automatic Selection**: Identifies strong and weak edges using adaptive thresholds based on image content.
- **Edge Tracking by Hysteresis**: Connects weak edges to strong edges to form a complete edge map.
- **Simplified Usage**: The module is easy to use with minimal configuration, and thresholds are automatically computed if not provided.

## Installation

To use this module, you need Python 3.6+ and the following libraries:

- `numpy`
- `scipy`
- `scikit-image` (for image I/O and color conversion)

Install the required libraries using pip:

```bash
pip install numpy scipy scikit-image
```

## Usage

1. **Import the Module**: Save the code as `canny_edge.py` and import the `canny_edge` function in your Python script.

2. **Load and Preprocess the Image**: Use `skimage.io.imread` to load the image and convert it to grayscale using `skimage.color.rgb2gray`.

3. **Apply Canny Edge Detection**: Call the `canny_edge` function with the grayscale image. You can optionally specify `sigma`, `th1`, and `th2`.

4. **Save or Display Results**: The function returns the Gaussian-smoothed image, gradient magnitude, and the final edge map. Save or display these as needed.

### Example

```python
from canny_edge import canny_edge
import skimage.io as io
import skimage.color as color

# Load and convert image to grayscale (float values between 0 and 1)
img = io.imread('path/to/your/image.jpg')
img = color.rgb2gray(img)

# Apply Canny edge detection with automatic thresholds
gauss, magnitude, final_edges = canny_edge(img, sigma=3)

# Save the final edge map
io.imsave('edges.jpg', final_edges)
print("Edge detection complete. The final edge map is saved as 'edges.jpg'.")
```

### Parameters

- `img`: 2D NumPy array representing the grayscale image (float values between 0 and 1).
- `sigma`: Standard deviation for the Gaussian filter (default: 3). Controls the amount of smoothing.
- `th1`: Lower threshold for weak edges (default: None, computed as 0.4 * `th2`).
- `th2`: Upper threshold for strong edges (default: None, set to the 70th percentile of gradient magnitudes).

If `th1` and `th2` are not provided, they are automatically calculated based on the image's gradient magnitudes, making the algorithm adaptive to different images.

## Algorithm Steps

1. **Gaussian Smoothing**: The image is smoothed using a Gaussian filter to reduce noise.
2. **Gradient Calculation**: Sobel filters are applied to compute the gradient magnitude and direction.
3. **Non-Maximum Suppression**: Edges are thinned by suppressing pixels that are not local maxima in the direction of the gradient.
4. **Double Thresholding**: Pixels are classified as strong edges (above `th2`), weak edges (between `th1` and `th2`), or non-edges (below `th1`).
5. **Edge Tracking by Hysteresis**: Weak edges connected to strong edges are included in the final edge map, ensuring continuity.

## Important Output

The most critical output is the **final edge map** (`final_edges`), which is a binary image (0 or 255) showing the detected edges after hysteresis. This map is essential for applications like leaf boundary detection and plant disease analysis.

### Example Output Files

- `gauss.jpg`: Gaussian-smoothed image (for reference).
- `magnitude.jpg`: Gradient magnitude image (for reference).
- `edges.jpg`: Final edge map (primary result).

## Notes

- **Input Image**: The input should be a grayscale image with float values between 0 and 1. If using a uint8 image (0-255), normalize it with `img = img / 255.0`.
- **Thresholds**: Automatic threshold selection uses the 70th percentile of non-zero gradient magnitudes for `th2` and 0.4 * `th2` for `th1`. These values can be adjusted manually if needed.
- **Performance**: The algorithm is efficient for most images but may be slower for very large images due to the hysteresis step. Optimizations can be explored for specific use cases.

## Alignment with Research

This implementation is informed by the research paper "A Survey of Image Processing and Identification Techniques" by Ali Turkey et al., which highlights the effectiveness of the Canny algorithm for leaf image analysis. The enhancements, such as automatic thresholding and hysteresis, improve the algorithm's accuracy and adaptability, making it well-suited for applications like plant disease detection.

## License

This code is provided under the MIT License. See the `LICENSE` file for details.