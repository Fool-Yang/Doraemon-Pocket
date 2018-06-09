def Inversion(Array):
    return _inversion(Array)[1]

def _inversion(Array):
    if len(Array) == 1:
        return (Array, 0)
    left, right = Array[:len(Array) // 2], Array[len(Array) // 2:]
    left, right = _inversion(left), _inversion(right)
    inversion = left[1] + right[1]
    # merge steps
    i = j = k = 0
    while i < len(left[0]) and j < len(right[0]):
        if left[0][i] <= right[0][j]:
            Array[k] = left[0][i]
            i += 1
            k += 1
        else:
            Array[k] = right[0][j]
            j += 1
            k += 1
            inversion += len(left[0]) - i
    while i < len(left[0]):
        Array[k] = left[0][i]
        i += 1
        k += 1
    while j < len(right[0]):
        Array[k] = right[0][j]
        j += 1
        k += 1
    return (Array, inversion)
