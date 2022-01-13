def simple_gen():
    for x in range(3):
        yield x


for f in simple_gen():
    print(f)