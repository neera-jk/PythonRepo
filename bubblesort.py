def bubble_sort(data : list) -> None:
    n = len(data)
    comparision_count = 0
    for i in range(n - 1):
        swapped = False
        #for j in range(n - 1):
        for j in range(n - 1 - i):
            comparision_count += 1    
            if data[j] > data[j + 1]:
                data[j], data[j +1] = data[j +1], data[j]
                swapped = True
                
        if not swapped:
            break

    print(f"The comparision count is {comparision_count}")

numbers = [4, 2, 5, 7, 1, 6, 3]
bubble_sort(numbers)
print(f"The sorted data is {numbers}")