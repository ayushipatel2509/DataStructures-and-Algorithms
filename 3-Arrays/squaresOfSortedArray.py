def square_of_sorted_array(arr):
    new_arr = []
    left = 0 
    right = len(arr) -1
    while left <=  right :
        square_left = arr[left] * arr[left]
        square_right = arr[right] *arr[right]
        if square_left < square_right:
            new_arr.append(square_left)
        else:
            new_arr.append(square_right)
        left = left +1
        right = right -1

    return new_arr