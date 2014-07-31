# -*- coding: UTF-8 -*-

import sys
import QatestConfidence


class QatestResult:

    def __init__(self):
        self.filename = ''
        self.best_precision = QatestConfidence.QatestConfidence()
        self.nearest_precision_and_recall = QatestConfidence.QatestConfidence()

    def parse(self, filename):
        fp = open(filename, 'r')
        all_lines = fp.readlines()
        fp.close()

        all_lines = all_lines[1:]
        self.best_precision.parse(all_lines[0])
        self.nearest_precision_and_recall.parse(all_lines[0])
        for every_line in all_lines:
            tmp_confidence = QatestConfidence.QatestConfidence()
            tmp_confidence.parse(every_line)
            self.best_precision = QatestConfidence.QatestConfidence.get_best_confidence(self.best_precision, tmp_confidence)
            self.nearest_precision_and_recall = QatestConfidence.QatestConfidence.get_nearest_confidence(self.nearest_precision_and_recall, tmp_confidence)

    def print_str(self):
        print 'file :', self.filename
        print 'best precision :'
        self.best_precision.print_str()
        print ''
        print 'nearest_precision_and_recall :'
        self.nearest_precision_and_recall.print_str()
        print ''

    @staticmethod
    def main(filename):
        qatest_result = QatestResult()
        qatest_result.parse(filename)
        qatest_result.print_str()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = r'sx500_assist\IAS_xml\.detail\mono\result-m0\summary.txt'
    QatestResult.main(filename)
