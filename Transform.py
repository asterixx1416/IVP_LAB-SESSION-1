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

def magnitude_spectrum(X):
    return np.abs(X)

def phase_spectrum(X):
    return np.angle(X)

def shift_spectrum(X):
    M, N = X.shape
    return np.fft.fftshift(X, axes=(0, 1))

def convolution_theorem(x, h):
    # Compute DFT of the input signal and the filter
    X = dft2d(x)
    H = dft2d(h)
    
    # Perform point-wise multiplication in the frequency domain
    Y = X * H
    
    # Compute the inverse DFT to get the convolved result
    y = idft2d(Y)
    
    return np.real(y)

def idft2d(X):
    return np.fft.ifft2(X)

# Example usage with user input:
try:
    rows_x = int(input("Enter the number of rows for the 2D array x: "))
    cols_x = int(input("Enter the number of columns for the 2D array x: "))
    elements_x = []
    for i in range(rows_x):
        row = input(f"Enter space-separated elements for row {i+1} of x: ").split()
        if len(row) != cols_x:
            raise ValueError("Number of elements in each row must match the number of columns.")
        elements_x.append(row)
    x = np.array(elements_x, dtype=float)

    rows_h = int(input("Enter the number of rows for the filter h: "))
    cols_h = int(input("Enter the number of columns for the filter h: "))
    elements_h = []
    for i in range(rows_h):
        row = input(f"Enter space-separated elements for row {i+1} of h: ").split()
        if len(row) != cols_h:
            raise ValueError("Number of elements in each row must match the number of columns.")
        elements_h.append(row)
    h = np.array(elements_h, dtype=float)

    # Compute 2D DFT
    X = dft2d(x)

    # Compute magnitude spectrum
    magnitude = magnitude_spectrum(X)

    # Compute phase spectrum
    phase = phase_spectrum(X)

    # Shift the magnitude spectrum
    shifted_magnitude = shift_spectrum(magnitude)

    # Shift the phase spectrum
    shifted_phase = shift_spectrum(phase)

    # Plotting
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(np.abs(X), cmap='gray')
    plt.title('2D DFT Magnitude')

    plt.subplot(2, 2, 2)
    plt.imshow(np.angle(X), cmap='hsv')
    plt.title('2D DFT Phase')

    plt.subplot(2, 2, 3)
    plt.imshow(shifted_magnitude, cmap='gray')
    plt.title('Shifted Magnitude Spectrum')

    plt.subplot(2, 2, 4)
    plt.imshow(shifted_phase, cmap='hsv')
    plt.title('Shifted Phase Spectrum')

    plt.tight_layout()
    plt.show()

    # Perform convolution using the convolution theorem
    result = convolution_theorem(x, h)

    # Plotting
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(x, cmap='gray')
    plt.title('Input Signal')

    plt.subplot(1, 3, 2)
    plt.imshow(h, cmap='gray')
    plt.title('Filter')

    plt.subplot(1, 3, 3)
    plt.imshow(result, cmap='gray')
    plt.title('Convolution Result')

    plt.tight_layout()
    plt.show()

except ValueError as ve:
    print(f"Error: {ve}")
