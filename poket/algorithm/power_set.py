def PowerSet(S):
    trans = type(S) is not list
    if trans:
        S = list(S)
    power_set = _power_set_r(S)
    if trans:
        power_set = set(power_set)
    return power_set

def _power_set(S):
    if len(S) == 0:
        return [[]]
    elem = S.pop()
    Pt1 = _power_set(S)
    Pt2 = [[elem] + Sub for Sub in Pt1]
    return Pt1 + Pt2
