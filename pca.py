import numpy as np
from scipy.linalg import eigh

def load_and_center_dataset(filename):
    dataset = np.load(filename)
    centered_dataset = dataset - np.mean(dataset, axis=0)
    return centered_dataset

def get_covariance(dataset):
    n = dataset.shape[0]
    covariance_matrix = (1 / (n - 1)) * np.dot(dataset.T, dataset)
    return covariance_matrix

def get_eig(S, m):
    eigvals, eigvecs = eigh(S)
    sorted_indices = np.argsort(eigvals)[::-1]
    top_m_indices = sorted_indices[:m]
    top_m_eigvals = eigvals[top_m_indices]
    top_m_eigvecs = eigvecs[:, top_m_indices]
    eigval_matrix = np.diag(top_m_eigvals)
    return eigval_matrix, top_m_eigvecs

def get_eig_prop(S, prop):
    eigen_vals, eigen_vecs = eigh(S)
    return select_eigenvalues_by_prop(eigen_vals, eigen_vecs, prop)

def select_eigenvalues_by_prop(eigen_vals, eigen_vecs, prop):
    sorted_indices = np.argsort(eigen_vals)[::-1] 
    sorted_eigen_vals = eigen_vals[sorted_indices]
    total_variance = np.sum(sorted_eigen_vals)
    selected_indices = np.where(sorted_eigen_vals > (prop * total_variance))[0]
    selected_eigen_vals = np.diag(sorted_eigen_vals[selected_indices])
    selected_eigen_vecs = eigen_vecs[:, sorted_indices[selected_indices]]
    return selected_eigen_vals, selected_eigen_vecs
