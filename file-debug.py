x = 'CBI ชบ BKK กทม CMI ชม KBI กบ KNN ขก'.split()
eng = x[::2]
th = x[1::2]
q = 'กบ'
if q in th:
    print(eng[th.index(q)])
elif q in eng:
    print(th[eng.index(q)])
else:
    print('Not found')