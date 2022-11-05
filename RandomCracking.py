
import random
from FiniteAutomaton import FAState


DEFAULT_PASSCODE = "23344" #"84985"
UNLOCK_CODE = "1"
LOCK_CODE = "4"

def randomCrack(PASSCODE: str = DEFAULT_PASSCODE):
    
    # whether it has been cracked
    cracked: bool = False
    # time in seconds
    guesses: int = 0 
    
    # start state (q0)
    q: int = FAState.NEUTRAL
    
    while (not cracked):
        
        # random guess
        letter: str = str(random.randint(0, 9))
        
        # print(f"letter: {letter}")
        
        guesses += 1
        
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
                
                if (letter == UNLOCK_CODE): # cracked
                    cracked = True
                    return guesses
                q = FAState.NEUTRAL
    
    
# Does n attacks
# Returns (maximum, minimum, average) time in seconds
def randomResults(
        n = 100, PASSCODE: 
        str = DEFAULT_PASSCODE
    ) -> tuple[int, int, float]:
    
    # results
    maximum: int = 0
    minimum: int = 0
    total: int = 0
    
    for _ in range(n):
        # time in seconds
        guesses: int = randomCrack(PASSCODE)
        
        total += guesses
        minimum = minimum if (minimum <= guesses and minimum > 0) else guesses
        maximum = maximum if (maximum >  guesses) else guesses
        
    # (maximum, minimum, average) 
    return (maximum, minimum, float(total)/n)
    
        
        
        