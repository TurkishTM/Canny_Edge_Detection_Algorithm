import numpy as np
from scipy.ndimage import gaussian_filter
from scipy.signal import convolve2d
from collections import deque

def canny_edge(img, sigma=3, th1=None, th2=None):
    """
    Apply Canny edge detection to a grayscale image with automatic thresholding and hysteresis.

    Parameters:
    -----------
    img : 2D array
        Grayscale input image (float values between 0 and 1).
    sigma : float, optional (default=3)
        Standard deviation for Gaussian filter to reduce noise.
    th1 : float, optional (default=None)
        Lower threshold; if None, computed as 0.4 * th2.
    th2 : float, optional (default=None)
        Upper threshold; if None, set to 70th percentile of gradient magnitudes.

    Returns:
    --------
    gauss : 2D array
        Image after Gaussian smoothing.
    magnitude : 2D array
        Gradient magnitude after Sobel filtering.
    final_edges : 2D array
        Final edge map (uint8, 0 or 255) after hysteresis.
    """
    # Step 1: Gaussian smoothing to reduce noise
    gauss = gaussian_filter(img, sigma=sigma)

    # Step 2: Compute gradients using Sobel filters
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    gx = convolve2d(gauss, sobel_x, mode='same', boundary='symm')
    gy = convolve2d(gauss, sobel_y, mode='same', boundary='symm')

    # Step 3: Calculate gradient magnitude and direction
    magnitude = np.sqrt(gx**2 + gy**2)
    theta = np.arctan2(gy, gx) * (180 / np.pi)
    theta[theta < 0] += 180

    # Step 4: Non-maximum suppression to thin edges
    nms = np.copy(magnitude)
    rows, cols = magnitude.shape
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            angle = theta[i, j]
            if (0 <= angle < 22.5) or (157.5 <= angle < 180):
                if not (magnitude[i, j] > magnitude[i, j-1] and magnitude[i, j] > magnitude[i, j+1]):
                    nms[i, j] = 0
            elif 22.5 <= angle < 67.5:
                if not (magnitude[i, j] > magnitude[i-1, j+1] and magnitude[i, j] > magnitude[i+1, j-1]):
                    nms[i, j] = 0
            elif 67.5 <= angle < 112.5:
                if not (magnitude[i, j] > magnitude[i-1, j] and magnitude[i, j] > magnitude[i+1, j]):
                    nms[i, j] = 0
            elif 112.5 <= angle < 157.5:
                if not (magnitude[i, j] > magnitude[i-1, j-1] and magnitude[i, j] > magnitude[i+1, j+1]):
                    nms[i, j] = 0

    # Step 5: Automatic threshold selection if not provided
    if th1 is None or th2 is None:
        flat_nms = nms.ravel()
        th2_auto = np.percentile(flat_nms[flat_nms > 0], 70)  # 70th percentile of non-zero magnitudes
        th2 = th2_auto if th2 is None else th2
        th1 = 0.4 * th2 if th1 is None else th1

    # Step 6: Double thresholding and hysteresis
    final_edges = np.zeros_like(nms, dtype=np.uint8)
    strong = nms > th2
    final_edges[strong] = 255
    mask = nms >= th1

    # Hysteresis: Connect weak edges to strong edges
    queue = deque()
    for i in range(rows):
        for j in range(cols):
            if strong[i, j]:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if mask[nx, ny] and final_edges[nx, ny] == 0:
                        final_edges[nx, ny] = 255
                        queue.append((nx, ny))

    return gauss, magnitude, final_edges

if __name__ == "__main__":
    import skimage.io as io
    import skimage.color as color

    # Example usage
    img_path = 'images.jpeg'  # Replace with actual image path
    img = io.imread(img_path)
    img = color.rgb2gray(img)  # Convert to grayscale (0 to 1)

    # Apply Canny edge detection with automatic thresholds
    gauss, magnitude, final_edges = canny_edge(img, sigma=3)

    # Save results
    io.imsave('gauss.jpg', (gauss / gauss.max() * 255).astype(np.uint8))
    io.imsave('magnitude.jpg', (magnitude / magnitude.max() * 255).astype(np.uint8))
    io.imsave('edges.jpg', final_edges)
    print("Edge detection complete. The important result file is 'edges.jpg' (final edge map).")