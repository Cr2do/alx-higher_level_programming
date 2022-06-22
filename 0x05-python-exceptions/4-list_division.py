#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            result_val = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("Out of range")
            result_val = 0
        except ZeroDivisionError:
            print("division by 0")
            result_val = 0
        except TypeError:
            print("Wrong type")
            result_val = 0
        finally:
            new_list.append(result_val)
    return new_list
