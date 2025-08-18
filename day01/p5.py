
if __name__ == '__main__':
    num1=int(input("num1을 입력 하세요"))
    print(num1)
    num2 =int(input("num2를 입력 하세요"))
    print(num2)
    num3 = int(input("num2를 입력 하세요"))
    print(num3)

    min=0
    max=0

    if num1<=num2:
        min=num1
        max=num2
    else:
        min=num2
        max=num1
    if min>=num3:
        min=num3
    if max<=num3:
        max=num3

    # 강사님 코드
    # if num1>num2:
    #     min=num2
    #     if num3<min:
    #         min=num3
    # else:
    #     min=num1
    #     if num3<min:
    #         min=num3
    #
    # if num1>num2:
    #     max=num1
    #     if num3>max:
    #         max=num3
    # else:
    #     max=num2
    #     if num3>max:
    #         max=num3

    print(f'최솟값은 {min}, 최댓값은 {max}')