
# An automaton can be represented by a 5-tuple (Q, ∑, δ, q0, F), where −

    #     Q is a finite set of states.
    #     states: { _0, _1, _2, _3, _4, CHECK, NEUTRAL }

    #     ∑ is a finite set of symbols, called the alphabet of the automaton.
    
    #     alphabet: { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }

    #     δ is the transition function.
    
    #       δ(NEUTRAL, '0') = NEUTRAL
    #       δ(NEUTRAL, '1') = NEUTRAL
    #       δ(NEUTRAL, '2') = NEUTRAL
    #       δ(NEUTRAL, '3') = NEUTRAL
    #       δ(NEUTRAL, '4') = NEUTRAL
    #       δ(NEUTRAL, '5') = NEUTRAL
    #       δ(NEUTRAL, '6') = NEUTRAL
    #       δ(NEUTRAL, '7') = NEUTRAL
    #       δ(NEUTRAL, '8') = _1
    #       δ(NEUTRAL, '9') = NEUTRAL
    #
    #       δ(_1, '0') = NEUTRAL
    #       δ(_1, '1') = NEUTRAL
    #       δ(_1, '2') = NEUTRAL
    #       δ(_1, '3') = NEUTRAL
    #       δ(_1, '4') = _2
    #       δ(_1, '5') = NEUTRAL
    #       δ(_1, '6') = NEUTRAL
    #       δ(_1, '7') = NEUTRAL
    #       δ(_1, '8') = NEUTRAL
    #       δ(_1, '9') = NEUTRAL
    #
    #       δ(_2, '0') = NEUTRAL
    #       δ(_2, '1') = NEUTRAL
    #       δ(_2, '2') = NEUTRAL
    #       δ(_2, '3') = NEUTRAL
    #       δ(_2, '4') = NEUTRAL
    #       δ(_2, '5') = NEUTRAL
    #       δ(_2, '6') = NEUTRAL
    #       δ(_2, '7') = NEUTRAL
    #       δ(_2, '8') = NEUTRAL
    #       δ(_2, '9') = _3
    #
    #       δ(_3, '0') = NEUTRAL
    #       δ(_3, '1') = NEUTRAL
    #       δ(_3, '2') = NEUTRAL
    #       δ(_3, '3') = NEUTRAL
    #       δ(_3, '4') = NEUTRAL
    #       δ(_3, '5') = NEUTRAL
    #       δ(_3, '6') = NEUTRAL
    #       δ(_3, '7') = NEUTRAL
    #       δ(_3, '8') = _4
    #       δ(_3, '9') = NEUTRAL
    #       
    #       δ(_4, '0') = NEUTRAL
    #       δ(_4, '1') = NEUTRAL
    #       δ(_4, '2') = NEUTRAL
    #       δ(_4, '3') = NEUTRAL
    #       δ(_4, '4') = NEUTRAL
    #       δ(_4, '5') = CHECK
    #       δ(_4, '6') = NEUTRAL
    #       δ(_4, '7') = NEUTRAL
    #       δ(_4, '8') = NEUTRAL
    #       δ(_4, '9') = NEUTRAL
    #
    #       δ(CHECK, '0') = NEUTRAL
    #       δ(CHECK, '1') = NEUTRAL
    #       δ(CHECK, '2') = NEUTRAL
    #       δ(CHECK, '3') = NEUTRAL
    #       δ(CHECK, '4') = NEUTRAL
    #       δ(CHECK, '5') = NEUTRAL
    #       δ(CHECK, '6') = NEUTRAL
    #       δ(CHECK, '7') = NEUTRAL
    #       δ(CHECK, '8') = NEUTRAL
    #       δ(CHECK, '9') = NEUTRAL


    #     q0 is the initial state from where any input is processed (q0 ∈ Q).

    #     F is a set of final state/states of Q (F ⊆ Q).
    #     final_states: { ? }

DEFAULT_PASSCODE = "23344" #"84985"
UNLOCK_CODE = "1"
LOCK_CODE = "4"

# states (Q)
class FAState:
    _1 = 1              # states that keep track of PASSCODE index
    _2 = 2         
    _3 = 4         
    _4 = 8         
    NEUTRAL = 16    # q0
    CHECK = 32      # checking to lock/unlock since PASSCODE was recognized  

def evaluate_code_verbose(
        input_string: str, 
        PASSCODE: str = DEFAULT_PASSCODE
    ) -> list[str]:
        
    """ Evaluate input string, record the locking/unlocking """
    
    record: list[str] = []
    
    # start state (q0)
    q: int = FAState.NEUTRAL
    
    for i, letter in enumerate(input_string):
        
        record.append(f"{i}: {q}   {letter}")
        
        match q:
            
            case FAState.NEUTRAL:
                
                if (letter == PASSCODE[0]):
                    q = FAState._1
                else:
                    q = FAState.NEUTRAL
                    
            case FAState._1:
                
                if (letter == PASSCODE[1]):
                    q = FAState._2
                else:
                    q = FAState.NEUTRAL
                    
            case FAState._2:
                
                if (letter == PASSCODE[2]):
                    q = FAState._3
                else:
                    q = FAState.NEUTRAL
                    
            case FAState._3:
                
                if (letter == PASSCODE[3]):
                    q = FAState._4
                else:
                    q = FAState.NEUTRAL
                    
            case FAState._4:
                
                if (letter == PASSCODE[4]):
                    q = FAState.CHECK
                else:
                    q = FAState.NEUTRAL
                    
                    
            case FAState.CHECK:
                
                if (letter == LOCK_CODE):
                    record.append(f"LOCK {i}")
                elif (letter == UNLOCK_CODE): 
                    record.append(f"UNLOCK {i}")
                q = FAState.NEUTRAL
                
    record.append(f"final: {q}")
    
    return record


def evaluate_code(
        input_string: str, 
        PASSCODE: str = DEFAULT_PASSCODE
    ) -> list[str]:
    
    return [r.split()[0] for r in evaluate_code_verbose(input_string, PASSCODE) 
            if (r.split()[0] == "LOCK" or r.split()[0] == "UNLOCK")]
    

def evaluate_code_with_side_effects(
        input_string: str, 
        PASSCODE: str = DEFAULT_PASSCODE
    ):
        
    """ Evaluate input string, record the locking/unlocking """
    
    # start state (q0)
    q: int = FAState.NEUTRAL
    
    for letter in input_string:
        
        match q:
            
            case FAState.NEUTRAL:
                
                if (letter == PASSCODE[0]):
                    q = FAState._1
                else:
                    q = FAState.NEUTRAL
                    
            case FAState._1:
                
                if (letter == PASSCODE[1]):
                    q = FAState._2
                else:
                    q = FAState.NEUTRAL
                    
            case FAState._2:
                
                if (letter == PASSCODE[2]):
                    q = FAState._3
                else:
                    q = FAState.NEUTRAL
                    
            case FAState._3:
                
                if (letter == PASSCODE[3]):
                    q = FAState._4
                else:
                    q = FAState.NEUTRAL
                    
            case FAState._4:
                
                if (letter == PASSCODE[4]):
                    q = FAState.CHECK
                else:
                    q = FAState.NEUTRAL
                    
                    
            case FAState.CHECK:
                
                if (letter == LOCK_CODE):
                    print("LOCK")
                elif (letter == UNLOCK_CODE): 
                    print("UNLOCK")
                q = FAState.NEUTRAL
                