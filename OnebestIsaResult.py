# -*- coding: UTF-8 -*-

import sys
import re
import OnebestIsaRole

class OnebestIsaResult:
    r"""onebest_ISA_xx/result.txt文件中的数据"""

    def __init__(self):
        self.filename = ''
        self.a_role = OnebestIsaRole.OnebestIsaRole()
        self.b_role = OnebestIsaRole.OnebestIsaRole()
        self.mix_vad = OnebestIsaRole.OnebestIsaRole()

    def parse(self, filename):
        self.filename = filename
        fp = open(filename, 'r')
        all_lines = fp.readlines()
        fp.close()
        self.a_role.parse(all_lines[1])
        self.b_role.parse(all_lines[2])
        self.mix_vad.parse(all_lines[3])

    def print_str(self):
        print 'a role:'
        self.a_role.print_str()
        print ''
        print 'b role:'
        self.b_role.print_str()
        print ''
        print 'mix vad:'
        self.mix_vad.print_str()

    @staticmethod
    def main(filename):
        onebest = OnebestIsaResult()
        onebest.parse(filename)
        onebest.print_str()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = r'sx500_assist\onebest_ISA_mono\result.txt'
    OnebestIsaResult.main(filename)