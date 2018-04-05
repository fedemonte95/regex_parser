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
    tf = dict()
    tf[(0, 'a')] = 1
    tf[(0, 'b')] = 2
    tf[(0, 'c')] = 3
    tf[(0, 'd')] = 0
    tf[(1, 'a')] = 1
    tf[(1, 'b')] = 2
    tf[(1, 'c')] = 3
    tf[(1, 'd')] = 0
    tf[(2, 'a')] = 1
    tf[(2, 'b')] = 2
    tf[(2, 'c')] = 3
    tf[(2, 'd')] = 0
    tf[(3, 'a')] = 1
    tf[(3, 'b')] = 2
    tf[(3, 'c')] = 3
    tf[(3, 'd')] = 0
    d = DFA(states, alphabet, tf, start_state, accept_states)
    print("DFA result")
    inp_program = list('aaaaaaaaaaaaaa')
    print(d.run_with_input_list(inp_program))
    d.add_transition_function()
    print('el mio' ,d.transition_func_dic)
    print('el del codigo',d.transition_function)
    if d.transition_function == d.transition_func_dic:
        print('son iguales')
    else: 
        print('no son iguales')

    
    #print 'Number of arguments:', len(sys.argv), 'arguments.'
    #print 'Argument List:', str(sys.argv)
