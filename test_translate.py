import unittest
from translate import push_constant

class TranslateTestCase(unittest.TestCase):

    def test_translate_push_min_constant(self):
        # when
        asm_cmds = push_constant(0)
        # then
        self.assertEqual(asm_cmds, [
            # save 0 to D register
            '@0',
            'D=A',
            # write constant from D register to the stack. Effectively *SP=0
            '@SP',
            'A=M',
            'M=D',
            # increase the stack pointer: SP++
            '@SP',
            'M=M+1',
        ])

    def test_translate_push_max_constant(self):
        # when
        asm_cmds = push_constant(32767)
        # then
        self.assertEqual(asm_cmds, [
            # save 32767 to D register
            '@32767',
            'D=A',
            # write constant from D register to the stack. Effectively *SP=32767
            '@SP',
            'A=M',
            'M=D',
            # increase the stack pointer: SP++
            '@SP',
            'M=M+1',
        ])


if __name__ == '__main__':
    unittest.main()
