# -*- coding: UTF-8 -*-

import sys
import re


class QatestConfidence:

    def __init__(self):
        self.line = ''
        self.confidence = '0'
        self.precision = '0.00'
        self.recall = '0.00'

    def parse(self, line):
        self.line = line
        splited_line = re.split('\s+', line)
        self.confidence = splited_line[0]
        self.precision = splited_line[1]
        self.recall = splited_line[2]

    def print_str(self):
        print 'line :', self.line
        print 'confidence =', self.confidence
        print 'precison =', self.precision
        print 'recall =', self.recall

    @staticmethod
    def main(line):
        qatest = QatestConfidence()
        qatest.parse(line)
        qatest.print_str()

    @staticmethod
    def get_best_confidence(lhs, rhs):
        if float(lhs.precision) >= float(rhs.precision):
            return lhs
        else:
            return rhs

    @staticmethod
    def get_nearest_confidence(lhs, rhs):
        lhs_diff = abs(float(lhs.precision) - float(lhs.recall))
        rhs_diff = abs(float(rhs.precision) - float(rhs.recall))
        if lhs_diff <= rhs_diff:
            return lhs
        else:
            return rhs

if __name__ == '__main__':
    if len(sys.argv) == 2:
        line = sys.argv[1]
    else:
        line = r'0                             1.67                          48.97'
    QatestConfidence.main(line)