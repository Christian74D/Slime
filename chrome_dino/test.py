
import pickle

net = pickle.load(open("best.pickle", 'rb'))

for i in range(100):
    output = net.activate([i, 25])
    if output[0] < 50:
        print(i," jumped ", output[0])
    else:
        print(i," nutjump ", output[0])
