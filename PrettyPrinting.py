

def pprinted_actions(actions: list[str]):
    
    return "...\n" + "\n".join(a for a in actions) + "\n...\n"

def pprinted_res(n, results):
    return (f"n = {n}:\n" 
            f"max = {results[0]}; min = {results[1]}; avg = {results[2]}")