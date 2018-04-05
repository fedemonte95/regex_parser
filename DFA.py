class DFA:
    """
    This class is a small implementation of a Deterministic Finite Automata.
    """
    current_state = None

    def __init__(self, states, alphabet, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state
        self.transition_function = dict()
        self.add_transition_function()
        return

    def add_transition_function(self):
        """
            This function will add transition functions to your transition table (transition function dictionary in code)
            params: 
                * p_tuple
                * value
        """
        self.transition_function[(0, 'a')] = 1
        self.transition_function[(0, 'b')] = 2
        self.transition_function[(0, 'c')] = 3
        self.transition_function[(0, 'd')] = 0
        self.transition_function[(1, 'a')] = 1
        self.transition_function[(1, 'b')] = 2
        self.transition_function[(1, 'c')] = 3
        self.transition_function[(1, 'd')] = 0
        self.transition_function[(2, 'a')] = 1
        self.transition_function[(2, 'b')] = 2
        self.transition_function[(2, 'c')] = 3
        self.transition_function[(2, 'd')] = 0
        self.transition_function[(3, 'a')] = 1
        self.transition_function[(3, 'b')] = 2
        self.transition_function[(3, 'c')] = 3
        self.transition_function[(3, 'd')] = 0
        
    def transition_to_state_with_input(self, input_value):
        if (self.current_state, input_value) not in self.transition_function.keys():
            self.current_state = None
            return
        self.current_state = self.transition_function[(self.current_state, input_value)]
        return

    def in_accept_state(self):
        return self.current_state in self.accept_states

    def go_to_initial_state(self):
        self.current_state = self.start_state
        return

    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
            continue
        return self.in_accept_state()
    pass