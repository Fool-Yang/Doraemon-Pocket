def PowerSet(S):
    return _power_set(list(S) if type(S) is not list else S)

def _power_set(S):
    if S:
        elem = S.pop()
        Pt1 = _power_set(S)
        Pt2 = [Sub + [elem] for Sub in Pt1]
        return Pt1 + Pt2
    return [[]]
