
# This function takes a list and turns it into a list of lists. Those sub-lists are from the first list, in groups of 3
def groups_of_3(input_list:list[int]) -> list[list[int]]:
    output_list = []
    sub_list = []
    tally = 1
    print(len(input_list))
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
    if len(input_list) % 3 == 1:
        sub_list = []
        print(len(input_list)-3)
        idx = len(input_list) - 1
        sub_list.append(input_list[idx])
        output_list.append(sub_list)
    if len(input_list) % 3 == 2:
        sub_list = []
        print(len(input_list)-3)
        print(len(input_list)-2)
        idx = len(input_list) - 2
        sub_list.append(input_list[idx])
        idx = len(input_list) - 1
        sub_list.append(input_list[idx])
        output_list.append(sub_list)
    print(output_list)
    return output_list