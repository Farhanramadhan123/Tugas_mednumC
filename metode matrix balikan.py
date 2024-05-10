import numpy as np

def solve_linear_eq_inv(matrix_A, vector_b):
    try:
        inv_A = np.linalg.inv(matrix_A)
        x = np.dot(inv_A, vector_b)
        return x
    except np.linalg.LinAlgError:
        print("Matrix A is singular. Cannot compute inverse.")
        return None

# Fungsi untuk menyelesaikan sistem persamaan linear dengan matriks balikan
def solve_linear_eq(matrix_A, vector_b, method='inv'):
    if method == 'inv':
        return solve_linear_eq_inv(matrix_A, vector_b)
    else:
        print("Metode tidak valid.")
        return None

# Fungsi untuk menguji kode sumber
def test():
    # Tes dengan contoh kasus
    A = np.array([[3, 2, 1], [1, -1, 2], [2, 3, 1]])
    b = np.array([9, 8, 3])

    # Menggunakan metode matriks balikan
    x_inv = solve_linear_eq(A, b, method='inv')
    print("Solusi dengan metode matriks balikan:", x_inv)

# Jalankan pengujian
if __name__ == "__main__":
    test()

