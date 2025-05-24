import statistics as stats
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")


def get_user_input():
    print("input: ")
    numbers=input()
    x=numbers.split(",")
    y=list(map(int, x))
    return y


def calc_average_temperature(num):
    y=sum(num)
    average=y/len(num)
    return average

def calc_min_max_temperature(num):
    minimum=min(num)
    maximum=max(num)
    result=[minimum,maximum]
    return result

def calc_median_temperature(num):
    median=stats.median(num)
    return median

def main():
    display_main_menu()
    num=get_user_input()
    average=calc_average_temperature(num)
    minmax=calc_min_max_temperature(num)
    median=calc_median_temperature(num)
    print(str(average))
    print("minimum , maximum ="+str(minmax))
    print("median = " +str(median))





if __name__ == "__main__":
    main()