def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort) - 1):
        has_made_chenges = False
        for index in range(len(list_to_sort) - 1, outer_index, -1):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index - 1]

            print(f'-- Iteration {outer_index}, {index}. Current element: {current_element}, Next element: {next_element}')

            if current_element < next_element:
                print('The current element is greater than the next one. Swapping them...')
                list_to_sort[index] = next_element
                list_to_sort[index - 1] = current_element
                has_made_chenges = True

        if not has_made_chenges:
            return


my_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list3 = []
my_list4 = [2, 2, 1, 3, -4, 5, 6, 6, -7, 8, 9, -9]
bubble_sort(my_list4)

print(my_list4)