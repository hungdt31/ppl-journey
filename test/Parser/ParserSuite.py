"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""

import unittest
from TestUtils import TestParser
import inspect

class ParserSuite(unittest.TestCase):
    def test_001(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = 1;","successful", inspect.stack()[0].function))

    def test_002(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = true;","successful", inspect.stack()[0].function))

    def test_003(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = [5][0]string{1, \"string\"};","successful", inspect.stack()[0].function))

    def test_004(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = [1.]ID{1, 3};","Error on line 1 col 16: 1.", inspect.stack()[0].function))

    def test_005(self):
        """Literal"""
        self.assertTrue(TestParser.test("const Votien = Person{name: \"Alice\", age: 30};","successful", inspect.stack()[0].function))

    def test_006(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = 1 || 2 && c + 3 / 2 - -1;","successful", inspect.stack()[0].function))

    def test_007(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = 1[2] + foo()[2] + ID[2].b.b;","successful", inspect.stack()[0].function))

    def test_008(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = ca.foo(132) + b.c[2];","successful", inspect.stack()[0].function))

    def test_009(self):
        """expression"""
        self.assertTrue(TestParser.test("const Votien = a.a.foo();","successful", inspect.stack()[0].function))
    
    def test_010(self):
        """declared variables"""
        self.assertTrue(TestParser.test("""
            var x int = foo() + 3 / 4;
            var y = "Hello" / 4;   
            var z str;
        ""","successful", inspect.stack()[0].function))

    def test_011(self):
        """declared constants"""
        self.assertTrue(TestParser.test("""
            const VoTien = a.b() + 2;
        ""","successful", inspect.stack()[0].function))

    def test_012(self):
        """declared function"""
        self.assertTrue(TestParser.test("""
            func VoTien(x int, y int) int {return;}
            func VoTien1() [2][3] ID {return;};        
            func VoTien2() {return;}                                       
        ""","successful", inspect.stack()[0].function))

    def test_013(self):
        """declared method"""
        self.assertTrue(TestParser.test("""
            func (c Calculator) VoTien(x int) int {return;};  
            func (c Calculator) VoTien() ID {return;}      
            func (c Calculator) VoTien(x int, y [2]VoTien) {return;}                                                      
        ""","successful", inspect.stack()[0].function))

    def test_014(self):
        """declared struct"""
        self.assertTrue(TestParser.test("""
            type VoTien struct {
                VoTien string ;
                VoTien [1][3]VoTien ;                     
            }                                                                     
        ""","successful", inspect.stack()[0].function))

    def test_015(self):
        """declared Interface"""
        self.assertTrue(TestParser.test("""
            type VoTien struct {}                                                                       
        ""","Error on line 2 col 32: }", inspect.stack()[0].function))
    
    def test_016(self):
        """declared Interface"""
        self.assertTrue(TestParser.test("""
            type Calculator interface {
                                        
                Add(x, y int) int;
                Subtract(a, b float, c int) [3]ID;
                Reset()
                                        
                SayHello(name string);
                                        
            }
            type VoTien interface {}                                                                       
        ""","Error on line 11 col 35: }", inspect.stack()[0].function))

    def test_017(self):
        """declared_statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {
                var x int = foo() + 3 / 4;
                var y = "Hello" / 4;   
                var z str;
                                        
                const VoTien = a.b() + 2;
            }                                       
        ""","successful", inspect.stack()[0].function))


    def test_018(self):
        """assign_statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;                       
            }                                       
        ""","successful", inspect.stack()[0].function))

    def test_019(self):
        """for_statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {
                if (x > 10) {return; } 
                if (x > 10) {
                  return; 
                } else if (x == 10) {
                    var z str;
                } else {
                    var z ID;
                }
            }
        ""","successful", inspect.stack()[0].function))
    
    def test_020(self):
        """if_statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {
                for i < 10 {return; }
                for i := 0; i < 10; i += 1 {return; }
                for index, value := range array {return; }
            }
        ""","successful", inspect.stack()[0].function))


    def test_021(self):
        """break and continue, return, Call  statement"""
        self.assertTrue(TestParser.test("""    
            func VoTien() {                           
                for i < 10 {break;}
                break;
                continue;
                return 1;
                return
                foo(2 + x, 4 / y); m.goo();                        
             }
                                        
        ""","successful", inspect.stack()[0].function))
    
    def test_022(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func (c c) Add(x, c int) {return ;}
""","successful", inspect.stack()[0].function))
    def test_023(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                        break;
                                    func Add() {
                                    };""","Error on line 2 col 40: break", inspect.stack()[0].function))
    
    def test_024(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        for var i [2]int = 0; foo().a.b(); i[3] := 1 {
                                            return; 
                                        }
                                    };""","successful", inspect.stack()[0].function))
    def test_025(self):
        self.assertTrue(TestParser.test("""
            func (p Person) Greet() string {
                if (1) {return;}
                else if (1)
                {}
            };
