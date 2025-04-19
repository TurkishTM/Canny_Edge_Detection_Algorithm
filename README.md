# Canny Edge Detection Algorithm

**Team Members**
Ali Turkey, Ahmed Mohamed Maher, Ahmed Walid

Edge detection is a fundamental technique in image processing used to identify boundaries within images. The Canny edge detection algorithm, developed by John F. Canny in 1986, is one of the most widely used methods due to its effectiveness and reliability.

## Key Features

The Canny algorithm is a multi-step process designed to detect edges accurately while reducing noise and false detections. Here’s a closer look at its key components:

- **Gaussian Smoothing**: Applies a Gaussian blur to the image to reduce noise. This step is critical because edge detection is highly sensitive to noise, and smoothing ensures more reliable results.
- **Gradient Calculation**: Uses filters (e.g., Sobel) to compute the intensity gradient of the image. The gradient magnitude and direction highlight areas of rapid intensity change, indicating potential edges.
- **Non-Maximum Suppression**: Refines the edges by suppressing non-maximum gradient values. Only the strongest edge pixels in the gradient direction are kept, resulting in thinner, more precise edges.
- **Double Thresholding**: Applies two thresholds (low and high) to classify edges. Pixels with gradient values above the high threshold are strong edges, those between the low and high are weak, and those below the low are discarded.
- **Edge Tracking by Hysteresis**: Links weak edges to strong ones if they are connected, ensuring continuous edges. This step eliminates weak edges that aren’t part of a larger structure, enhancing edge continuity.

These steps collectively enable the Canny algorithm to produce sharp, clean edges with minimal noise interference, making it stand out among edge detection methods.

## Advantages

According to the research paper "A Survey of Image Processing and Identification Techniques," the Canny algorithm offers several benefits:

- **Less sensitive to noise**: Effectively handles noisy images, reducing false edge detections.
- **Adaptive to different image conditions**: Adjusts to various image types and qualities.
- **Detects sharper edges**: Outperforms other methods in identifying precise edges.

## Disadvantages

The research paper does not highlight any specific disadvantages of the Canny algorithm. It does mention a general challenge in edge detection: accurately detecting edges of most objects in an image can be difficult, but this is not unique to the Canny method.
