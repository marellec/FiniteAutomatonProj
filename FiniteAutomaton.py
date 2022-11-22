
class FA:
    
    def __init__(self, transition_function, q0) -> None:
        self.state = q0
        self.transition_function = transition_function
        
    def next(self, input_val):
        # update state and return output
        # using transition function
        self.state, output_val = self.transition_function(self.state, input_val)
        return output_val
    

def make_FA_logic(
    PASSCODE: str,
    UNLOCK_CODE: str,
    LOCK_CODE: str
):
    class FAStates:
        _1 = 1          # states that keep track of PASSCODE index
        _2 = 2         
        _3 = 4         
        _4 = 8         
        NEUTRAL = 16    # q0
        CHECK = 32      # checking to lock/unlock since PASSCODE was recognized  
    
    """ Returns (Q, δ, q0) """
    
    def transition_function(
        q: int,
        letter: str, 
    ):
            
        """  """
        
        if q == FAStates.NEUTRAL:
                
            if (letter == PASSCODE[0]):
                return (FAStates._1, "")
            elif (letter.isdigit()):
                return (FAStates.NEUTRAL, "")
            else:
                return (q, "")
                    
        elif q == FAStates._1:
            
            if (letter == PASSCODE[1]):
                return (FAStates._2, "")
            elif (letter == PASSCODE[0]):
                return (FAStates._1, "")
            elif (letter.isdigit()):
                return (FAStates.NEUTRAL, "")
            else:
                return (q, "")
                    
        elif q ==FAStates._2:
                
            if (letter == PASSCODE[2]):
                return (FAStates._3, "")
            elif (letter == PASSCODE[0]):
                return (FAStates._1, "")
            elif (letter.isdigit()):
                return (FAStates.NEUTRAL, "")
            else:
                return (q, "")
                    
        elif q ==FAStates._3:
                
            if (letter == PASSCODE[3]):
                return (FAStates._4, "")
            elif (letter == PASSCODE[0]):
                return (FAStates._1, "")
            elif (letter.isdigit()):
                return (FAStates.NEUTRAL, "")
            else:
                return (q, "")
                    
        elif q ==FAStates._4:
                
            if (letter == PASSCODE[4]):
                return (FAStates.CHECK, "")
            elif (letter == PASSCODE[0]):
                return (FAStates._1, "")
            elif (letter.isdigit()):
                return (FAStates.NEUTRAL, "")
            else:
                return (q, "")
            
        elif q ==FAStates.CHECK:
                
            if (letter == LOCK_CODE):
                return (FAStates.NEUTRAL, "LOCK\n")
            elif (letter == UNLOCK_CODE): 
                return (FAStates.NEUTRAL, "UNLOCK\n")
            elif (letter == PASSCODE[0]):
                return (FAStates._1, "")
            elif (letter.isdigit()):
                return (FAStates.NEUTRAL, "")
            else:
                return (q, "")
    
    return (FAStates, transition_function, FAStates.NEUTRAL)






    


                