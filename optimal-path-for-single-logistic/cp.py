import pickle

# 파일을 열고 데이터 로드
with open('/home/unist51002/PycharmProjects/optimal-path-for-single-logistic/data/node_coordinates.pkl', 'rb') as f:
    exist_data = pickle.load(f)


print(exist_data)