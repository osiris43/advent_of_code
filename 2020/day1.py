def calculate():
    with open("expense_report.txt") as fp:
        expenses = [int(x) for x in fp.readlines()]
        answer = test_for_value(expenses, 2020)
        print(f"answer is {answer[0] * answer[1]}")

def part_two():
    with open("expense_report.txt") as fp:
        expenses = [int(x) for x in fp.readlines()]
        #expenses = [3,1,2,2017, 2008] for debugging
        answer = []

        for expense in expenses:
            target = 2020 - expense
            answer = test_for_value(expenses, target)
            if [] == answer:
                continue
            
            answer.append(expense)
            print(f"answer is {answer[0] * answer[1] * answer[2]}")
            break


def test_for_value(expenses, sum):
    for expense in expenses:
        target = sum - expense
        print(f"{sum} and {target}")
        if target in expenses:
            return [target, expense]

    return [] 

if __name__ == '__main__':
    #calculate()
    part_two()