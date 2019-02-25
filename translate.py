def push_constant(const):
    return [
        # save const to D register
        '@' + str(const),
        'D=A',
    ] + _push_d_register_to_stack()


def push_local(index):
   if index == 0:
       return [
            # save value of the first local segment memory cell to D register
            '@LCL',
            'D=M',
       ] + _push_d_register_to_stack()

   return [
        # save value of the 10th local segment memory cell to D register
        '@' + str(index),
        'D=A',
        '@LCL',
        'A=D+A',
        'D=M',
   ] + _push_d_register_to_stack()

def _push_d_register_to_stack():
    return [
        # write constant from D register to the stack.
        '@SP',
        'A=M',
        'M=D',
        # increase the stack pointer: SP++
        '@SP',
        'M=M+1',
    ]
