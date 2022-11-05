

DEFAULT_PASSCODE = "84985"
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
                