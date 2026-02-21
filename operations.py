from typing import TypeAlias

SubSet: TypeAlias = list[str]
Multiset: TypeAlias = dict[str, int]

UNIVERSAL_SET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]

###################################################
# PART 1
###################################################

#code duplication thing
def blankList():
    out : list[bool] = [0,0,0,0,0,0,0,0,0,0,0,0]
    return out

#converts a subset into a list of booleans
def setStrToBool(subSet : SubSet) -> list[bool]:
    out = blankList()

    for element in UNIVERSAL_SET:
        out[element.index] = element in subSet
    return out

#complement: everything outside of a in the universal set
#ex: a = [a,b]
# complement(a) = [c, d, e, f, g, h, i, j, k] 
def complement(a: SubSet) -> list[bool]:
    out = blankList()

    boolA = setStrToBool(a)

    for i in range(out.len()):
        out[i] = not boolA[i]
    #if a[i] == 0, then out[i] = 1 and vice versa
    return out

#union: a combination of the two sets
def union(a: SubSet, b: SubSet) -> list[bool]:
    out = blankList()

    boolA = setStrToBool(a)
    boolB = setStrToBool(b)

    for i in range(out.len()):
        out[i] = (boolA[i] or boolB[i]) #self explanatory
    return out


# intersection: 
# all elements shared between sets a and b
def intersection(a: SubSet, b: SubSet) -> list[bool]:
    out = blankList()

    boolA = setStrToBool(a)
    boolB = setStrToBool(b)

    for i in range(out.len()):
        out[i] = (boolA[i] and boolB[i]) #self explanatory
    return out

# difference: 
# all elements in a but NOT b
def difference(a: SubSet, b: SubSet) -> list[bool]:
    out : list[bool] = [0,0,0,0,0,0,0,0,0,0,0,0]

    boolA = setStrToBool(a)
    boolB = setStrToBool(b)

    for i in range(out.len()):
        out[i] = (boolA[i] and not boolB[i]) # a == 1 and b == 0
    return out

# symmetric difference:
# all elements in one set but NOT the other
def symmetricDifference(a: SubSet, b: SubSet) -> list[bool]:
    out : list[bool] = [0,0,0,0,0,0,0,0,0,0,0,0]

    boolA = setStrToBool(a)
    boolB = setStrToBool(b)

    for i in range(out.len()):
        out[i] = (boolA[i] ^ boolB[i]) # exclusive or
    return out


###################################################
# PART 2
###################################################

#Sometimes the number of times an element occurs in an unordered collection matters.
#A multiset (or mset or bag) is an unordered collection of elements where an element
#can occur as a member more than once.

def blankMultiSet() -> Multiset:
    out : Multiset = {
      "a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0,
      "f" : 0, "g" : 0, "h" : 0, "i" : 0, "j" : 0,
      "k" : 0, "l" : 0
      }
    return out

#its easier this way imo
def getTheZeroes(multiSet : Multiset) -> Multiset:
    out = blankMultiSet()

    for element in UNIVERSAL_SET:
        if element in multiSet:
            out[element] = multiSet[element]
        
    return out

#Multiset union (A ∪ B): for each element, take the maximum count in A and B.
def multisetUnion(a: Multiset, b: Multiset) -> Multiset:
    out = blankMultiSet()

    zeroA = getTheZeroes(a)
    zeroB = getTheZeroes(b)

    for element in out:
        out[element] = max(zeroA[element], zeroB[element])
    return out

#Multiset intersection (A ∩ B): for each element, take the minimum count in A and B.
def multisetIntersection(a: Multiset, b: Multiset) -> Multiset:
    out = blankMultiSet()

    zeroA = getTheZeroes(a)
    zeroB = getTheZeroes(b)

    for element in out:
        out[element] = min(zeroA[element], zeroB[element])
    return out

#Multiset difference (A − B): for each element, subtract B’s count from A’s count, but not below 0.
def multisetDifference(a: Multiset, b: Multiset) -> Multiset:
    out = blankMultiSet()

    zeroA = getTheZeroes(a)
    zeroB = getTheZeroes(b)

    for element in out:
        out[element] = max(0, zeroA[element] - zeroB[element])
    return out

#Multiset sum (A + B): for each element, add the two counts.
def multisetSum(a: Multiset, b: Multiset) -> Multiset:
    out = blankMultiSet()

    zeroA = getTheZeroes(a)
    zeroB = getTheZeroes(b)

    for element in out:
        out[element] = zeroA[element] + zeroB[element]
    pass
