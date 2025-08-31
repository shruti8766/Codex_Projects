import numpy as np

def get_matrix_input(matrix_name):
    print(f"\nEnter dimensions for {matrix_name} (rows columns):")
    try:
        rows, cols = map(int, input().split())
        if rows <= 0 or cols <= 0:
            raise ValueError("Dimensions must be positive integers.")
        print(f"Enter {rows}x{cols} elements for {matrix_name} (row-wise, space-separated):")
        elements = []
        for i in range(rows):
            row = list(map(float, input(f"Row {i+1}: ").split()))
            if len(row) != cols:
                raise ValueError(f"Expected {cols} elements in row {i+1}, got {len(row)}.")
            elements.append(row)
        return np.array(elements)
    except ValueError as e:
        print(f"Error: {e}")
        return None

def display_matrix(matrix, name):
    print(f"\n{name}:")
    for row in matrix:
        print(" ".join(f"{x:.2f}" for x in row))

def matrix_operations_tool():
    print("=== Matrix Operations Tool ===")
    A = get_matrix_input("Matrix A")
    if A is None:
        print("Invalid input for Matrix A. Exiting.")
        return
    B = get_matrix_input("Matrix B")
    if B is None:
        print("Invalid input for Matrix B. Exiting.")
        return
    display_matrix(A, "Matrix A")
    display_matrix(B, "Matrix B")
    while True:
        print("\nSelect an operation:")
        print("1. Addition (A + B)")
        print("2. Subtraction (A - B)")
        print("3. Multiplication (A * B)")
        print("4. Transpose of Matrix A")
        print("5. Transpose of Matrix B")
        print("6. Determinant of Matrix A")
        print("7. Determinant of Matrix B")
        print("8. Exit")
        choice = input("Enter choice (1-8): ")
        try:
            if choice == "1":
                if A.shape != B.shape:
                    print("Error: Matrices must have the same dimensions for addition.")
                else:
                    result = A + B
                    display_matrix(result, "A + B")
            elif choice == "2":
                if A.shape != B.shape:
                    print("Error: Matrices must have the same dimensions for subtraction.")
                else:
                    result = A - B
                    display_matrix(result, "A - B")
            elif choice == "3":
                if A.shape[1] != B.shape[0]:
                    print("Error: Columns of A must match rows of B for multiplication.")
                else:
                    result = np.dot(A, B)
                    display_matrix(result, "A * B")
            elif choice == "4":
                result = A.T
                display_matrix(result, "Transpose of A")
            elif choice == "5":
                result = B.T
                display_matrix(result, "Transpose of B")
            elif choice == "6":
                if A.shape[0] != A.shape[1]:
                    print("Error: Matrix A must be square for determinant.")
                else:
                    det = np.linalg.det(A)
                    print(f"Determinant of Matrix A: {det:.2f}")
            elif choice == "7":
                if B.shape[0] != B.shape[1]:
                    print("Error: Matrix B must be square for determinant.")
                else:
                    det = np.linalg.det(B)
                    print(f"Determinant of Matrix B: {det:.2f}")
            elif choice == "8":
                print("Exiting.")
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    matrix_operations_tool()