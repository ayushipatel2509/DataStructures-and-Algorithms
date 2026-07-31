def square_of_sorted_array(arr):
    new_arr = [0] * len(arr)
    pos = len(new_arr) -1 
    left = 0 
    right = len(arr) -1
    while left <=  right :
        square_left = arr[left] * arr[left]
        square_right = arr[right] *arr[right]
        if square_left < square_right:
            new_arr[pos] = square_right
            right = right -1
        else:
            new_arr[pos] = square_left
            left = left +1
        pos = pos -1
    return new_arr


print(square_of_sorted_array([-2,-1,0,3,4]))