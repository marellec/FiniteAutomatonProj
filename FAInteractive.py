
from FiniteAutomaton import evaluate_code_with_side_effects


def run():
    
    evaluate_code_with_side_effects(
        input("\nENTER STRING: ")
    )
    print()
    
if (__name__ == "__main__"):
    run()