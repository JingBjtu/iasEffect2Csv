# -*- coding: UTF-8 -*-

import sys
import re


class OnebestIasResult:
    r"""onebest_IAS_xx/result.txt文件中的数据"""

    def __init__(self):
        self.file = ''
        self.corr = ''
        self.acc = ''
        self.h = ''
        self.d = ''
        self.s = ''
        self.i = ''
        self.n = ''
        pass

    def parse(self, file_name):
        self.file = file_name
        fp = open(file_name, 'r')
        all_lines = fp.readlines()
        fp.close()

        line_num_after_overall_result = -1
        for every_line in all_lines:
            if every_line.startswith('------------------------ Overall Results --------------------------'):
                line_num_after_overall_result = 0
            elif line_num_after_overall_result >= 0:
                line_num_after_overall_result += 1
                if line_num_after_overall_result == 2:
                    self.line = every_line
                    self._parse_line(every_line)

        self._cal_error_rate()

    def _parse_line(self, line):
        r"""e.g. line like
        WORD: %Corr=87.70, Acc=87.70 [H=208029, D=29177, S=0, I=0, N=237206]"""

        # property_dictionary = {'Corr': self.corr,
        #                        'Acc': self.acc,
        #                        'H': self.h,
        #                        'D': self.d,
        #                        'S': self.s,
        #                        'I': self.i,
        #                        'N': self.n}

        splited_line = re.split('\s+', line)
        property_separator = '[=,\]]'
        splited_corr = re.split(property_separator, splited_line[1])
        splited_acc = re.split(property_separator, splited_line[2])
        splited_h = re.split(property_separator, splited_line[3])
        splited_d = re.split(property_separator, splited_line[4])
        splited_s = re.split(property_separator, splited_line[5])
        splited_i = re.split(property_separator, splited_line[6])
        splited_n = re.split(property_separator, splited_line[7])

        self.corr = splited_corr[1]
        self.acc = splited_acc[1]
        self.h = splited_h[1]
        self.d = splited_d[1]
        self.s = splited_s[1]
        self.i = splited_i[1]
        self.n = splited_n[1]

    def _cal_error_rate(self):
        self.replace_error = float(self.s) / float(self.n) * 100
        self.delete_error = float(self.d) / float(self.n) * 100
        self.insert_error = float(self.i) / (float(self.n) + float(self.i)) * 100

    def print_str(self):
        print 'file :', self.file
        print 'line :', self.line.rstrip()
        print 'corr =', self.corr
        print 'acc =', self.acc
        print 'replace error =', self.replace_error
        print 'delete error =', self.delete_error
        print 'insert error =', self.insert_error
        print 'h =', self.h
        print 'd =', self.d
        print 's =', self.s
        print 'i =', self.i
        print 'n =', self.n

    @staticmethod
    def main(filename):
        onebest = OnebestIasResult()
        onebest.parse(filename)
        onebest.print_str()
    pass

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = r'sx500_assist\onebest_IAS_mono\result.txt'
    OnebestIasResult.main(filename)