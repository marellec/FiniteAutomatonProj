
import unittest

from FiniteAutomaton import evaluate_code

class Test(unittest.TestCase):
    
    def test_routine(self):
        
        # routine, one lock/unlock
        self.assertEqual(
            ["UNLOCK"], 
            evaluate_code(
                "1234849851345727",
                "84985"
            )
        )
        
        self.assertEqual(
            ["LOCK"], 
            evaluate_code(
                "1234849854345727",
                "84985"
            )
        )
        
    def test_beg_end(self):
        
        # beginning/ending with a lock/unlock
        self.assertEqual(
            ["UNLOCK"], 
            evaluate_code(
                "8498511234345727",
                "84985"
            )
        )
        
        self.assertEqual(
            ["UNLOCK"], 
            evaluate_code(
                "1234345727849851",
                "84985"
            )
        )
        
        self.assertEqual(
            ["LOCK"], 
            evaluate_code(
                "8498541234345727",
                "84985"
            )
        )
        
        self.assertEqual(
            ["LOCK"], 
            evaluate_code(
                "1234345727849854",
                "84985"
            )
        )
        
        self.assertEqual(
            ["UNLOCK", "LOCK"], 
            evaluate_code(
                "8498511234345727849854",
                "84985"
            )
        )
        
    def test_offset(self):
        
        # lock/unlock code is offset from passcode
        self.assertEqual(
            [], 
            evaluate_code(
                "12348498561345727",
                "84985"
            )
        )
        
        self.assertEqual(
            [], 
            evaluate_code(
                "12348498564345727",
                "84985"
            )
        )
        
    def test_breakup(self):
        
        # passcode is broken up
        self.assertEqual(
            [], 
            evaluate_code(
                "12348449851345727",
                "84985"
            )
        )
        
        self.assertEqual(
            [], 
            evaluate_code(
                "12348449854345727",
                "84985"
            )
        )
        
    def test_multiple(self):
        
        # multiple lock/unlock combos
        self.assertEqual(
            ["UNLOCK", "LOCK", "UNLOCK"], 
            evaluate_code(
                "913520849851245108498541239700011184985518498510101",
                "84985"
            )
        )
        
        self.assertEqual(
            ["LOCK", "UNLOCK", "LOCK"], 
            evaluate_code(
                "93746856417509708538498542328499675584985135274996643232638400102736526243849854",
                "84985"
            )
        )
        
    def test_invalid_chars(self):
        
        # non-integers
        self.assertEqual(
            ["UNLOCK"], 
            evaluate_code(
                "ABCDE233441G",
                "23344"
            )
        )
        
        self.assertEqual(
            ["LOCK", "UNLOCK", "LOCK"], 
            evaluate_code(
                "247064394e5408498549454830rhf0nu8498510r80r3804ri48y0489849854240489429y7frh498",
                "84985"
            )
        )
        
        # no input
        self.assertEqual(
            [], 
            evaluate_code(
                ""
            )
        )
    
    def test_other_passcodes(self):
        
        # other passcodes
        self.assertEqual(
            ["UNLOCK", "LOCK", "UNLOCK"], 
            evaluate_code(
                "913520233441245102334441239700011123344512334410101", 
                "23344"
            )
        )
    
    def test_exhaust(self):
        
        # many
        self.assertEqual(
            ["UNLOCK", "LOCK", "UNLOCK"], 
            evaluate_code(
                "84985191352ac084985712451084985412397bce0001118498551849851...0101",
                "84985"
            )
        )
        
        self.assertEqual(
            ["UNLOCK", "LOCK"], 
            evaluate_code(
                "937%%%%468564175097//0853849,85423284996755jajaja8498513527499g6g64323200102736526243jk849854",
                "84985"
            )
        )
        
        
        
if __name__ == "__main__":
    unittest.main()