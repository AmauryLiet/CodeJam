import unittest
from .pb import solve


class Test(unittest.TestCase):
    def test_simple(self):
        input_lines = """
        1 2 3
        """.strip().split('\n')
        
        original_input = __builtins__.input
        original_print = __builtins__.print
        global line
        line = 0
        
        def mocked_input():
            global line
            line += 1
            return input_lines[line - 1]
        
        __builtins__.input = mocked_input
        __builtins__.print = mocked_print
        
        output = 0
        solve()
        
        __builtins__.input = original_input
        __builtins__.print = original_print


if __name__ == '__main__':
    unittest.main()
