
from RandomCracking import randomResults
from PrettyPrinting import pprinted_res

# what are the unit tests for?
# how to do part 2
# how to test the output on their machine
# is my code valid
# what is a language

def run():
    
    n_res: str = ""
    is_number: bool = False
    
    while (not is_number):
        n_res = input("\nENTER TRIAL COUNT: ")
        
        try:
            int(n_res)
            is_number = True
        except ValueError:
            print("\n    That isn't a number.")
    
    n: int = int(n_res)
    
    print("\nrunning\n...")
    print(pprinted_res(n, randomResults(n)))
    print("...")
    
    
if (__name__ == "__main__"):
    run()
    
