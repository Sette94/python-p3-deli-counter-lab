# import ipdb
katz_deli = []


def line(katz_deli):
    if katz_deli:
        line_data = ''.join(f'{index+1}. {value} ' for index,
                            value in enumerate(katz_deli))
        print(f"The line is currently: {line_data}")
    else:
        print("The line is currently empty.")


def take_a_number(katz_deli, patron):
    if patron:
        katz_deli.append(patron)
        print(f"Welcome, {patron}. You are number {len(katz_deli)} in line.")


def now_serving(katz_deli):
    if katz_deli:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)
    else:
        print("There is nobody waiting to be served!")


# ipdb.set_trace()
