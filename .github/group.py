def groups_of_3(input_list:list[int]) -> list[list[int]]:
    output_list = []
    sub_list = []
    tally = 1
    for idx in range(0,len(input_list)-1):
        if tally == 1 or tally == 2:
            sub_list.append(input_list[idx])
            tally += 1
        elif tally == 3:
            sub_list.append(input_list[idx])
            output_list.append(sub_list)
            print(sub_list)
            sub_list = []
            tally = 1
    output_list.append(sub_list)
    print(output_list)
    return output_list

print(4%3)