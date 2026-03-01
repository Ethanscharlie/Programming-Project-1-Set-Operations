import operations
from operations import Multiset, SubSet
import unittest


SUBSET_A = ["a", "c", "e"]
SUBSET_B = ["b", "c", "d"]
SUBSET_C = ["f", "g"]
SUBSET_D = ["h", "i"]
SUBSET_EMPTY = []

# Authors: Christopher Reynolds & Ethan J. Hadley


def bitString(binary: list[bool]) -> str:
    """
    Convert a list of boolean values into a string.

    Args:
        binary (list[bool]): List of booleans.

    Returns:
        str: String of 0 or 1 seperated by spaces.
    """
    return " ".join(["1" if b else "0" for b in binary])


def outputResultsP1(
    operation: str, data: list[SubSet], result: list[bool], expected: list[bool]
) -> None:
    """Prints a comparison of expected and actual results for part 1.

    Args:
        operation: The name of the operation being performed.
        data: A list of subsets containing the input for the operation.
        result: A list of boolean values representing the actual output of
            the operation.
        expected: A list of boolean values representing the expected output
            for comparison.
    """

    print("Performing " + operation + " operation on the following:")

    for element in data:
        print(" " * 18 + str(element))

    for element in data:
        print(" " * 18 + bitString(operations.setStrToBool(element)))

    print("                  -----------------------")
    print("Expected Result:  " + bitString(expected))
    print("Actual Result:    " + bitString(result))
    print("--------------------------------------------")


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
        outputResultsP1("Complement", [SUBSET_A], result, expected)

    #      u = [a, b, c, d, e, f, g, h, i, j, k, l]
    #      e = [                                  ]
    # NOT(e) = [a, b, c, d, e, f, g, h, i, j, k, l]
    def test_complement_empty(self):
        result = operations.complement(SUBSET_EMPTY)
        expected = [True] * 12
        self.assertEqual(result, expected)
        outputResultsP1("Complement", [SUBSET_EMPTY], result, expected)

    #      u = [a, b, c, d, e, f, g, h, i, j, k, l]
    # NOT(u) = [                                  ]
    def test_complement_full(self):
        result = operations.complement(operations.UNIVERSAL_SET)
        expected = [False] * 12
        self.assertEqual(result, expected)
        outputResultsP1("Complement", [operations.UNIVERSAL_SET], result, expected)

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
        outputResultsP1("Intersection", [SUBSET_A, SUBSET_B], result, expected)

    #   u = [a, b, c, d, e, f, g, h, i, j, k, l]
    #   c = [               f, g               ]
    #   d = [                     h, i         ]
    # c∩d = [                                  ]
    def test_intersection_disjoint(self):
        result = operations.intersection(SUBSET_C, SUBSET_D)
        expected = [False] * 12
        self.assertEqual(result, expected)
        outputResultsP1("Intersection", [SUBSET_C, SUBSET_D], result, expected)

    #   u = [a, b, c, d, e, f, g, h, i, j, k, l]
    #   a = [a,    c,    e                     ]
    #   e = [                                  ]
    # a∩e = [                                  ]
    def test_intersection_with_empty(self):
        result = operations.intersection(SUBSET_A, SUBSET_EMPTY)
        expected = [False] * 12
        self.assertEqual(result, expected)
        outputResultsP1("Intersection", [SUBSET_A, SUBSET_EMPTY], result, expected)

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
        outputResultsP1("Union", [SUBSET_A, SUBSET_B], result, expected)

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
        # OUTPUT TEST RESULTS:
        outputResultsP1("Union", [SUBSET_C, SUBSET_D], result, expected)

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
        outputResultsP1("Union", [SUBSET_A, SUBSET_EMPTY], result, expected)

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
        outputResultsP1("Difference", [SUBSET_A, SUBSET_B], result, expected)

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
        outputResultsP1("Difference", [SUBSET_C, SUBSET_D], result, expected)

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
        outputResultsP1("Difference", [SUBSET_A, SUBSET_EMPTY], result, expected)

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
        outputResultsP1("Symmetric Difference", [SUBSET_A, SUBSET_B], result, expected)

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
        outputResultsP1("Symmetric Difference", [SUBSET_C, SUBSET_D], result, expected)

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
        outputResultsP1(
            "Symmetric Difference", [SUBSET_A, SUBSET_EMPTY], result, expected
        )