""","Error on line 4 col 16: else", inspect.stack()[0].function))
        
    def test_026(self):
        """Declared"""
        self.assertTrue(TestParser.test("""
            func Add(a) [2]id {return ;}
""","Error on line 2 col 22: )", inspect.stack()[0].function))
        
    def test_027(self):
        self.assertTrue(TestParser.test("""
        func Add(x, y int, b float) {return ;}
""","successful", inspect.stack()[0].function))
        
    def test_028(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1]int{1+1}                    
""","Error on line 1 col 18: +", inspect.stack()[0].function))
        
    def test_029(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1][2]int{{1,2},{3,4}}                    
""","successful", inspect.stack()[0].function))
    
    def test_030(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1]int{{1, 0x1}, ID{}, {{ID{}}}}                    
""","successful", inspect.stack()[0].function))
        
    def test_031(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1]int{{1, 0x1}, ID{}, 1.2, "s", true, false, nil} + nil                    
""","successful", inspect.stack()[0].function))
        
    def test_032(self):
        self.assertTrue(TestParser.test("""
        type Person struct {
            func (p Person) Greet() string {
                return "Hello, " + p.name
            }; c c;
            func (p Person) Greet() string {
                return "Hello, " + p.name
            } c c;                                                    
        }      
""","Error on line 8 col 14: c", inspect.stack()[0].function))
        
    def test_033(self):
        self.assertTrue(TestParser.test("""
            func (p Person) Greet() string {
                for i := 0
                    i < 10
                    i += 1 {
                    return
                }
                for i := 0
                    i < 10
                    i += 1 
                {
                    return
                }
            };  
""","Error on line 10 col 27: ;", inspect.stack()[0].function))
        
    def test_034(self):
        self.assertTrue(TestParser.test("""
            func (p Person) Greet() string {
                for i < 10 {
// loop body
}
            };  
""","Error on line 5 col 0: }", inspect.stack()[0].function))
        
    def test_035(self):
        self.assertTrue(TestParser.test("""
            func (p Person) Greet() string {
                for index, value := range STRUCT{} {
// loop body                                   
};
            };  
""","Error on line 5 col 0: }", inspect.stack()[0].function))
    
    # array literal - attention to element type
    def test_036(self):
        self.assertTrue(TestParser.test("""
            const a = [2]int{1, 2, 3}; 
""","successful", inspect.stack()[0].function))
        
    # testcase is so hard for me to design expression, not include ID DOT NUMBER
    def test_037(self):
        self.assertTrue(TestParser.test("""
        const a = a.2; 
""","Error on line 2 col 20: 2", inspect.stack()[0].function))
        
    def test_038(self):
        self.assertTrue(TestParser.test("""
        var a = ((a + 2) * 3) + 5 * 6; 
""","successful", inspect.stack()[0].function))
        
    def test_038(self):
        self.assertTrue(TestParser.test("""
        const a = !a[2][3].foo(2, 3) - (4 + 6); 
""","successful", inspect.stack()[0].function))
        
    def test_038(self):
        self.assertTrue(TestParser.test("""
        if (a > 2) {
                                        return;
        } else {
            return;
        }
""","successful", inspect.stack()[0].function))
        
    def test_039(self):
        self.assertTrue(TestParser.test("""
        func (c c) Add(x, c int) {return ;}
""","successful", inspect.stack()[0].function))
        
    def test_040(self):
        """array_literal"""
        self.assertTrue(TestParser.test("""const a = [1]int{[1]int{1}}                    
""","Error on line 1 col 17: [", inspect.stack()[0].function))
        
    def test_041(self):
        """Statement"""
        self.assertTrue(TestParser.test("""
                                    func Add() {
                                        (1+2).foo(2 + 3, a {a:2})
                                    };""","Error on line 3 col 40: (", inspect.stack()[0].function))
       