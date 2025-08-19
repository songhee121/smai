if __name__ == '__main__':
    try:
        num=int(input("Input Number .?"))
        result=num+100
        print(f'결과 {result}')
    except:
        print("숫자만 입력해라")
    #숫자 입력 해야할 때 문자를 입력한 경우-예외 상황