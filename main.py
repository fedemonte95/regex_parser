from DFA import DFA
import sys


def read_file():
    """
    This functions reads a file text line by line
    :return: NULL
    """
    print("Reading file...")
    fh = open('file_to_read.txt')
    for line in fh:
        for character in line:
            print(character)
    fh.close()


if __name__ == "__main__":
    
    #read_file()
    states = {0, 1, 2, 3}
    alphabet = {'a', 'b', 'c', 'd'}
    start_state = 0
    accept_states = {2, 3}

    d = DFA(states, alphabet, start_state, accept_states)

    print("DFA result")
    inp_program = list('aaaaaaaaaaaaaa')
    print(d.run_with_input_list(inp_program))
    
    #print 'Number of arguments:', len(sys.argv), 'arguments.'
    #print 'Argument List:', str(sys.argv)
