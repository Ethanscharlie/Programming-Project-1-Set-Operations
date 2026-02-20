import unittest

"""
Required output / testability constraints (Parts 1 & 2)
• Part 1 must use a universal set with n ≥ 10 elements.
• For Part 1 results, display BOTH: (1) bit string / Boolean array and (2) element-name listing.
• Include at least 2–3 representative test cases in your Results (not just one).
• For Part 2, ensure both A and B have at least two elements with multiplicity > 1.
• Clearly label outputs so ordinary set operations are not confused with multiset operations.
"""


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
    def test_demo(self):
        self.assertEqual(0, 1)


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


class TestPartTwo(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(0, 1)


if __name__ == "__main__":
    unittest.main()
