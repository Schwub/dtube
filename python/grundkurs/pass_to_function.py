class intWrapper():
    def __init__(self, value):
        self.value = int(value)

def reassing(x):
    x = 0

def reassing_int_wrapper_value(x):
    x.value = 0

int_wrapper = intWrapper(5)
reassing(int_wrapper.value)
reassing_int_wrapper_value(int_wrapper)
print(int_wrapper.value)
