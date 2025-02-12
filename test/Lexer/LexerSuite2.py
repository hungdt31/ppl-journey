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
    
    # def test_001(self):
    #     """Keywords"""
    #     self.assertTrue(TestLexer.test("if","if,<EOF>", inspect.stack()[0].function))

    # def test_002(self):
    #     """Operators"""
    #     self.assertTrue(TestLexer.test("+","+,<EOF>", inspect.stack()[0].function))
        
    # def test_003(self):
    #     """Separators"""
    #     self.assertTrue(TestLexer.test("[]","[,],<EOF>", inspect.stack()[0].function))
        
    # def test_004(self):
    #     """Identifiers"""
    #     self.assertTrue(TestLexer.test("_VOTien","_VOTien,<EOF>", inspect.stack()[0].function))
        
    # def test_005(self):
    #     """Literals INT"""
    #     self.assertTrue(TestLexer.test("12","12,<EOF>", inspect.stack()[0].function))
        
    # def test_006(self):
    #     """Literals INT 16*1 + 1 = 17"""
    #     self.assertTrue(TestLexer.test("0x11","17,<EOF>", inspect.stack()[0].function))
    
    # def test_007(self):
    #     """Literals FLOAT"""
    #     self.assertTrue(TestLexer.test("12.e-8","12.e-8,<EOF>", inspect.stack()[0].function))
    
    # def test_015(self):
    #     """Literals FLOAT"""
    #     self.assertTrue(TestLexer.test("0452","0,452,<EOF>", inspect.stack()[0].function))

    # def test_008(self):
    #     """Literals String"""
    #     self.assertTrue(TestLexer.test(""" "VOTIEN \\r" ""","VOTIEN \\r,<EOF>", inspect.stack()[0].function))

    # def test_014(self):
    #     """ILLEGAL_ESCAPE"""
    #     self.assertTrue(TestLexer.test("""\"HELLO\" \n WORLD""","\"HELLO\" \n WORLD", inspect.stack()[0].function))
        
    # def test_009(self):
    #     """COMEMENTS"""
    #     self.assertTrue(TestLexer.test("// VOTIEN","<EOF>", inspect.stack()[0].function))

    # def test_010(self):
    #     """COMEMENTS"""
    #     self.assertTrue(TestLexer.test("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", inspect.stack()[0].function))

    # def test_011(self):
    #     """ERROR_CHAR"""
    #     self.assertTrue(TestLexer.test("^","ErrorToken ^", inspect.stack()[0].function))

    # def test_012(self):
    #     """UNCLOSE_STRING"""
    #     self.assertTrue(TestLexer.test(""" "VOTIEN\n" ""","Unclosed string: VOTIEN", inspect.stack()[0].function))
    
    # def test_013(self):
    #     """ILLEGAL_ESCAPE"""
    #     self.assertTrue(TestLexer.test(""" "VOTIEN\\f" ""","Illegal escape in string: VOTIEN\\f", inspect.stack()[0].function))
    def test_001(self):
        self.assertTrue(TestLexer.test("var x int;", "var,x,int,;,<EOF>", inspect.stack()[0].function))


    def test_002(self):
        self.assertTrue(TestLexer.test("func main() {}", "func,main,(,),{,},<EOF>", inspect.stack()[0].function))


    def test_003(self):
        self.assertTrue(TestLexer.test("if x == 10 {}", "if,x,==,10,{,},<EOF>", inspect.stack()[0].function))


    def test_004(self):
        self.assertTrue(TestLexer.test("else {}", "else,{,},<EOF>", inspect.stack()[0].function))


    def test_005(self):
        self.assertTrue(TestLexer.test("for i = 0; i < 10; i++ {}", "for,i,=,0,;,i,<,10,;,i,+,+,{,},<EOF>", inspect.stack()[0].function))


    def test_006(self):
        self.assertTrue(TestLexer.test("return 0;", "return,0,;,<EOF>", inspect.stack()[0].function))
       
    # Test operator
    def test_007(self):
        self.assertTrue(TestLexer.test("true && false", "true,&&,false,<EOF>", inspect.stack()[0].function))


    def test_008(self):
        self.assertTrue(TestLexer.test("x += 1;", "x,+=,1,;,<EOF>", inspect.stack()[0].function))


    def test_009(self):
        self.assertTrue(TestLexer.test("y -= 2;", "y,-=,2,;,<EOF>", inspect.stack()[0].function))


    def test_010(self):
        self.assertTrue(TestLexer.test("z *= 3;", "z,*=,3,;,<EOF>", inspect.stack()[0].function))


    def test_011(self):
        self.assertTrue(TestLexer.test("w /= 4;", "w,/=,4,;,<EOF>", inspect.stack()[0].function))


    def test_012(self):
        self.assertTrue(TestLexer.test("a %= 5;", "a,%=,5,;,<EOF>", inspect.stack()[0].function))


    def test_013(self):
        self.assertTrue(TestLexer.test("x && y || z", "x,&&,y,||,z,<EOF>", inspect.stack()[0].function))


    def test_014(self):
        self.assertTrue(TestLexer.test("!x", "!,x,<EOF>", inspect.stack()[0].function))


    def test_015(self):
        self.assertTrue(TestLexer.test("x == y", "x,==,y,<EOF>", inspect.stack()[0].function))


    def test_016(self):
        self.assertTrue(TestLexer.test("x != y", "x,!=,y,<EOF>", inspect.stack()[0].function))


    def test_017(self):
        self.assertTrue(TestLexer.test("x < y", "x,<,y,<EOF>", inspect.stack()[0].function))


    def test_018(self):
        self.assertTrue(TestLexer.test("x <= y", "x,<=,y,<EOF>", inspect.stack()[0].function))


    def test_019(self):
        self.assertTrue(TestLexer.test("x > y", "x,>,y,<EOF>", inspect.stack()[0].function))


    def test_020(self):
        self.assertTrue(TestLexer.test("x >= y", "x,>=,y,<EOF>", inspect.stack()[0].function))


    def test_021(self):
        self.assertTrue(TestLexer.test("x = y", "x,=,y,<EOF>", inspect.stack()[0].function))


    def test_022(self):
        self.assertTrue(TestLexer.test("x + y", "x,+,y,<EOF>", inspect.stack()[0].function))


    def test_023(self):
        self.assertTrue(TestLexer.test("x - y", "x,-,y,<EOF>", inspect.stack()[0].function))


    def test_024(self):
        self.assertTrue(TestLexer.test("x * y", "x,*,y,<EOF>", inspect.stack()[0].function))


    def test_025(self):
        self.assertTrue(TestLexer.test("x / y", "x,/,y,<EOF>", inspect.stack()[0].function))


    def test_026(self):
        self.assertTrue(TestLexer.test("x % y", "x,%,y,<EOF>", inspect.stack()[0].function))


    def test_027(self):
        self.assertTrue(TestLexer.test("x.y", "x,.,y,<EOF>", inspect.stack()[0].function))
       
    # Test array
    def test_028(self):
        self.assertTrue(TestLexer.test("x[0]", "x,[,0,],<EOF>", inspect.stack()[0].function))


    def test_029(self):
        self.assertTrue(TestLexer.test("x[0][1]", "x,[,0,],[,1,],<EOF>", inspect.stack()[0].function))


    def test_030(self):
        self.assertTrue(TestLexer.test("x[0].y", "x,[,0,],.,y,<EOF>", inspect.stack()[0].function))


    def test_031(self):
        self.assertTrue(TestLexer.test("x[0].y[1]", "x,[,0,],.,y,[,1,],<EOF>", inspect.stack()[0].function))
       


    def test_032(self):
        self.assertTrue(TestLexer.test("x[0].y[1].z", "x,[,0,],.,y,[,1,],.,z,<EOF>", inspect.stack()[0].function))


    def test_033(self):
        self.assertTrue(TestLexer.test("x[0].y[1].z[2]", "x,[,0,],.,y,[,1,],.,z,[,2,],<EOF>", inspect.stack()[0].function))


    def test_034(self):
        self.assertTrue(TestLexer.test("x[0].y[1].z[2].w", "x,[,0,],.,y,[,1,],.,z,[,2,],.,w,<EOF>", inspect.stack()[0].function))
       
    def test_035(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("if","if,<EOF>", inspect.stack()[0].function))


    def test_036(self):
        """Operators"""
        self.assertTrue(TestLexer.test("+","+,<EOF>", inspect.stack()[0].function))
       
    def test_037(self):
        """Separators"""
        self.assertTrue(TestLexer.test("[]","[,],<EOF>", inspect.stack()[0].function))
       
    def test_038(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("_VOTien","_VOTien,<EOF>", inspect.stack()[0].function))
       
    def test_039(self):
        """Literals INT"""
        self.assertTrue(TestLexer.test("12","12,<EOF>", inspect.stack()[0].function))
       
    def test_040(self):
        """Literals INT 16*1 + 1 = 17"""
        self.assertTrue(TestLexer.test("0x11","17,<EOF>", inspect.stack()[0].function))
   
    def test_041(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("12.e-8","12.e-8,<EOF>", inspect.stack()[0].function))
   
    def test_042(self):
        """Literals String"""
        self.assertTrue(TestLexer.test(""" "VOTIEN \\r" ""","VOTIEN \\r,<EOF>", inspect.stack()[0].function))
       
    def test_043(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.test("// VOTIEN","<EOF>", inspect.stack()[0].function))


    def test_044(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.test("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", inspect.stack()[0].function))


    def test_045(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.test("^","ErrorToken ^", inspect.stack()[0].function))


    def test_046(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.test(""" "VOTIEN\n" ""","Unclosed string: VOTIEN", inspect.stack()[0].function))
   
    def test_047(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.test(""" "VOTIEN\\f" ""","Illegal escape in string: VOTIEN\\f", inspect.stack()[0].function))


   
    def test_048(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.test("""
            const a = 2;
        ""","\n,const,a,=,2,;,\n,<EOF>", inspect.stack()[0].function))

    def test_049(self):
        """skip"""
        self.assertTrue(TestLexer.test("\t\f\r ", "<EOF>", inspect.stack()[0].function))
    
    def test_050(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.test("0452.", "0,452.,<EOF>", inspect.stack()[0].function))
    
    def test_051(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.test("1_2", "1,_2,<EOF>", inspect.stack()[0].function))
    
    def test_052(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.test("0b000", "0,<EOF>", inspect.stack()[0].function))

    def test_053(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.test("010.010e-020", "0,10.010e-0,20,<EOF>", inspect.stack()[0].function))

    def test_054(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.test(""" "\\"" """, "\\\",<EOF>", inspect.stack()[0].function))
    
    def test_055(self):
        self.assertTrue(TestLexer.test("const Votien = [5][0]string{1, \"string\"}", "const,Votien,=,[,5,],[,0,],string,{,1,,,string,},<EOF>", inspect.stack()[0].function))
    # self.assertTrue(TestParser.test("""
    #         type VoTien struct {
    #             VoTien string ;
    #             VoTien [1][3]VoTien ;                     
    #         }
    #         type VoTien struct {}                                                                       
    #     ""","successful", inspect.stack()[0].function))
    # def test_056(self):
    #     self.assertTrue(TestLexer.test("""
    #         type VoTien struct {
    #             VoTien string ;
    #             VoTien [1][3]VoTien ;                     
    #         }
    #         type VoTien struct {}                                                                       
    #     """, "", inspect.stack()[0].function))
    
    # def test_057(self):
    #     self.assertTrue(TestLexer.test("/*abc/*abc*/", "", inspect.stack()[0].function))
    # def test_056(self):
    #     """Statement"""
    #     self.assertTrue(TestLexer.test("""
    #                                 func Add() {
    #                                     a.c[2].e[3].k += 2;       
    #                                 }""","successful", inspect.stack()[0].function))
    
    # def test_057(self):
    #     """Statement"""
    #     self.assertTrue(TestLexer.test("""
    #                                    "this is a" newline"
    #     ""","successful", inspect.stack()[0].function))
    def test_109(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.test("""
            if
            }
            ]
            )
""", "if,},;,],;,),;,<EOF>", inspect.stack()[0].function))

    def test_110(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.test("""
            nil
""", "nil,;,<EOF>", inspect.stack()[0].function))
    #!!! 87 test yêu cầu code chấm sau



