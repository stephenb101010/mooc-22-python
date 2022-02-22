def row_sums(my_matrix: list):
    for row in my_matrix:
        sum = 0
        for entry in row:
            sum += entry
        row.append(sum)