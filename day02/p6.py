import pickle

if __name__ == '__main__':
    sts = [
        {"name": "정태원", "age": 32, "major": "ee"},
        {"name": "김송희", "age": 23, "major": "ee"},
        {"name": "조태희", "age": 28, "major": "sw"},
        {"name": "머하지", "age": 20, "major": "sw"}
    ]

    pickle.dump(sts, open('data/sts.pkl', 'wb'))
    result= pickle. load(open('data/sts.pkl', 'rb'))
    print(type(result))
    print(result)
    #pickle은 python 파일 형태 그대로 유지..