from typing import TypeAlias

SubSet: TypeAlias = list[str]
Multiset: TypeAlias = dict[str, int]

UNIVERSAL_SET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]

###################################################
# PART 1
###################################################


def complement(a: SubSet) -> list[bool]:
    pass


def union(a: SubSet, b: SubSet) -> list[bool]:
    pass


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
