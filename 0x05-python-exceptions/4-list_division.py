#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    try:
        for i in range(list_length):
            try:
                num_1 = my_list_1[i]
                num_2 = my_list_2[i]

                if isinstance(num_1, (int, float)) and isinstance(num_2, (int, float)):
                    try:
                        result = num_1 / num_2
                        result_list.append(result)
                    except ZeroDivisionError:
                        result_list.append(0)
                        print("division by 0")
                else:
                    result_list.append(0)
                    print("wrong type")
            except IndexError:
                print("out of range")
                break
    finally:
        return result_list

