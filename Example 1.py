import numpy as np
import matplotlib.pyplot as plt

def dft2d(x):
    M, N = x.shape
    X = np.zeros((M, N), dtype=np.complex128)
    
    for u in range(M):
        for v in range(N):
            for m in range(M):
                for n in range(N):
                    X[u, v] += x[m, n] * np.exp(-2j * np.pi * ((u * m) / M + (v * n) / N))
    
    return X / np.sqrt(M * N)

def shift_spectrum(X):
    M, N = X.shape
    return np.fft.fftshift(X, axes=(0, 1))

# Example 1: Symmetric Binary Pattern
symmetric_binary = np.array([[0, 1, 1, 0],
                             [1, 0, 0, 1],
                             [1, 0, 0, 1],
                             [0, 1, 1, 0]])

# Compute 2D DFT
X_symmetric = dft2d(symmetric_binary)

# Shift the spectrum
shifted_spectrum_symmetric = shift_spectrum(np.abs(X_symmetric))

# Plotting
plt.figure(figsize=(6, 6))
plt.imshow(np.log10(shifted_spectrum_symmetric + 1), cmap='gray')  # Log scale for better visualization
plt.title('2D DFT of Symmetric Binary Pattern')
plt.colorbar(label='Log Magnitude')
plt.axis('off')
plt.show()
