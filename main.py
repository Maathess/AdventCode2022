'''
Exo 1
'''

def exo1(w):
    result = 0
    max_res = 0
    res = []
    with open(w) as f:
        for line in f:
            try:
                num = float(line)
                result += num
                #print(result)
            except ValueError:
                if result < max_res:
                    res.append(result)
                    result = 0
                else :
                    max_res = result
                    res.append(result)
                    result = 0

    sorted_res = sorted(res,reverse=True)
    print(sorted_res)
    print(sum(sorted_res[:2]))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    exo1("input\input_exo1.txt")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
