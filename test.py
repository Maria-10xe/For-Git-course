# Lab 4: optional question

def couple(s, t):
    assert len(s) == len(t)
    return [[s[i],t[i]] for i in range(len(s))]
