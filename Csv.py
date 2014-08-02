# -*- coding: UTF-8 -*-

import os
import types

class Csv:
    @staticmethod
    def write_file(data, filename):
        csv_str = ''
        if type(data) is types.TupleType:
            for row in data:
                if type(row) is types.TupleType:
                    for column in row:
                        csv_str += column + ','
                else:
                    csv_str += row
                csv_str += '\n'
        else:
            csv_str += data

        dir = os.path.dirname(filename)
        if not os.path.exists(dir):
            os.makedirs(dir)
        fp = open(filename, 'w')
        fp.write(csv_str)

    @staticmethod
    def main():
        row1 = ('a', 'b', 'c')
        row2 = ('1', '2', '3')
        row3 = ('中', '文')
        data = (row1, row2, row3)
        csv = Csv()
        csv.write_file(data, 'test/test.csv')

if __name__ == '__main__':
    Csv.main()

