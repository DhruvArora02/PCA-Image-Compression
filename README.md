# PCA-Image-Compression

__Project Overview__ -

This project demonstrates the use of Principal Component Analysis (PCA) for image compression and reconstruction. PCA is a statistical technique commonly used in machine learning and image processing to reduce dimensionality, retain significant features, and reconstruct images with reduced data.

In this project, PCA is applied to a dataset of images to analyze the variance in pixel data, extract the most significant eigenvalues and eigenvectors, and compress the data. The goal is to reconstruct the images using fewer principal components and observe the quality of compression and reconstruction.

__Key Features__ -

- Dataset Preprocessing: The images are loaded and centered by subtracting the mean of each pixel across the dataset to ensure that PCA works effectively.

- Covariance Matrix Calculation: The covariance matrix is calculated from the dataset to understand the relationships between pixel values.

- Eigenvalue and Eigenvector Computation: Using the covariance matrix, eigenvalues and eigenvectors are computed to determine the principal components of the data.

- Image Reconstruction: Images are projected into the principal component space and then reconstructed by selecting the most significant components for compression.

- Image Perturbation: Perturbations are added to the image projections to explore the impact of noise on the reconstruction quality.

- Image Combination: Two images are combined using PCA, and the resulting combined image is projected back into the original space.

__Technologies Used__ -

- Python: The primary programming language for data manipulation, PCA implementation, and image processing.

- NumPy: Used for matrix operations, eigenvalue computation, and handling large datasets.

- SciPy: Provides the eigh function for eigenvalue decomposition, which is used to find principal components.

- Matplotlib: Used for visualizing the images and their reconstructions, displaying the original and projected images side by side.

__How It Works__ -

1. Data Loading and Centering: The dataset of images is loaded, and each image is centered by subtracting the mean of all pixels in the dataset to ensure that PCA is applied correctly.

2. Covariance Matrix Calculation: The covariance matrix of the centered data is computed to understand the variance and correlations between the pixels of different images.

3. Eigenvalue and Eigenvector Calculation: Eigenvalues and eigenvectors are computed using the covariance matrix to determine the directions (principal components) that account for the most variance in the dataset.

4. Image Projection and Reconstruction: Images are projected onto the subspace spanned by the top m principal components and reconstructed using fewer components, showing the effect of dimensionality reduction.

5. Perturbation: Gaussian noise is added to the projected image data, and the perturbed data is used to reconstruct the image to analyze the robustness of PCA in handling noisy data.

6. Image Combination: Two images are combined using a weighted average, and PCA is applied to the combined image to explore how merging different images affects the projection and reconstruction.
