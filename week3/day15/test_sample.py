import pytest
def take_money(q=0,d=0,n=0,s=0):
    monies = []
    q *= 25
    d *=10
    n *= 5
    monies.append(q)
    monies.append(d)
    monies.append(n)
    monies.append(s)
    return sum(monies)

def test_answer():
    assert take_money(1,1,1,1) == 41 
    assert take_money() == 0
    assert take_money(0,1,0,1) == 11