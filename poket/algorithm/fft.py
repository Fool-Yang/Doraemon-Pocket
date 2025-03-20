from math import sin, cos, pi

def FFT(X):
    n = len(X)
    power_of_2 = 1
    while power_of_2 < n:
        power_of_2 *= 2
    return _FFT(X + [0]*(power_of_2 - n))

def _FFT(X):
    n = len(X)
    if n == 1:
        return X
    even = _FFT(X[::2])
    odd = _FFT(X[1::2])
    F = [0]*n
    middle = n//2
    theta = 2*pi/n
    nth_root_of_unity = complex(cos(theta), sin(theta))
    omega = 1 # the current evaluation_point
    for i in range(middle):
        even_i = even[i]
        omega_odd_i = omega*odd[i]
        F[i] = even_i + omega_odd_i
        F[middle + i] = even_i - omega_odd_i
        omega *= nth_root_of_unity
    return F

def IFFT(X):
    n = len(X)
    power_of_2 = 1
    while power_of_2 < n:
        power_of_2 *= 2
    return [x/n for x in _IFFT(X + [0]*(power_of_2 - n))]

def _IFFT(X):
    n = len(X)
    if n == 1:
        return X
    even = _IFFT(X[::2])
    odd = _IFFT(X[1::2])
    F = [0]*n
    middle = n//2
    theta = -2*pi/n
    nth_root_of_unity = complex(cos(theta), sin(theta))
    omega = 1 # the current evaluation_point
    for i in range(middle):
        even_i = even[i]
        omega_odd_i = omega*odd[i]
        F[i] = even_i + omega_odd_i
        F[middle + i] = even_i - omega_odd_i
        omega *= nth_root_of_unity
    return F
