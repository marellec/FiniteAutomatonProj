
import unittest
from FiniteAutomaton import FA, make_FA_logic

def default_fa_logic():
    
    """ Returns (automaton, Q, δ) """
    
    DEFAULT_PASSCODE = "84985"
    DEFAULT_UNLOCK_CODE = "1"
    DEFAULT_LOCK_CODE = "4"
    
    # set up FA
    return make_FA_logic(
        DEFAULT_PASSCODE,
        DEFAULT_UNLOCK_CODE,
        DEFAULT_LOCK_CODE
    )
    
def evaluate_default(input_str: str):
    
    _, transition_function, q0  = default_fa_logic()
    
    fa = FA(transition_function, q0)
    
    return tuple(output
                 for letter in input_str 
                 if (output := fa.next(letter)) != "")   



class Test(unittest.TestCase):
    
    # tf = δ = transition_function
    # logic = output of make_FA_logic() from FiniteAutomaton
    # evaluation = output of evaluate_default()
    
    # 
    def test_all_valid_inputs_tf(self):
        
        # tf = δ = transition_function
        States, tf, _ = default_fa_logic()
        
        # δ(q, letter) == (expected_q, expected_output)
        self.assertEqual(tf(States.NEUTRAL, '0'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States.NEUTRAL, '1'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States.NEUTRAL, '2'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States.NEUTRAL, '3'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States.NEUTRAL, '4'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States.NEUTRAL, '5'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States.NEUTRAL, '6'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States.NEUTRAL, '7'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States.NEUTRAL, '8'), (States._1, ""))
        self.assertEqual(tf(States.NEUTRAL, '9'), (States.NEUTRAL, ""))
        
        self.assertEqual(tf(States._1, '0'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._1, '1'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._1, '2'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._1, '3'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._1, '4'), (States._2, ""))
        self.assertEqual(tf(States._1, '5'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._1, '6'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._1, '7'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._1, '8'), (States._1, ""))
        self.assertEqual(tf(States._1, '9'), (States.NEUTRAL, ""))
        
        self.assertEqual(tf(States._2, '0'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._2, '1'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._2, '2'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._2, '3'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._2, '4'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._2, '5'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._2, '6'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._2, '7'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._2, '8'), (States._1, ""))
        self.assertEqual(tf(States._2, '9'), (States._3, ""))
        
        self.assertEqual(tf(States._3, '0'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._3, '1'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._3, '2'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._3, '3'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._3, '4'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._3, '5'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._3, '6'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._3, '7'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._3, '8'), (States._4, ""))
        self.assertEqual(tf(States._3, '9'), (States.NEUTRAL, ""))
        
        self.assertEqual(tf(States._4, '0'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._4, '1'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._4, '2'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._4, '3'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._4, '4'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._4, '5'), (States.CHECK, ""))
        self.assertEqual(tf(States._4, '6'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._4, '7'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States._4, '8'), (States._1, ""))
        self.assertEqual(tf(States._4, '9'), (States.NEUTRAL, ""))
        
        self.assertEqual(tf(States.CHECK, '0'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States.CHECK, '1'), (States.NEUTRAL, "UNLOCK\n"))
        self.assertEqual(tf(States.CHECK, '2'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States.CHECK, '3'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States.CHECK, '4'), (States.NEUTRAL, "LOCK\n"))
        self.assertEqual(tf(States.CHECK, '5'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States.CHECK, '6'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States.CHECK, '7'), (States.NEUTRAL, ""))
        self.assertEqual(tf(States.CHECK, '8'), (States._1, ""))
        self.assertEqual(tf(States.CHECK, '9'), (States.NEUTRAL, ""))
    
    #
    def test_ignored_inputs_tf(self):
        
        # tf = δ = transition_function
        States, tf, _ = default_fa_logic()
        
        for q in (States._1, States._2, States._3, States._4, States.NEUTRAL, States.CHECK):
            # δ(q, letter) == (expected_q, expected_output)
            self.assertEqual(tf(q, 'A'), (q, ""))
            self.assertEqual(tf(q, 'Q'), (q, ""))
            self.assertEqual(tf(q, '%'), (q, ""))
            self.assertEqual(tf(q, '_'), (q, ""))
            self.assertEqual(tf(q, '\n'), (q, ""))
            self.assertEqual(tf(q, ' '), (q, ""))
        
    #
    def test_no_input_evaluation(self):
        
        # no input
        self.assertEqual(
            tuple(), evaluate_default("")
        )
        
    #
    def test_initial_state_logic(self):
        
        States, _, q0 = default_fa_logic()
        
        self.assertEqual(q0, States.NEUTRAL)
        
        
        
    # redundant
    
    def test_routine(self):
        
        # routine, one lock/unlock
        self.assertEqual(
            ("UNLOCK\n",), 
            evaluate_default("1234849851345727")
        )
        
        self.assertEqual(
            ("LOCK\n",), 
            evaluate_default("1234849854345727")
        )
        
    def test_beg_end(self):
        
        # beginning/ending with a lock/unlock
        self.assertEqual(
            ("UNLOCK\n",), 
            evaluate_default("8498511234345727",)
        )
        
        self.assertEqual(
            ("UNLOCK\n",), 
            evaluate_default("1234345727849851")
        )
        
        self.assertEqual(
            ("LOCK\n",), 
            evaluate_default("8498541234345727")
        )
        
        self.assertEqual(
            ("LOCK\n",), 
            evaluate_default("1234345727849854")
        )
        
        self.assertEqual(
            ("UNLOCK\n", "LOCK\n"), 
            evaluate_default("8498511234345727849854")
        )
        
    def test_offset(self):
        
        # lock/unlock code is offset from passcode
        self.assertEqual(
            tuple(), evaluate_default("12348498561345727")
        )
        
        self.assertEqual(
            tuple(), evaluate_default("12348498564345727")
        )
        
    def test_breakup(self):
        
        # passcode is broken up
        self.assertEqual(
            tuple(), evaluate_default("12348449851345727")
        )
        
        self.assertEqual(
            tuple(), evaluate_default("12348449854345727")
        )
        
    def test_multiple(self):
        
        # multiple lock/unlock combos
        self.assertEqual(
            ("UNLOCK\n", "LOCK\n", "UNLOCK\n"), 
            evaluate_default("913520849851245108498541239700011184985518498510101")
        )
        
        self.assertEqual(
            ("LOCK\n", "UNLOCK\n", "LOCK\n"), 
            evaluate_default("93746856417509708538498542328499675584985135274996643232638400102736526243849854")
        )
        
    def test_other_chars(self):
        
        # non-integers
        self.assertEqual(
            ("LOCK\n", "UNLOCK\n", "LOCK\n"), 
            evaluate_default("247064394e5408498549454830rhf0nu8498510r80r3804ri48y0489849854240489429y7frh498")
        )
        
      
    def test_other(self):
        
        # many
        self.assertEqual(
            ("UNLOCK\n", "LOCK\n", "UNLOCK\n"), 
            evaluate_default("84985191352ac084985712451084985412397bce0001118498551849851...0101")
        )
        
        self.assertEqual(
            ("LOCK\n", "UNLOCK\n", "LOCK\n"), 
            evaluate_default("937%%%%468564175097//0853849,85423284996755jajaja8498513527499g6g64323200102736526243jk849854")
        )
        
        
        
if __name__ == "__main__":
    unittest.main()