import time


def worktime(f1, f2):
    def f(string):
        initial_time = time.time()
        f1(string)
        first = time.time() - initial_time
        initial_time = time.time()
        f2(string)
        second = time.time() - initial_time
        print(f1.__name__ if first < second else f2.__name__)
    return f


def find_c_symbols(st):
    st = st.lower()
    count = 0
    for i in set(st):
        if st.count(i) > 1:
            count += 1
    print(count)


def counter_2(s):
    return len([ch for ch in (set(s.lower())) if s.lower().count(ch) > 1])


funcion = worktime(find_c_symbols, counter_2)
funcion('aaaBBnn')
