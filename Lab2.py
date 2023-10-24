import statistics


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    average = calc_average_temperature(num_list)
    min_val, max_val = calc_min_max_temperature(num_list)
    sorted_list = sort_temperature(num_list)
    median = calc_median_temperature(sorted_list)
    print(num_list)
    print("Average: " + str(average))
    print("Minimum Value: " + str(min_val))
    print("Maximum Value: " + str(max_val))
    print(sorted_list)
    print("Median: " + str(median))

def display_main_menu():
     print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input()
    str_list = user_input.split(", ")
    float_list = list(map(float, str_list))
    return float_list

def calc_average_temperature(num_list):
     return sum(num_list)/len(num_list)

def calc_min_max_temperature(num_list):
    return min(num_list), max(num_list)

def sort_temperature(num_list):
    return sorted(num_list)

def calc_median_temperature(sorted_list):
    return statistics.median(sorted_list)

if __name__ == "__main__":
    main()