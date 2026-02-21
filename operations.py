from typing import TypeAlias

SubSet: TypeAlias = list[str]
Multiset: TypeAlias = dict[str, int]

UNIVERSAL_SET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]

###################################################
# PART 1
###################################################

#complement: everything outside of a in the universal set
#ex: a = [a,b]
# complement(a) = [c, d, e, f, g, h, i, j, k] 
def complement(a: SubSet) -> list[bool]:
    out = list[bool]
    out = [0,0,0,0,0,0,0,0,0,0,0,0]

    for i in range(12):
        out[i] = !a[i]
    #if a[i] == 0, then out[i] = 1 and vice versa
    return out[i]

#union: a combination of the two sets
def union(a: SubSet, b: SubSet) -> list[bool]:
    out = list[bool]
    out = [0,0,0,0,0,0,0,0,0,0,0,0]

    for i in range(12):
        out[i] = (a[i] or b[i])
    return out[i]


# intersection: 
# all elements shared between sets a and b
def intersection(a: SubSet, b: SubSet) -> list[bool]:
    pass


def difference(a: SubSet, b: SubSet) -> list[bool]:
    pass


def symmetricDifference(a: SubSet, b: SubSet) -> list[bool]:
    pass


###################################################
# PART 2
###################################################


def multisetUnion(a: Multiset, b: Multiset) -> Multiset:
    pass


def multisetIntersection(a: Multiset, b: Multiset) -> Multiset:
    pass


def multisetDifference(a: Multiset, b: Multiset) -> Multiset:
    pass


def multisetSum(a: Multiset, b: Multiset) -> Multiset:
    pass
