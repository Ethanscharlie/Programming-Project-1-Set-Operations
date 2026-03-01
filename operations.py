from typing import TypeAlias

SubSet: TypeAlias = list[str]
Multiset: TypeAlias = dict[str, int]

UNIVERSAL_SET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]

# Authors: Christian Miller & Ethan J. Hadley

###################################################
# PART 1
###################################################


def blankList():
    """
    Create a blank list of all methods in part 1.
    """
    return [False] * len(UNIVERSAL_SET)


def setStrToBool(subSet: SubSet) -> list[bool]:
    """
    Coverts the input subset into a list of booleans.

    Args:
        subset SubSet: The input subset.

    Returns:
        List of true or false depending on if the element from the universal set in in the given subset.
    """

    return [element in subSet for index, element in enumerate(UNIVERSAL_SET)]


def complement(a: SubSet) -> list[bool]:
    """
    Performs the complement operation on the subset A.

    Args:
        a Subset: An input subset.

    Returns:
        A list[bool] with the operation performed
    """
    out = blankList()

    boolA = setStrToBool(a)

    for i in range(len(out)):
        out[i] = not boolA[i]
    # if a[i] == 0, then out[i] = 1 and vice versa
    return out


def union(a: SubSet, b: SubSet) -> list[bool]:
    """
    Performs the union operation on the subsets A and B.

    Args:
        a Subset: An input subset.
        b Subset: An input subset.

    Returns:
        A list[bool] with the operation performed.
    """

    out = blankList()

    boolA = setStrToBool(a)
    boolB = setStrToBool(b)

    for i in range(len(out)):
        out[i] = boolA[i] or boolB[i]  # self explanatory
    return out


def intersection(a: SubSet, b: SubSet) -> list[bool]:
    """
    Performs the intersection operation on the subsets A and B.

    Args:
        a Subset: An input subset.
        b Subset: An input subset.

    Returns:
        A list[bool] with the operation performed.
    """

    out = blankList()

    boolA = setStrToBool(a)
    boolB = setStrToBool(b)

    for i in range(len(out)):
        out[i] = boolA[i] and boolB[i]
    return out


def difference(a: SubSet, b: SubSet) -> list[bool]:
    """
    Performs the difference operation on the subsets A and B.

    Args:
        a Subset: An input subset.
        b Subset: An input subset.

    Returns:
        A list[bool] with the operation performed.
    """

    out = blankList()

    boolA = setStrToBool(a)
    boolB = setStrToBool(b)

    for i in range(len(out)):
        out[i] = boolA[i] and not boolB[i]  # a == 1 and b == 0
    return out


def symmetricDifference(a: SubSet, b: SubSet) -> list[bool]:
    """
    Performs the difference operation symmetrically on the subsets A and B

    Args:
        a Subset: An input subset.
        b Subset: An input subset.

    Returns:
        A list[bool] with the operation performed.
    """

    out = blankList()

    boolA = setStrToBool(a)
    boolB = setStrToBool(b)

    for i in range(len(out)):
        out[i] = boolA[i] ^ boolB[i]  # exclusive or
    return out


###################################################
# PART 2
###################################################

# Sometimes the number of times an element occurs in an unordered collection matters.
# A multiset (or mset or bag) is an unordered collection of elements where an element
# can occur as a member more than once.


def blankMultiSet() -> Multiset:
    """
    Create a blank Multiset for all methods in part 2.
    """

    return {element: 0 for element in UNIVERSAL_SET}


def getTheZeroes(multiSet: Multiset) -> Multiset:
    """
    Takes an input Multiset and returns a similar Multiset with
    values of zero explicitly specified.
    ex input : {a : 1}
       output: {a : 1, b : 0, c : 0, d : 0....etc.}
    """
    out = blankMultiSet()

    for element in UNIVERSAL_SET:
        if element in multiSet:
            out[element] = multiSet[element]
    return out


def multisetUnion(a: Multiset, b: Multiset) -> Multiset:
    """
    Multiset union (A ∪ B): for each element, take the maximum count in A and B.

    Args:
        a Multiset: An input multiset.
        b Multiset: An input multiset.

    Returns:
        A Multiset with the operation applied.
    """

    out = blankMultiSet()

    zeroA = getTheZeroes(a)
    zeroB = getTheZeroes(b)

    for element in out:
        out[element] = max(zeroA[element], zeroB[element])
    return out


def multisetIntersection(a: Multiset, b: Multiset) -> Multiset:
    """
    Multiset intersection (A ∩ B): for each element, take the minimum count in A and B.

    Args:
        a Multiset: An input multiset.
        b Multiset: An input multiset.

    Returns:
        A Multiset with the operation applied.
    """

    out = blankMultiSet()

    zeroA = getTheZeroes(a)
    zeroB = getTheZeroes(b)

    for element in out:
        out[element] = min(zeroA[element], zeroB[element])
    return out


def multisetDifference(a: Multiset, b: Multiset) -> Multiset:
    """
    Multiset difference (A − B): for each element, subtract B’s count from A’s count, but not below 0.

    Args:
        a Multiset: An input multiset.
        b Multiset: An input multiset.

    Returns:
        A Multiset with the operation applied.
    """

    out = blankMultiSet()

    zeroA = getTheZeroes(a)
    zeroB = getTheZeroes(b)

    for element in out:
        out[element] = max(0, zeroA[element] - zeroB[element])
    return out


def multisetSum(a: Multiset, b: Multiset) -> Multiset:
    """
    Multiset sum (A + B): for each element, add the two counts.

    Args:
        a Multiset: An input multiset.
        b Multiset: An input multiset.

    Returns:
        A Multiset with the operation applied.
    """

    out = blankMultiSet()

    zeroA = getTheZeroes(a)
    zeroB = getTheZeroes(b)

    for element in out:
        out[element] = zeroA[element] + zeroB[element]
    return out
