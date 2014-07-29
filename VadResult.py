# -*- coding: UTF-8 -*-
import re

class VadResult:
    'vad_result_xx文件中的数据'
    def __init__(self):
        self.precision = 0.00
        self.recall = 0.00
        self.falram = 0.00
        self.error = 0.00
        self.miss = 0.00

    def parse(self, file):
        fp = open(file, 'r')
        allLines = fp.readlines()
        fp.close()

        lineNumAfterFinalResultLine = -1                   # 根据这个变量的数值，确定正在解析的哪行数据
        for eachLine in allLines:
            if eachLine.startswith('Final Result'):     # r'Final Result'
                lineNumAfterFinalResultLine = 0            # r'--------------------------------------------------------'
            elif lineNumAfterFinalResultLine >= 0:
                lineNumAfterFinalResultLine += 1
                if lineNumAfterFinalResultLine == 2:
                    self.parseLine1(eachLine)
                elif lineNumAfterFinalResultLine == 3:
                    self.parseLine2(eachLine)

        return self

    # e.g. line == r'Vad(vad效果)          : Presicion=0.995309 Recall=0.984212'
    def parseLine1(self, line):
        splitedLine = re.split('\s+', line)
        splitedPrecision = re.split('=', splitedLine[2])
        splitedRecall = re.split('=', splitedLine[3])
        self.precision = splitedPrecision[1]
        self.recall = splitedRecall[1]

    # e.g. line == r'                        Falram=181.805394(0.004691), Error=0.000000(0.000000), Miss=618.815538(0.015788)'
    def parseLine2(self, line):
        splitedLine = re.split('\s+', line)
        splitedFalram = re.split('[()]', splitedLine[1])
        splitedError = re.split('[()]', splitedLine[2])
        splitedMiss = re.split('[()]', splitedLine[3])
        self.falram = splitedFalram[1]
        self.error = splitedError[1]
        self.miss = splitedMiss[1]

    @staticmethod
    def main(file):
        vadResult = VadResult()
        vadResult.parse(file)

VadResult.main(r'sx500_assist\vad_result_mono.txt')