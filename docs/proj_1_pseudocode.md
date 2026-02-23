
# Operations

```
######################################################################################################
#####################                       operations.py                        #####################
######################################################################################################



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
    return out

```



# Operation Tests / Verification

```
######################################################################################################
#####################                       operationTests.py                    #####################
######################################################################################################



import operations
import unittest

"""
Required output / testability constraints (Parts 1 & 2)
• Part 1 must use a universal set with n ≥ 10 elements.
• For Part 1 results, display BOTH: (1) bit string / Boolean array and (2) element-name listing.
• Include at least 2–3 representative test cases in your Results (not just one).
• For Part 2, ensure both A and B have at least two elements with multiplicity > 1.
• Clearly label outputs so ordinary set operations are not confused with multiset operations.

The requirement is that your "results" (in your report) demonstrate correctness in a way a reader (or grader) can verify.

For Part 1, show both:
1. the bitstring / Boolean-array representation, and
2. the element-name listing, for each required operation, and for 2–3 representative test cases.

***That “expected output” is a format illustration — it does not mean verification is required to be manual.***

How to avoid duplicating tests:

You do not need to rewrite tests in two places. A good pattern is:
1. Unit tests (JUnit / pytest):
- assert correctness using structured comparisons (set equality, boolean arrays, counts, etc.)
- no printing unless a test fails
2. Demo / Results runner (a separate main() / demo()):
- runs the same operations on 2–3 cases
- prints the required labeled output (bits + element listing)

To keep this DRY, define your test cases once (e.g., U, A, B) and reuse them in both the unit-test loop and the demo/results loop.

Keep printing limited to the demo/results run:
● label the operation
● print bits/Booleans
● print the element list (same line or next line)
"""

SUBSET_A = ["a", "c", "e"]
SUBSET_B = ["b", "c", "d"]
SUBSET_C = ["f", "g"]
SUBSET_D = ["h", "i"]
SUBSET_EMPTY = []


def bitString(binary: list[bool]) -> str:
    """
    Convert a list of boolean values into a string.

    Args:
        binary (list[bool]): List of booleans.

    Returns:
        str: String of 0 or 1 seperated by spaces.
    """
    return " ".join(["1" if b else "0" for b in binary])


"""
Let the universal set be ordered as:
U = [a, b, c, d, e, f, g, h, i, j] (n = 10)

Suppose:
A = {a, c, e, j}
B = {b, c, f, g}

Then the bit strings (aligned to U) are:
A bits: 1 0 1 0 1 0 0 0 0 1
B bits: 0 1 1 0 0 1 1 0 0 0

Example result labeling (you should label similarly):
• NOT(A) (U − A): bits = 0 1 0 1 0 1 1 1 1 0 ; elements = {b, d, f, g, h, i}
• A ∪ B: bits = 1 1 1 0 1 1 1 0 0 1 ; elements = {a, b, c, e, f, g, j}
• A ∩ B: bits = 0 0 1 0 0 0 0 0 0 0 ; elements = {c}
• A − B: bits = 1 0 0 0 1 0 0 0 0 1 ; elements = {a, e, j}
• A ⊕ B: bits = 1 1 0 0 1 1 1 0 0 1 ; elements = {a, b, e, f, g, j}
"""


class TestPartOne(unittest.TestCase):
    # ---- Complement ----
    
    #      u = [a, b, c, d, e, f, g, h, i, j, k, l]
    #      a = [a,    c,    e                     ]
    # NOT(a) = [   b,    d,    f, g, h, i, j, k, l]
    def test_complement_basic(self):
        result = operations.complement(SUBSET_A)
        expected = [
            False,
            True,  # b
            False,
            True,  # d
            False,
            True,  # f
            True,  # g
            True,  # h
            True,  # i
            True,  # j
            True,  # k
            True,  # l
        ]
        self.assertEqual(result, expected)

    #      u = [a, b, c, d, e, f, g, h, i, j, k, l]
    #      e = [                                  ]
    # NOT(e) = [a, b, c, d, e, f, g, h, i, j, k, l]
    def test_complement_empty(self):
        result = operations.complement(SUBSET_EMPTY)
        self.assertEqual(result, [True] * 12)

    #      u = [a, b, c, d, e, f, g, h, i, j, k, l]
    # NOT(u) = [                                  ]
    def test_complement_full(self):
        result = operations.complement(operations.UNIVERSAL_SET)
        self.assertEqual(result, [False] * 12)

    # ---- Intersection ----
    
    #   u = [a, b, c, d, e, f, g, h, i, j, k, l]
    #   a = [a,    c,    e                     ]
    #   b = [   b, c, d                        ]
    # a∩b = [      c                           ]
    def test_intersection_overlap(self):
        result = operations.intersection(SUBSET_A, SUBSET_B)
        expected = [
            False,
            False,
            True,  # c
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
        ]
        self.assertEqual(result, expected)

    #   u = [a, b, c, d, e, f, g, h, i, j, k, l]
    #   c = [               f, g               ]
    #   d = [                     h, i         ]
    # c∩d = [                                  ]
    def test_intersection_disjoint(self):
        result = operations.intersection(SUBSET_C, SUBSET_D)
        self.assertEqual(result, [False] * 12)

    #   u = [a, b, c, d, e, f, g, h, i, j, k, l]
    #   a = [a,    c,    e                     ]
    #   e = [                                  ]
    # a∩e = [                                  ]
    def test_intersection_with_empty(self):
        result = operations.intersection(SUBSET_A, SUBSET_EMPTY)
        self.assertEqual(result, [False] * 12)

    # ---- Union ----
    
    #   u = [a, b, c, d, e, f, g, h, i, j, k, l]
    #   a = [a,    c,    e                     ]
    #   b = [   b, c, d                        ]
    # a∪b = [a, b, c, d, e                     ]
    def test_union_overlap(self):
        result = operations.union(SUBSET_A, SUBSET_B)
        expected = [
            True,  # a
            True,  # b
            True,  # c
            True,  # d
            True,  # e
            False,
            False,
            False,
            False,
            False,
            False,
            False,
        ]
        self.assertEqual(result, expected)

    #   u = [a, b, c, d, e, f, g, h, i, j, k, l]
    #   c = [               f, g               ]
    #   d = [                     h, i         ]
    # c∪d = [               f, g, h, i         ]
    def test_union_disjoint(self):
        result = operations.union(SUBSET_C, SUBSET_D)
        expected = [
            False,
            False,
            False,
            False,
            False,
            True,  # f
            True,  # g
            True,  # h
            True,  # i
            False,
            False,
            False,
        ]
        self.assertEqual(result, expected)

    #   u = [a, b, c, d, e, f, g, h, i, j, k, l]
    #   a = [a,    c,    e                     ]
    #   e = [                                  ]
    # a∪e = [a,    c,    e                     ]
    def test_union_with_empty(self):
        result = operations.union(SUBSET_A, SUBSET_EMPTY)
        expected = [
            True,  # a
            False,
            True,  # c
            False,
            True,  # e
            False,
            False,
            False,
            False,
            False,
            False,
            False,
        ]
        self.assertEqual(result, expected)

    # ---- Difference ----
    
    #   u = [a, b, c, d, e, f, g, h, i, j, k, l]
    #   a = [a,    c,    e                     ]
    #   b = [   b, c, d                        ]
    # a-b = [a,          e                     ]
    def test_difference_basic(self):
        result = operations.difference(SUBSET_A, SUBSET_B)
        expected = [
            True,  # a
            False,
            False,
            False,
            True,  # e
            False,
            False,
            False,
            False,
            False,
            False,
            False,
        ]
        self.assertEqual(result, expected)

    #   u = [a, b, c, d, e, f, g, h, i, j, k, l]
    #   c = [               f, g               ]
    #   d = [                     h, i         ]
    # c-d = [               f, g               ]
    def test_difference_disjoint(self):
        result = operations.difference(SUBSET_C, SUBSET_D)
        expected = [
            False,
            False,
            False,
            False,
            False,
            True,  # f
            True,  # g
            False,
            False,
            False,
            False,
            False,
        ]
        self.assertEqual(result, expected)

    #   u = [a, b, c, d, e, f, g, h, i, j, k, l]
    #   a = [a,    c,    e                     ]
    #   e = [                                  ]
    # a-e = [a,    c,    e                     ]
    def test_difference_with_empty(self):
        result = operations.difference(SUBSET_A, SUBSET_EMPTY)
        expected = [
            True,  # a
            False,
            True,  # c
            False,
            True,  # e
            False,
            False,
            False,
            False,
            False,
            False,
            False,
        ]
        self.assertEqual(result, expected)

    # ---- Symmetric Difference ----

    #    u = [a, b, c, d, e, f, g, h, i, j, k, l]
    #    a = [a,    c,    e                     ]
    #    b = [   b, c, d                        ]
    # a⊕b = [a, b,    d, e                     ]
    def test_symmetric_difference_overlap(self):
        result = operations.symmetricDifference(SUBSET_A, SUBSET_B)
        expected = [
            True,  # a
            True,  # b
            False,
            True,  # d
            True,  # e
            False,
            False,
            False,
            False,
            False,
            False,
            False,
        ]
        self.assertEqual(result, expected)

    #    u = [a, b, c, d, e, f, g, h, i, j, k, l]
    #    c = [               f, g               ]
    #    d = [                     h, i         ]
    # c⊕d = [               f, g, h, i         ]
    def test_symmetric_difference_disjoint(self):
        result = operations.symmetricDifference(SUBSET_C, SUBSET_D)
        expected = [
            False,
            False,
            False,
            False,
            False,
            True,  # f
            True,  # g
            True,  # h
            True,  # i
            False,
            False,
            False,
        ]
        self.assertEqual(result, expected)

    #    u = [a, b, c, d, e, f, g, h, i, j, k, l]
    #    a = [a,    c,    e                     ]
    #    e = [                                  ]
    # a⊕e = [a,    c,    e                     ]
    def test_symmetric_difference_with_empty(self):
        result = operations.symmetricDifference(SUBSET_A, SUBSET_EMPTY)
        expected = [
            True,  # a
            False,
            True,  # c
            False,
            True,  # e
            False,
            False,
            False,
            False,
            False,
            False,
            False,
        ]
        self.assertEqual(result, expected)


"""
Concrete example (no code)

Using the same U = [a, b, c, d, e, f, g, h, i, j], suppose:
A = {a, a, c, e, e, e, g} = {a×2, c×1, e×3, g×1}
B = {a, b, b, e, g, g, g, g} = {a×1, b×2, e×1, g×4}

Then (show results as counts per element, clearly labeled):
• A ∪ B: a×2, b×2, c×1, e×3, g×4
• A ∩ B: a×1, e×1, g×1
• A − B: a×1, c×1, e×2, g×0 (often omit ×0 in display)
• A + B: a×3, b×2, c×1, e×4, g×5
"""


if __name__ == "__main__":
    unittest.main()




```

    
    


