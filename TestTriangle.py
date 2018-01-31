# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author: Celeste Sakhile
"""

import unittest
from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # Zero Inputs tested
    def testZeroInput1(self):
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput','0,0,0 can not be sides of a triangle')

    def testZeroInput2(self):
        self.assertEqual(classifyTriangle(0,3,4),'InvalidInput','0,3,4 can not be sides of a triangle')

    def testZeroInput3(self):
        self.assertEqual(classifyTriangle(5,0,6),'InvalidInput','5,0,6 can not be sides of a triangle')

    def testZeroInput4(self):
        self.assertEqual(classifyTriangle(7,2,0),'InvalidInput','7,2,0 can not be sides of a triangle')

    # Inputs larger than 200 tested
    def testLargeInput1(self):
        self.assertEqual(classifyTriangle(300,400,500),'InvalidInput','300,400,500 can not be sides of a triangle')

    def testLargeInput2(self):
        self.assertEqual(classifyTriangle(201,167,189),'InvalidInput','201,167,189 can not be sides of a triangle')

    def testLargeInput3(self):
        self.assertEqual(classifyTriangle(155,178,201),'InvalidInput','155,178,201 can not be sides of a triangle')

    def testLargeInput4(self):
        self.assertEqual(classifyTriangle(179,201,160),'InvalidInput','179,201,160 can not be sides of a triangle')

    # Negative Inputs tested
    def testNegativeInput1(self):
        self.assertEqual(classifyTriangle(-7, 8, 9), 'InvalidInput', '-7,8,9 can not be sides of a triangle')

    def testNegativeInput2(self):
        self.assertEqual(classifyTriangle(5, -6, 4), 'InvalidInput', '5,-6,4 can not be sides of a triangle')

    def testNegativeInput3(self):
        self.assertEqual(classifyTriangle(3, 4, -5), 'InvalidInput', '3,4,-5 can not be sides of a triangle')

    def testNegativeInput4(self):
        self.assertEqual(classifyTriangle(-12, -13, -10), 'InvalidInput', '-12,-13,-10 can not be sides of a triangle')

    # Wrong Input type tested
    def testWrongType1(self):
        self.assertEqual(classifyTriangle(7, 11, 6.9), 'InvalidInput', '7,11,6.9 contain incorrect input types')

    def testWrongType2(self):
        self.assertEqual(classifyTriangle(31, 20.5, 36), 'InvalidInput', '31,20.5,36 contain incorrect input types')

    def testWrongType3(self):
        self.assertEqual(classifyTriangle(5, 3, 3.4), 'InvalidInput', '5,3,3.4 are contain input types')

    def testWrongType4(self):
        self.assertEqual(classifyTriangle(4.1, 3.3, 2.9), 'InvalidInput', '4.1,3.3,2.9 contain incorrect input types')

    # Invalid triangle inputs tested. (Inputs that dont follow the condition that the sum of two sides of a triange should be greater than the third)
    def testNotTriangle1(self):
        self.assertEqual(classifyTriangle(1, 1, 3), 'NotATriangle', '1,1,3 can not be sides of a triangle')

    def testNotTriangle2(self):
        self.assertEqual(classifyTriangle(2, 3, 1), 'NotATriangle', '2,3,1 can not be sides of a triangle')

    def testNotTriangle3(self):
        self.assertEqual(classifyTriangle(4, 2, 8), 'NotATriangle', '4,2,8 can not be sides of a triangle')

    # Equilateral Inputs tested
    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    # Isoceles Inputs tested
    def testIsoscelesTriangle1(self):
        self.assertEqual(classifyTriangle(10, 10, 15), 'Isoceles','10, 10, 15 is an Isoceles triangle')

    def testIsoscelesTriangle2(self):
        self.assertEqual(classifyTriangle(3, 4, 3),'Isoceles','3,4,3 is an Isoceles triangle')

    def testIsoscelesTriangle3(self):
        self.assertEqual(classifyTriangle(8, 6, 6),'Isoceles','8,6,6 is an Isoceles triangle')

    # Right Triangle Inputs tested
    def testRightTriangle1(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangle2(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testRightTriangle3(self):
        self.assertEqual(classifyTriangle(15, 17, 8), 'Right', '15,17,8 is a Right triangle')

    # Scalene Triangle Inputs tested
    def testScaleneTriangle1(self):
        self.assertEqual(classifyTriangle(3, 4, 2), 'Scalene', '3,4,2 is a Scalene triangle')

    def testScaleneTriangle2(self):
        self.assertEqual(classifyTriangle(153, 199, 200), 'Scalene', '153,199,200 is a Scalene triangle')

    def testScaleneTriangle3(self):
        self.assertEqual(classifyTriangle(200, 153, 199), 'Scalene', '200,153,199 is a Scalene triangle')

    def testScaleneTriangle4(self):
        self.assertEqual(classifyTriangle(199, 200, 153), 'Scalene', '199,200,153 is a Scalene triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

