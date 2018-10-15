from time_repr import Time

def test_nominal_init():
    t = Time('12:25:36')
    assert t.hour   == 12
    assert t.minute == 25
    assert t.second == 36

def test_wrong_format_input():
    #todo
    t = Time('12h25m36s')
    pass

def test_unphysical_input():
    #todo
    t = Time('65:25:36')
    t = Time('12:61:36')
    t = Time('12:25:61')
    pass
