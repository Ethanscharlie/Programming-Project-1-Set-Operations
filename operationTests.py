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


def outputResults(operation: str, data:list[list[str]], result: list[bool] , expected: list[bool]):
    # Print what we're doing
    print("Performing " + operation + " operation on the following:")
    # Print data as str list
    for element in data:
        print("                  " + element.__str__())
    # Print data as bitstring
    for element in data:
        print("                  " + bitString(operations.setStrToBool(element)))
    # Print results
    print("                  -----------------------")
    print("Expected Result:  " + bitString(expected))
    print("Actual Result:    " + bitString(result))
    print("--------------------------------------------")


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
        # OUTPUT TEST RESULTS:
        outputResults("Complement", [SUBSET_A], result, expected)

    #      u = [a, b, c, d, e, f, g, h, i, j, k, l]
    #      e = [                                  ]
    # NOT(e) = [a, b, c, d, e, f, g, h, i, j, k, l]
    def test_complement_empty(self):
        result = operations.complement(SUBSET_EMPTY)
        expected = [True] * 12
        self.assertEqual(result, expected)
        # OUTPUT TEST RESULTS:
        outputResults("Complement", [SUBSET_EMPTY], result, expected)

    #      u = [a, b, c, d, e, f, g, h, i, j, k, l]
    # NOT(u) = [                                  ]
    def test_complement_full(self):
        result = operations.complement(operations.UNIVERSAL_SET)
        expected = [False] * 12
        self.assertEqual(result, expected)
        # OUTPUT TEST RESULTS:
        outputResults("Complement", [operations.UNIVERSAL_SET], result, expected)

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
        # OUTPUT TEST RESULTS:
        outputResults("Intersection", [SUBSET_A, SUBSET_B], result, expected)

    #   u = [a, b, c, d, e, f, g, h, i, j, k, l]
    #   c = [               f, g               ]
    #   d = [                     h, i         ]
    # c∩d = [                                  ]
    def test_intersection_disjoint(self):
        result = operations.intersection(SUBSET_C, SUBSET_D)
        expected = [False] * 12
        self.assertEqual(result, expected)
        # OUTPUT TEST RESULTS:
        outputResults("Intersection", [SUBSET_C, SUBSET_D], result, expected)

    #   u = [a, b, c, d, e, f, g, h, i, j, k, l]
    #   a = [a,    c,    e                     ]
    #   e = [                                  ]
    # a∩e = [                                  ]
    def test_intersection_with_empty(self):
        result = operations.intersection(SUBSET_A, SUBSET_EMPTY)
        expected = [False] * 12
        self.assertEqual(result, expected)
        # OUTPUT TEST RESULTS:
        outputResults("Intersection", [SUBSET_A, SUBSET_EMPTY], result, expected)

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
        # OUTPUT TEST RESULTS:
        outputResults("Union", [SUBSET_A, SUBSET_B], result, expected)

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
        outputResults("Union", [SUBSET_C, SUBSET_D], result, expected)

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
        # OUTPUT TEST RESULTS:
        outputResults("Union", [SUBSET_A, SUBSET_EMPTY], result, expected)

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
        # OUTPUT TEST RESULTS:
        outputResults("Difference", [SUBSET_A, SUBSET_B], result, expected)

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
        # OUTPUT TEST RESULTS:
        outputResults("Difference", [SUBSET_C, SUBSET_D], result, expected)

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
        # OUTPUT TEST RESULTS:
        outputResults("Difference", [SUBSET_A, SUBSET_EMPTY], result, expected)

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
        # OUTPUT TEST RESULTS:
        outputResults("Symmetric Difference", [SUBSET_A, SUBSET_B], result, expected)

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
        # OUTPUT TEST RESULTS:
        outputResults("Symmetric Difference", [SUBSET_C, SUBSET_D], result, expected)

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
        # OUTPUT TEST RESULTS:
        outputResults("Symmetric Difference", [SUBSET_A, SUBSET_EMPTY], result, expected)


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

