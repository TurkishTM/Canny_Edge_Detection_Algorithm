# Canny Edge Detection Implementation

A Python implementation of the Canny edge detection algorithm with automatic thresholding and hysteresis-based edge linking.

## Features
- Gaussian noise reduction
- Sobel filter gradient calculation
- Non-maximum suppression
- Automatic threshold selection (70th percentile for high threshold)
- BFS-based hysteresis edge linking

## Usage
```python
from skimage import io, color

# Load image
img = color.rgb2gray(io.imread("input.jpg"))

# Detect edges
gauss, magnitude, edges = canny_edge(img, sigma=3)

# Save results
io.imsave("edges.jpg", edges)

Pros & Cons
Advantages (+)
Accurate edge detection - Multi-stage process reduces false positives

Noise resilience - Gaussian filtering pre-processes image effectively

Automatic thresholds - Defaults work well for most images

Edge continuity - Hysteresis connects weak/strong edges reliably

Parameter flexibility - Adjustable sigma and thresholds

Limitations (-)
Processing speed - Not optimized for real-time applications

Parameter sensitivity - Requires tuning for noisy/low-contrast images

Memory usage - Creates multiple intermediate matrices

Fixed percentile - 70th percentile assumption may not suit all cases

Border artifacts - Edge effects from convolution operations

Dependencies
NumPy

SciPy

scikit-image

Matplotlib (optional for visualization)

