
from FiniteAutomaton import FA, make_FA_logic

def run():
    
    print("\n\n")
    
    # one character at a time
    
    DEFAULT_PASSCODE = "84985"
    DEFAULT_UNLOCK_CODE = "1"
    DEFAULT_LOCK_CODE = "4"
    
    # set up FA
    _, transition_function, q0 = make_FA_logic(
        DEFAULT_PASSCODE,
        DEFAULT_UNLOCK_CODE,
        DEFAULT_LOCK_CODE
    )
    
    fa = FA(transition_function, q0)
    
    
    while (True):
        
        # get user input , 
        # feed input one character at a time to FA, 
        # print output
        print("".join(fa.next(letter) for letter in input("")), end="")
    
    
    
if (__name__ == "__main__"):
    run()