"""
    A test python file for our const keyword
"""

import unittest

class TestConst(unittest.TestCase):

    def test_normal_vars_function_normally(self):
        x = 5
        self.assertEqual(x, 5)
        x += 1
        self.assertEqual(x, 6)

    def test_normal_vars_cannot_become_const(self):
        x = 5
        with self.assertRaises(Exception):
            const x = 6

    def test_const_statement_can_only_be_used_with_name_assignments(self):
        pass
        # TODO: fix this test
    #     x = [1, 2, 3]
    #     class Klass():
    #         pass
    #     y = Klass()

    #     const y = 5
    #     self.assertEqual(y, 5)
    #     with self.assertRaises(SyntaxError):
    #         const x[3] = 10
    #     with self.assertRaises(SyntaxError):
    #         const y.x = 10
    #     with self.assertRaises(SyntaxError):
    #         const 9 = 10
    #     with self.assertRaises(SyntaxError):
    #         const x += 4

    def test_const_vars_can_only_be_assigned_compile_time_readable_values(self):
        pass
        # TODO: do we want to do this?

    def test_const_vars_can_be_read_by_other_variables(self):
        const y = 6
        self.assertEqual(y, 6)
        x = 5
        z = x + y
        self.assertEqual(z, 11)

    def test_const_vars_cannot_be_reassigned(self):
        const y = 6
        with self.assertRaises(Exception):
            y += 1
        self.assertEqual(y, 6)

    def test_const_scope(self):
        pass
        # TODO: fill in some tests that look at the scope of const vars

if __name__ == '__main__':
    unittest.main()