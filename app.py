import IasTestData
import Csv

ias_test_data = IasTestData.IasTestData('sx500_assist')
data_table = ias_test_data.parse()
Csv.Csv.write_file(data_table, r'test/example.csv')