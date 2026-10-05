def bobble_sort(list_to_sot):
    for outer_index in range(0, len(list_to_sot) - 1):
        has_madde_change = False
        for index in range(0, len(list_to_sot) - 1 - outer_index):
            current_element = list_to_sot[index]
            next_element = list_to_sot[index + 1]

            print(f'-- Iteration {outer_index}, {index}. Current element: {current_element}, Next element: {next_element}')

            if current_element > next_element:
                print('The current element is less than the next one. Swapping them...')
                list_to_sot[index] = next_element
                list_to_sot[index + 1] = current_element
                has_madde_change = True

        if not has_madde_change:
            return


my_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list3 = []
my_list4 = [2, 2, 1, 3, -4, 5, 6, 6, -7, 8, 9, -9]
bobble_sort(my_list4)

print(my_list4)