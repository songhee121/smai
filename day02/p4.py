if __name__ == '__main__':
    #set
    s1={1,2,3,4,5}
    print(type(s1))
    print(s1)
    s1.add(6)
    s1.add(5)
    print(s1)
    #set은 중복된 값 삽입 불가

    #tuple
    print("\n--------tuple----------")
    t1=(1,2,3,4,5)
    print(type(t1))
    print(t1)
    print(t1[1])
    #tuple은 값 변경 불가

    #딕셔너리
    #JavaScript JSON
    print("\n---------dict---------")
    d1={"a":1, "b":2, "c":3}
    print(type(d1))
    print(d1)
    print(d1["a"])

    print("\n")
    d2={"name":"정태원", "age":32, "major":"ee"}
    print(d2["name"])
    print(d2["age"])

    sts=[
        {"name": "정태원", "age": 32, "major": "ee"},
        {"name": "김송희", "age": 23, "major": "ee"},
        {"name": "조태희", "age": 28, "major": "sw"},
        {"name": "머하지", "age": 20, "major": "sw"}
    ]
    print("\n")

    #응용
    #전체 학과 학생의 나이 합과 평균
    sum=0
    for i in sts:
        sum+=i["age"]

    print(f'전체 학과 학생 나이 합은 {sum}, 평균은 {sum/len(sts)}입니다')

    #ee 학과 학생의 나이 합과 평균
    sum=0
    len=0
    for i in sts:
        if i["major"]=="ee":
            sum+=i["age"]
            len+=1

    print(f'전자과 학생 나이 합은 {sum}, 평균은 {sum/len}입니다')