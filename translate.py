def push_constant(const):
    return [
        # save const to D register
        '@' + str(const),
        'D=A',
        # write constant from D register to the stack. Effectively *SP=const
        '@SP',
        'A=M',
        'M=D',
        # increase the stack pointer: SP++
        '@SP',
        'M=M+1',
    ]
