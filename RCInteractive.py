
from RandomCracking import randomResults
from PrettyPrinting import pprinted_res

# what are the unit tests for?
# how to do part 2
# how to test the output on their machine
# is my code valid
# what is a language

def run():
    
    DEFAULT_PASSCODE = "84985"
    DEFAULT_UNLOCK_CODE = "1"
    DEFAULT_LOCK_CODE = "4"
    
    # user trial count input
    n_response: str = ""
    is_number: bool = False
    
    while (not is_number):
        
        n_response = input("\nENTER TRIAL COUNT: ")
        
        # check for valid number
        try:
            int(n_response)
            is_number = True
        except ValueError:
            print("\n    That isn't a number.")
    
    # parse response
    n: int = int(n_response)
    
    print("\nrunning\n...")
    print(
        pprinted_res(n, 
            randomResults(
                n,
                DEFAULT_PASSCODE,
                DEFAULT_UNLOCK_CODE,
                DEFAULT_LOCK_CODE
            )
        )
    )
    print("...")
    
    
if (__name__ == "__main__"):
    run()
    
