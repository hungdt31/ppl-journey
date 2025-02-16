"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""
import sys
import os
import unittest
import inspect

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
   
    def test_001(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("if","if,<EOF>", inspect.stack()[0].function))

    def test_002(self):
        """Operators"""
        self.assertTrue(TestLexer.test("+","+,<EOF>", inspect.stack()[0].function))
        
    def test_003(self):
        """Separators"""
        self.assertTrue(TestLexer.test("[]","[,],<EOF>", inspect.stack()[0].function))
        
    def test_004(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("_VOTien","_VOTien,<EOF>", inspect.stack()[0].function))
        
    def test_005(self):
        """Literals INT"""
        self.assertTrue(TestLexer.test("12","12,<EOF>", inspect.stack()[0].function))
        
    def test_006(self):
        """Literals INT 16*1 + 1 = 17"""
        self.assertTrue(TestLexer.test("0x11","0x11,<EOF>", inspect.stack()[0].function))
    
    def test_007(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("12.e-8","12.e-8,<EOF>", inspect.stack()[0].function))
    
    def test_008(self):
        """Literals String"""
        self.assertTrue(TestLexer.test(""" "VOTIEN \\r" ""","\"VOTIEN \\r\",<EOF>", inspect.stack()[0].function))
        
    def test_009(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.test("// VOTIEN","<EOF>", inspect.stack()[0].function))

    def test_010(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.test("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", inspect.stack()[0].function))

    def test_011(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.test("^","ErrorToken ^", inspect.stack()[0].function))

    def test_012(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.test(""" "VOTIEN\n" ""","Unclosed string: \"VOTIEN", inspect.stack()[0].function))
    
    def test_013(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.test(""" "VOTIEN\\f" ""","Illegal escape in string: \"VOTIEN\\f", inspect.stack()[0].function))
        
    #!!! 87 test yêu cầu code chấm sau
    def test_014(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("else for return func type struct interface string int float boolean const var continue break range nil true false", "else,for,return,func,type,struct,interface,string,int,float,boolean,const,var,continue,break,range,nil,true,false,<EOF>", inspect.stack()[0].function))

    def test_015(self):
        """Operators"""
        self.assertTrue(TestLexer.test("+ - * / % == != > < <= >= && || ! = += -= *= /= %= :=", "+,-,*,/,%,==,!=,>,<,<=,>=,&&,||,!,=,+=,-=,*=,/=,%=,:=,<EOF>", inspect.stack()[0].function))

    def test_016(self):
        """Separators"""
        self.assertTrue(TestLexer.test("{}[](),;", "{,},[,],(,),,,;,<EOF>", inspect.stack()[0].function))

    def test_017(self):
        """skip"""
        self.assertTrue(TestLexer.test("\t\f\r ", "<EOF>", inspect.stack()[0].function))

    def test_018(self):
        """skip"""
        self.assertTrue(TestLexer.test("// tesst //", "<EOF>", inspect.stack()[0].function))

    def test_023(self):
        """skip"""
        self.assertTrue(TestLexer.test("/**///", "<EOF>", inspect.stack()[0].function))

    def test_024(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("2_bA", "2,_bA,<EOF>", inspect.stack()[0].function))

    def test_025(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("_", "_,<EOF>", inspect.stack()[0].function))

    def test_026(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("2b", "2,b,<EOF>", inspect.stack()[0].function))

    def test_031(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.test("-0120", "-,0,120,<EOF>", inspect.stack()[0].function))

    def test_036(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.test("0b000", "0b000,<EOF>", inspect.stack()[0].function))

    def test_037(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.test("0b1e", "0b1,e,<EOF>", inspect.stack()[0].function))

    def test_042(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.test("-0O72", "-,0O72,<EOF>", inspect.stack()[0].function))

    def test_048(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.test("0xae2", "0xae2,<EOF>", inspect.stack()[0].function))

    def test_050(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.test("010.010e-020", "010.010e-020,<EOF>", inspect.stack()[0].function))

    def test_052(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.test("1.2Ee2", "1.2,Ee2,<EOF>", inspect.stack()[0].function))

    def test_058(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.test("00.1e2", "00.1e2,<EOF>", inspect.stack()[0].function))

    def test_061(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.test(""" "votien" """, "\"votien\",<EOF>", inspect.stack()[0].function))

    def test_062(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.test(""" "\\r" """, "\"\\r\",<EOF>", inspect.stack()[0].function))

    def test_067(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.test(""" "\\r \\r \\r" """, "\"\\r \\r \\r\",<EOF>", inspect.stack()[0].function))

    def test_069(self):
        """Keywords"""
        self.assertTrue(TestLexer.test(""" ^ """, "ErrorToken ^", inspect.stack()[0].function))

    def test_083(self):
        """BOOL_LIT"""
        self.assertTrue(TestLexer.test("true", "true,<EOF>", inspect.stack()[0].function))

    def test_084(self):
        """BOOL_LIT"""
        self.assertTrue(TestLexer.test("false", "false,<EOF>", inspect.stack()[0].function))

    def test_085(self):
        """NIL_LIT"""
        self.assertTrue(TestLexer.test("nil", "nil,<EOF>", inspect.stack()[0].function))

    def test_086(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.test("?", "ErrorToken ?", inspect.stack()[0].function))

    def test_087(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.test("@", "ErrorToken @", inspect.stack()[0].function))

    def test_091(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.test(""" 123" """, "123,Unclosed string: \" ", inspect.stack()[0].function))

    def test_094(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.test(""" "123
        " """, "Unclosed string: \"123", inspect.stack()[0].function))

    def test_097(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.test(""" "&\\&" """, "Illegal escape in string: \"&\\&", inspect.stack()[0].function))

    def test_098(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.test(""" "\\z" """, "Illegal escape in string: \"\\z", inspect.stack()[0].function))
