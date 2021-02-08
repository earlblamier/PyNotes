listarray = [25, 54, 27, 54, 23, 47, 23, 4, 27, 36, 26, 12, 25, 29, 41]
    
def list_average(num):

    sum_num = 0
    for t in num:
        sum_num = sum_num + t
        
    avg = sum_num / len(num)
    return avg

print("The average is", list_average(listarray))