# u =      a   b   c   d   e   f   g   h   i   j   k   l
# A =     {a:2     c:3     e:1                            }
# B =     {b:5     c:2 d:3                                }
# C =     {                    f:7 g:2                    }
# D =     {                            h:3 i:4            }
# EMPTY = {                                               }
MULTISET_A = {"a": 2, "c": 3, "e": 1}
MULTISET_B = {"b": 5, "c": 2, "d": 3}
MULTISET_C = {"f": 7, "g": 2}
MULTISET_D = {"h": 3, "i": 4}
MULTISET_EMPTY = {}


def outputResultsP2(
    operation: str, data: list[Multiset], result: Multiset, expected: Multiset
) -> None:
    """Prints a comparison of expected and actual results for part 2.

    Args:
        operation: The name of the operation being performed.
        data: A Multiset containing the input elements for the operation.
        result: A multiset representing the actual output of the operation.
        expected: A multiset representing the expected output for comparison.
    """

    print("Performing " + operation + " operation on the following:")

    for element in data:
        print(" " * 18 + str(operations.getTheZeroes(element)))

    print("Expected Result:  " + str(expected))
    print("Actual Result:    " + str(result))
    print("--------------------------------------------")


class TestPartTwo(unittest.TestCase):
    # ---- Intersection ----

    #          a   b   c   d   e   f   g   h   i   j   k   l
    # A =     {a:2     c:3     e:1                            }
    # B =     {    b:5 c:2 d:3                                }
    # A∩B =   {        c:2                                    }
    def test_intersection_overlap(self):
        result = operations.multisetIntersection(MULTISET_A, MULTISET_B)
        expected = {
            "a": 0,
            "b": 0,
            "c": 2,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
        }
        self.assertEqual(result, expected)
        outputResultsP2("Intersection", [MULTISET_A, MULTISET_B], result, expected)

    #          a   b   c   d   e   f   g   h   i   j   k   l
    # C =     {                    f:7 g:2                    }
    # D =     {                            h:3 i:4            }
    # C∩D =   {                                               }
    def test_intersection_disjoint(self):
        result = operations.multisetIntersection(MULTISET_C, MULTISET_D)
        expected = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
        }
        self.assertEqual(result, expected)
        outputResultsP2("Intersection", [MULTISET_C, MULTISET_D], result, expected)

    #          a   b   c   d   e   f   g   h   i   j   k   l
    # A =     {a:2     c:3     e:1                            }
    # EMPTY = {                                               }
    # A∩E =   {                                               }
    def test_intersection_with_empty(self):
        result = operations.multisetIntersection(MULTISET_A, MULTISET_EMPTY)
        expected = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
        }
        self.assertEqual(result, expected)
        outputResultsP2("Intersection", [MULTISET_A, MULTISET_EMPTY], result, expected)

    # ---- Union ----

    #          a   b   c   d   e   f   g   h   i   j   k   l
    # A =     {a:2     c:3     e:1                            }
    # B =     {    b:5 c:2 d:3                                }
    # A∪B =   {a:2 b:5 c:3 d:3 e:1                            }
    def test_union_overlap(self):
        result = operations.multisetUnion(MULTISET_A, MULTISET_B)
        expected = {
            "a": 2,
            "b": 5,
            "c": 3,
            "d": 3,
            "e": 1,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
        }
        self.assertEqual(result, expected)
        outputResultsP2("Union", [MULTISET_A, MULTISET_B], result, expected)

    #          a   b   c   d   e   f   g   h   i   j   k   l
    # C =     {                    f:7 g:2                    }
    # D =     {                            h:3 i:4            }
    # C∪D =   {                    f:7 g:2 h:3 i:4            }
    def test_union_disjoint(self):
        result = operations.multisetUnion(MULTISET_C, MULTISET_D)
        expected = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 7,
            "g": 2,
            "h": 3,
            "i": 4,
            "j": 0,
            "k": 0,
            "l": 0,
        }
        self.assertEqual(result, expected)
        outputResultsP2("Union", [MULTISET_C, MULTISET_D], result, expected)

    #          a   b   c   d   e   f   g   h   i   j   k   l
    # A =     {a:2     c:3     e:1                            }
    # EMPTY = {                                               }
    # A∪E =   {a:2     c:3     e:1                            }
    def test_union_with_empty(self):
        result = operations.multisetUnion(MULTISET_A, MULTISET_EMPTY)
        expected = {
            "a": 2,
            "b": 0,
            "c": 3,
            "d": 0,
            "e": 1,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
        }
        self.assertEqual(result, expected)
        outputResultsP2("Union", [MULTISET_A, MULTISET_EMPTY], result, expected)

    # ---- Difference ----

    #          a   b   c   d   e   f   g   h   i   j   k   l
    # A =     {a:2     c:3     e:1                            }
    # B =     {    b:5 c:2 d:3                                }
    # A-B =   {a:2     c:1     e:1                            }
    def test_difference_basic(self):
        result = operations.multisetDifference(MULTISET_A, MULTISET_B)
        expected = {
            "a": 2,
            "b": 0,
            "c": 1,
            "d": 0,
            "e": 1,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
        }
        self.assertEqual(result, expected)
        outputResultsP2("Difference", [MULTISET_A, MULTISET_B], result, expected)

    #          a   b   c   d   e   f   g   h   i   j   k   l
    # C =     {                    f:7 g:2                    }
    # D =     {                            h:3 i:4            }
    # C-D =   {                    f:7 g:2                    }
    def test_difference_disjoint(self):
        result = operations.multisetDifference(MULTISET_C, MULTISET_D)
        expected = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 7,
            "g": 2,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
        }
        self.assertEqual(result, expected)
        outputResultsP2("Difference", [MULTISET_C, MULTISET_D], result, expected)

    #          a   b   c   d   e   f   g   h   i   j   k   l
    # A =     {a:2     c:3     e:1                            }
    # EMPTY = {                                               }
    # A-E =   {a:2     c:3     e:1                            }
    def test_difference_with_empty(self):
        result = operations.multisetDifference(MULTISET_A, MULTISET_EMPTY)
        expected = {
            "a": 2,
            "b": 0,
            "c": 3,
            "d": 0,
            "e": 1,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
        }
        self.assertEqual(result, expected)
        outputResultsP2("Difference", [MULTISET_A, MULTISET_EMPTY], result, expected)

    # ---- Sum ----

    #          a   b   c   d   e   f   g   h   i   j   k   l
    # A =     {a:2     c:3     e:1                            }
    # B =     {    b:5 c:2 d:3                                }
    # A+B =   {a:2 b:5 c:5 d:3 e:1                            }
    def test_symmetric_difference_overlap(self):
        result = operations.multisetSum(MULTISET_A, MULTISET_B)
        expected = {
            "a": 2,
            "b": 5,
            "c": 5,
            "d": 3,
            "e": 1,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
        }
        self.assertEqual(result, expected)
        outputResultsP2("Sum", [MULTISET_A, MULTISET_B], result, expected)

    #          a   b   c   d   e   f   g   h   i   j   k   l
    # C =     {                    f:7 g:2                    }
    # D =     {                            h:3 i:4            }
    # C+D =   {                    f:7 g:2 h:3 i:4            }
    def test_symmetric_difference_disjoint(self):
        result = operations.multisetSum(MULTISET_C, MULTISET_D)
        expected = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 7,
            "g": 2,
            "h": 3,
            "i": 4,
            "j": 0,
            "k": 0,
            "l": 0,
        }
        self.assertEqual(result, expected)
        outputResultsP2("Sum", [MULTISET_C, MULTISET_D], result, expected)

    #          a   b   c   d   e   f   g   h   i   j   k   l
    # A =     {a:2     c:3     e:1                            }
    # EMPTY = {                                               }
    # A+E =   {a:2     c:3     e:1                            }
    def test_symmetric_difference_with_empty(self):
        result = operations.multisetSum(MULTISET_A, MULTISET_EMPTY)
        expected = {
            "a": 2,
            "b": 0,
            "c": 3,
            "d": 0,
            "e": 1,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
        }
        self.assertEqual(result, expected)
        outputResultsP2("Sum", [MULTISET_A, MULTISET_EMPTY], result, expected)


if __name__ == "__main__":
    unittest.main()
