import numpy as np

def solve_linear_eq_crout(matrix_A, vector_b):
    try:
        n = len(matrix_A)
        L = np.zeros((n, n))
        U = np.zeros((n, n))

        # Dekomposisi Crout
        for i in range(n):
            U[i, i] = 1
            for j in range(i, n):
                s = sum(L[j, k] * U[k, i] for k in range(i))
                L[j, i] = matrix_A[j, i] - s
            for j in range(i+1, n):
                s = sum(L[i, k] * U[k, j] for k in range(i))
                U[i, j] = (matrix_A[i, j] - s) / L[i, i]

        # Solusi dengan substitusi maju dan mundur
        y = np.linalg.solve(L, vector_b)
        x = np.linalg.solve(U, y)

        return x
    except Exception as e:
        print("An error occurred:", e)
        return None

# Testing
def test_crout_method():
    # Contoh sistem persamaan linear
    A = np.array([[3, 2, 1], [1, -1, 2], [2, 3, 1]])
    b = np.array([9, 8, 3])

    # Memanggil fungsi untuk mencari solusi
    x = solve_linear_eq_crout(A, b)

    # Menampilkan hasil pengujian
    if x is not None:
        print("Uji berhasil")
        print("Solusi sistem persamaan linear:")
        for i, sol in enumerate(x):
            print("x{} = {}".format(i+1, sol))
    else:
        print("Uji tidak berhasil")

# Menjalankan pengujian
if __name__ == "__main__":
    test_crout_method()
