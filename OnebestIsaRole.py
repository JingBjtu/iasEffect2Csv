# -*- coding: UTF-8 -*-

import sys
import re


class OnebestIsaRole:

    def __init__(self):
        self.line = ''
        self.role = ''
        self.precision = ''
        self.accurate_rate = ''
        self.replace_error = ''
        self.delete_error = ''
        self.insert_error = ''
        self.h = ''
        self.d = ''
        self.s = ''
        self.i = ''
        self.n = ''

    def parse(self, line):
        self.line = line.rstrip()
        splited_line = re.split('\s+', line)
        self.role = re.split('\(', splited_line[0])[0]
        self.precision = splited_line[1]
        self.accurate_rate = splited_line[2]
        self.replace_error = splited_line[3]
        self.delete_error = splited_line[4]
        self.insert_error = splited_line[5]
        self.h = splited_line[6]
        self.d = splited_line[7]
        self.s = splited_line[8]
        self.i = splited_line[9]
        self.n = splited_line[10]
        pass

    def print_str(self):
        print 'line :', self.line
        print 'role =', self.role
        print 'precision =', self.precision
        print 'accurate rate =',self.accurate_rate
        print 'replace error =', self.replace_error
        print 'delete error =', self.delete_error
        print 'insert error =', self.insert_error
        print 'h =', self.h
        print 'd =', self.d
        print 's =', self.s
        print 'i =', self.i
        print 'n =', self.n

    @staticmethod
    def main(line):
        onebest_isa_role = OnebestIsaRole()
        onebest_isa_role.parse(line)
        onebest_isa_role.print_str()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        line = sys.argv[1]
    else:
        line = r'MIX-VAD(%)     100.00         100.00         0.00           0.00           0.00           208046         0              0              0              208046         '
    OnebestIsaRole.main(line)
