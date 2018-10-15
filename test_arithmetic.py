from time_repr import Time

def test_comp():
    a = Time('05:25:45')
    b = Time('05:25:45')
    assert a == b

def test_simple_addition():
    a = Time('05:25:45')
    b = Time('12:24:21')
    c = a + b
    assert c == Time('17:50:06')

def test_modulo_addition():
    a = Time('05:25:45')
    b = Time('20:24:21')
    c = a + b
    assert c == Time('01:50:06')

def test_modulo_addition_24():
    a = Time('03:37:45')
    b = Time('20:24:21')
    c = a + b
    assert c == Time('00:02:06')

def test_forward_multiply():
    a = Time('05:25:45')
    b = a*2
    assert b == Time('10:51:30')

def test_backward_multiply():
    a = Time('05:25:45')
    b = 2*a
    assert b == Time('10:51:30')
