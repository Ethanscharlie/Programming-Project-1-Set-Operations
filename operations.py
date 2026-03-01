from typing import TypeAlias

SubSet: TypeAlias = list[str]
Multiset: TypeAlias = dict[str, int]

UNIVERSAL_SET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]

#Author: Christian Miller
###################################################
# PART 1
###################################################

# Create a blank list for all methods in part 1
def blankList():
    out : list[bool] = [0,0,0,0,0,0,0,0,0,0,0,0]
    return out

# Converts the input subset into a list of booleans
def setStrToBool(subSet : SubSet) -> list[bool]:
    out = blankList()

    for index, element in enumerate(UNIVERSAL_SET):
        out[index] = element in subSet
    return out

# Performs the complement operation on the subset A
# Returns: a list[bool] with the operation performed
def complement(a: SubSet) -> list[bool]:
    out = blankList()

    boolA = setStrToBool(a)

    for i in range(len(out)):
        out[i] = not boolA[i]
    #if a[i] == 0, then out[i] = 1 and vice versa
    return out

# Performs the union operation on the subsets A and B
# Returns: a list[bool] with the operation performed
def union(a: SubSet, b: SubSet) -> list[bool]:
    out = blankList()

    boolA = setStrToBool(a)
    boolB = setStrToBool(b)

    for i in range(len(out)):
        out[i] = (boolA[i] or boolB[i]) #self explanatory
    return out


# Performs the intersection operation on the subsets A and B
# Returns: a list[bool] with the operation performed
def intersection(a: SubSet, b: SubSet) -> list[bool]:
    out = blankList()

    boolA = setStrToBool(a)
    boolB = setStrToBool(b)

    for i in range(len(out)):
        out[i] = (boolA[i] and boolB[i])
    return out

# Performs the difference operation on the subsets A and B
# Returns: a list[bool] with the operation performed
def difference(a: SubSet, b: SubSet) -> list[bool]:
    out = blankList()

    boolA = setStrToBool(a)
    boolB = setStrToBool(b)

    for i in range(len(out)):
        out[i] = (boolA[i] and not boolB[i]) # a == 1 and b == 0
    return out

# Performs the difference operation symmetrically on the subsets A and B
# Returns: a list[bool] with the operation performed
def symmetricDifference(a: SubSet, b: SubSet) -> list[bool]:
    out = blankList()

    boolA = setStrToBool(a)
    boolB = setStrToBool(b)

    for i in range(len(out)):
        out[i] = (boolA[i] ^ boolB[i]) # exclusive or
    return out


###################################################
# PART 2
###################################################

#Sometimes the number of times an element occurs in an unordered collection matters.
#A multiset (or mset or bag) is an unordered collection of elements where an element
#can occur as a member more than once.

# Create a blank Multiset for all methods in part 2
def blankMultiSet() -> Multiset:
    out : Multiset = {
      "a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0,
      "f" : 0, "g" : 0, "h" : 0, "i" : 0, "j" : 0,
      "k" : 0, "l" : 0
      }
    return out

# Takes an input Multiset and returns a similar Multiset with
# values of zero explicitly specified.
# ex input : {a : 1}
#    output: {a : 1, b : 0, c : 0, d : 0....etc.}
def getTheZeroes(multiSet : Multiset) -> Multiset:
    out = blankMultiSet()

    for element in UNIVERSAL_SET:
        if element in multiSet:
            out[element] = multiSet[element]
    return out

# Performs the given operation on two Multisets
# Multiset union (A ∪ B): for each element, take the maximum count in A and B.
# Returns: a Multiset with the operation applied
def multisetUnion(a: Multiset, b: Multiset) -> Multiset:
    out = blankMultiSet()
    

    zeroA = getTheZeroes(a)
    zeroB = getTheZeroes(b)

    for element in out:
        out[element] = max(zeroA[element], zeroB[element])
    return out

# Performs the given operation on two Multisets
# Multiset intersection (A ∩ B): for each element, take the minimum count in A and B.
# Returns: a Multiset with the operation applied
def multisetIntersection(a: Multiset, b: Multiset) -> Multiset:
    out = blankMultiSet()

    zeroA = getTheZeroes(a)
    zeroB = getTheZeroes(b)

    for element in out:
        out[element] = min(zeroA[element], zeroB[element])
    return out

# Performs the given operation on two Multisets
# Multiset difference (A − B): for each element, subtract B’s count from A’s count, but not below 0.
# Returns: a Multiset with the operation applied
def multisetDifference(a: Multiset, b: Multiset) -> Multiset:
    out = blankMultiSet()

    zeroA = getTheZeroes(a)
    zeroB = getTheZeroes(b)

    for element in out:
        out[element] = max(0, zeroA[element] - zeroB[element])
    return out

# Performs the given operation on two Multisets
# Multiset sum (A + B): for each element, add the two counts.
# Returns: a Multiset with the operation applied
def multisetSum(a: Multiset, b: Multiset) -> Multiset:
    out = blankMultiSet()

    zeroA = getTheZeroes(a)
    zeroB = getTheZeroes(b)

    for element in out:
        out[element] = zeroA[element] + zeroB[element]
    return out
