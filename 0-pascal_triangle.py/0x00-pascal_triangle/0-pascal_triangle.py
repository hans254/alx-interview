def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1] * (i + 1) for i in range(n)]

    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle

# Test the function
if __name__ == "__main__":
    # Test with n = 5
    result_triangle = pascal_triangle(5)
    print_triangle(result_triangle)
