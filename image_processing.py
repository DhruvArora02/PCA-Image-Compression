import numpy as np
import matplotlib.pyplot as plt

def project_image(image, U):
    projection = np.dot(U.T, image)
    reconstructed = np.dot(U, projection)
    return reconstructed

def display_image(orig, proj):
    orig_image = orig.reshape(64, 64)
    proj_image = proj.reshape(64, 64)
    fig, (ax1, ax2) = plt.subplots(figsize=(9, 3), ncols=2)
    ax1.imshow(orig_image, cmap='gray', aspect='equal')
    ax1.set_title('Original')
    plt.colorbar(ax1.imshow(orig_image, cmap='gray'), ax=ax1)
    ax2.imshow(proj_image, cmap='gray', aspect='equal')
    ax2.set_title('Projection')
    plt.colorbar(ax2.imshow(proj_image, cmap='gray'), ax=ax2)
    return fig, ax1, ax2

def perturb_image(image, U, sigma):
    projection = project_image(image, U)
    noise = np.random.normal(0, sigma, projection.shape)
    perturbed_projection = projection + noise
    reconstructed_image = np.dot(U, perturbed_projection)
    return reconstructed_image

def combine_image(image1, image2, U, lam):
    combined_image = lam * image1 + (1 - lam) * image2
    projection = project_image(combined_image, U)
    return projection
