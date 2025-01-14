import numpy as np
from pca import load_and_center_dataset, get_covariance, get_eig
from image_processing import display_image, perturb_image

# Example usage:
dataset = load_and_center_dataset('your_dataset.npy')
covariance_matrix = get_covariance(dataset)
eigvals, eigvecs = get_eig(covariance_matrix, m=50)

# Process image
image = np.random.rand(64 * 64)  # example image as a vector
projected_image = perturb_image(image, eigvecs, sigma=0.1)
display_image(image, projected_image)
