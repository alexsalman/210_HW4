#!/usr/bin/python3
# Alex Salman 2/5/2021 aalsalma@ucsc.edu
# resource:
# (1) https://ruslanspivak.com/lsbasi-part7/
# (2) https://ruslanspivak.com/lsbasi-part8/
# (3) https://ruslanspivak.com/lsbasi-part9/
# (4) https://github.com/versey-sherry/while/blob/master/parsewhile.py

from parser import *
from interpreter import *


def main():
    contents = []
    line = input()
    line = line.strip()
    line = " ".join(line.split())
    contents.append(line)

    text = ' '.join(contents)
    text = ' '.join(text.split())
    lexer = Lexer(text)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    interpreter.visit()
    step_list = interpreter.print_step
    step_list = [item for sublist in step_list for item in sublist]
    state_list = interpreter.print_state
    if text[0:5] == "skip;" or text[0:6] == "skip ;":
        del step_list[0]
        del state_list[0]

    step_list[-1] = 'skip'

    if len(state_list) > 10000:
        state_list = state_list[0:10000]
        step_list = step_list[0:10000]

    if len(state_list) ==1 and state_list[0] == {} and text[0:4] == "skip":
        print('')
    else:
        for i in range(len(state_list)):
            output_string = []
            for key in sorted(state_list[i]):
                separator = " "
                output_string.append(separator.join([key, "→", str(state_list[i][key])]))

            state_string = ''.join(["{", ", ".join(output_string), "}"])
            step_string = ' '.join(['⇒', step_list[i]])
            print(step_string, state_string, sep = ', ')


if __name__ == '__main__':
    main()
