# 返回数据参数获取
class Dohuoqu:
    def __init__(self, file_res, gile_expecpt):
        self.file_res = file_res
        self.gile_expecpt = gile_expecpt

    def get_data(self):
        reslist = []
        reslist1 = []
        aaa = self.file_res['allData'][0]['regressionData']
        bbb = self.gile_expecpt['allData'][0]['regressionData']
        for i in range(0, len(aaa)):
            keys = list(aaa[i].keys())
            for j in keys:
                if str(aaa[i][j]) != str(bbb[i][j]):
                    a = {j: bbb[i][j]}
                    reslist1.append(a)

        return reslist1


if __name__ == '__main__':
    res = {'calculateStatus': 'regressed', 'allData': [{'project': 'lanyuan15000', 'regressionData': [
        {'testcaseId': '9', 'testcaseName': '33333', 'UUID': 'a9c79a72fd566a152b6a597b7921d710', 'versionid': '138',
         'versionName': '#', 'testcaseTypeName': '33333', 'laststate': 'runned', 'lasttime': '2021-01-29 12:51:29',
         'impact_value': '0', 'fiximpact_value': '0', 'sectionRatio': '0', 'm_run_fun': []},
        {'testcaseId': '2', 'testcaseName': '2222', 'UUID': '#', 'versionid': '135', 'versionName': '#',
         'testcaseTypeName': '222', 'laststate': 'runned', 'lasttime': '2021-01-29 12:37:28', 'impact_value': '0',
         'fiximpact_value': '0', 'sectionRatio': '0', 'm_run_fun': []},
        {'testcaseId': '6', 'testcaseName': '222222222', 'UUID': 'a9c79a72fd566a152b6a567b7f26d710', 'versionid': '135',
         'versionName': '#', 'testcaseTypeName': '22222222222', 'laststate': 'runned',
         'lasttime': '2021-01-29 12:39:24', 'impact_value': '0', 'fiximpact_value': '0', 'sectionRatio': '0',
         'm_run_fun': []}, {'testcaseId': '7', 'testcaseName': '4444444444', 'UUID': 'a9c79a72fd566a152b6a567b7926d710',
                            'versionid': '135', 'versionName': '#', 'testcaseTypeName': '22222222222',
                            'laststate': 'runned', 'lasttime': '2021-01-29 12:41:26', 'impact_value': '0',
                            'fiximpact_value': '0', 'sectionRatio': '0', 'm_run_fun': []}]}]}
    cse = {'calculateStatus': 'regressed', 'allData': [{'project': 'lanyuan15000', 'regressionData': [
        {'testcaseId': '9', 'testcaseName': '33333', 'UUID': 'a9c79a72fd566a152b6a597b7921d710', 'versionid': '138',
         'versionName': '#', 'testcaseTypeName': '33333', 'laststate': 'runned', 'lasttime': '2021-01-29 12:51:29',
         'impact_value': '0', 'fiximpact_value': '0', 'sectionRatio': '0', 'm_run_fun': []},
        {'testcaseId': '2', 'testcaseName': '2222', 'UUID': '#', 'versionid': '135', 'versionName': '#',
         'testcaseTypeName': '222', 'laststate': 'runned', 'lasttime': '2021-01-29 12:37:28', 'impact_value': '0',
         'fiximpact_value': '0', 'sectionRatio': '0', 'm_run_fun': []},
        {'testcaseId': '6', 'testcaseName': '222222222', 'UUID': 'a9c79a72fd566a152b6a567b7f26d710', 'versionid': '135',
         'versionName': '#', 'testcaseTypeName': '22222222222', 'laststate': 'runned',
         'lasttime': '2021-01-29 12:39:24', 'impact_value': '0', 'fiximpact_value': '0', 'sectionRatio': '0',
         'm_run_fun': []}, {'testcaseId': '7', 'testcaseName': '4444444444', 'UUID': 'a9c79a72fd566a152b6a567b7926d710',
                            'versionid': '135', 'versionName': '#', 'testcaseTypeName': '22222222222',
                            'laststate': 'runned', 'lasttime': '2021-01-29 12:41:26', 'impact_value': '0',
                            'fiximpact_value': '0', 'sectionRatio': '1', 'm_run_fun': []}]}]}

    print(Dohuoqu(res, cse).get_data())

