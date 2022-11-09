
import random
from FiniteAutomaton import FA, make_FA_logic

def randomCrack(
    PASSCODE: str,
    UNLOCK_CODE: str,
    LOCK_CODE: str
):
    
    # whether it has been cracked
    cracked: bool = False
    # time in seconds
    guesses: int = 0 
    
    
    _, transition_function, q0 = make_FA_logic(
        PASSCODE, 
        UNLOCK_CODE,
        LOCK_CODE
    )
    
    fa = FA(transition_function, q0)
    
    
    while (not cracked):
        
        # random guess
        letter: str = str(random.randint(0, 9))
        guesses += 1
        
        # FA output
        output = fa.next(letter)
        
        if (output == "UNLOCK\n"):
            cracked = True
            return guesses

# Does n attacks
# Returns (maximum, minimum, average) time in seconds
def randomResults(
        n, 
        PASSCODE: str,
        UNLOCK_CODE: str,
        LOCK_CODE: str
    ) -> tuple[int, int, float]:
    
    # results
    maximum: int = 0
    minimum: int = 0
    total: int = 0
    
    for _ in range(n):
        # time in seconds
        guesses: int = randomCrack(PASSCODE, UNLOCK_CODE, LOCK_CODE)
        
        total += guesses
        minimum = minimum if (minimum <= guesses and minimum > 0) else guesses
        maximum = maximum if (maximum >  guesses) else guesses
        
    # (maximum, minimum, average) 
    return (maximum, minimum, float(total)/n)
    
        
        
        