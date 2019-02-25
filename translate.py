def push_constant(const):
    return [
        # save const to D register
        '@' + str(const),
        'D=A',
    ] + _push_d_register_to_stack()


def push_local(index):
    return _push('LCL', index)


def push_that(index):
    return _push('THAT', index)


def push_this(index):
    return _push('THIS', index)


def push_argument(index):
    return _push('ARG', index)


def _push(segment, index):
   if index == 0:
       return [
            # save value of the first segment memory cell to D register
            '@' + segment,
            'D=M',
       ] + _push_d_register_to_stack()
   return [
        # save value of the n-th segment memory cell to D register
        '@' + str(index),
        'D=A',
        '@' + segment,
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
