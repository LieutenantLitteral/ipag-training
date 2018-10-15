from time_repr import Time

def test_repr():
    a = Time('02:06:46')
    assert a.__repr__() == '02h 06m 46s' 
