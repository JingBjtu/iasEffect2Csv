# -*- coding: UTF-8 -*-

import VadResult
import OnebestIsaResult
import OnebestIasResult
import QatestResult

class IasTestData:
    def __init__(self, data_dir):
        self.data_fir = data_dir
        self.filenames = {'onebest_ias_mono': data_dir + r"/onebest_IAS_mono/result.txt",
                          'onebest_ias_stereo_n0': data_dir + r"/onebest_IAS_stereo_n0/result.txt",
                          'onebest_ias_stereo_n1': data_dir + r"/onebest_IAS_stereo_n1/result.txt",
                          'onebest_isa_mono': data_dir + r"/onebest_ISA_mono/result.txt",
                          'onebest_isa_stereo_n0': data_dir + r"/onebest_ISA_stereo_n0/result.txt",
                          'onebest_isa_stereo_n1': data_dir + r"/onebest_ISA_stereo_n1/result.txt",
                          'vad_result_mono': data_dir + r'/vad_result_mono.txt',
                          'vad_result_stereo_n0': data_dir + r'/vad_result_stereo_n0.txt',
                          'vad_result_stereo_n1': data_dir + r'/vad_result_stereo_n1.txt',
                          'qatest_boss': data_dir + r'/IAS_xml/.detail/mono/result-m0/boss_summary.txt',
                          'qatest_qa': data_dir + r'/IAS_xml/.detail/mono/result-m0/qa_summary.txt',
                          'qatest_recommend': data_dir + r'/IAS_xml/.detail/mono/result-m0/recommend_summary.txt',
                          'qatest_summary': data_dir + r'/IAS_xml/.detail/mono/result-m0/summary.txt'}

    def parse(self):
        self._parse_onebest_ias()
        self._parse_onebest_isa()
        self._parse_qatest()
        self._parse_vad()
        return self.get_csv_data()

    def get_csv_data(self):
        
        self.csv_data = (('zhong'), ('中', 'dad'))
        return self.csv_data

    def _parse_vad(self):
        self.vad_result_mono = VadResult.VadResult()
        self.vad_result_mono.parse(self.filenames['vad_result_mono'])
        self.vad_result_stereo_n0 = VadResult.VadResult()
        self.vad_result_stereo_n0.parse(self.filenames['vad_result_stereo_n0'])
        self.vad_result_stereo_n1 = VadResult.VadResult()
        self.vad_result_stereo_n1.parse(self.filenames['vad_result_stereo_n1'])

    def _parse_onebest_isa(self):
        self.onebest_isa_mono = OnebestIsaResult.OnebestIsaResult()
        self.onebest_isa_mono.parse(self.filenames['onebest_isa_mono'])
        self.onebest_isa_stereo_n0 = OnebestIsaResult.OnebestIsaResult()
        self.onebest_isa_stereo_n0.parse(self.filenames['onebest_isa_stereo_n0'])
        self.onebest_isa_stereo_n1 = OnebestIsaResult.OnebestIsaResult()
        self.onebest_isa_stereo_n1.parse(self.filenames['onebest_isa_stereo_n1'])

    def _parse_onebest_ias(self):
        self.onebest_ias_mono = OnebestIasResult.OnebestIasResult()
        self.onebest_ias_mono.parse(self.filenames['onebest_ias_mono'])
        self.onebest_ias_stereo_n0 = OnebestIasResult.OnebestIasResult()
        self.onebest_ias_stereo_n0.parse(self.filenames['onebest_ias_stereo_n0'])
        self.onebest_ias_stereo_n1 = OnebestIasResult.OnebestIasResult()
        self.onebest_ias_stereo_n1.parse(self.filenames['onebest_ias_stereo_n1'])

    def _parse_qatest(self):
        self.qatest_boss = QatestResult.QatestResult()
        self.qatest_boss.parse(self.filenames['qatest_boss'])
        self.qatest_qa = QatestResult.QatestResult()
        self.qatest_qa.parse(self.filenames['qatest_qa'])
        self.qatest_recommend = QatestResult.QatestResult()
        self.qatest_recommend.parse(self.filenames['qatest_recommend'])
        self.qatest_summary = QatestResult.QatestResult()
        self.qatest_summary.parse(self.filenames['qatest_summary'])