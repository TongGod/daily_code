from mpl_toolkits.basemap import Basemap

import matplotlib.pyplot as plt

from matplotlib.patches import Polygon

from matplotlib.collections import PatchCollection

from matplotlib.patches import PathPatch

import numpy as np

info_dic = {}

provinces = ['湖北', '广东', '浙江', '河南', '湖南', '安徽', '江西', '江苏', '重庆', '山东', '四川', '北京', '黑龙江', '上海', '福建', '河北', '陕西',
             '广西', '云南', '海南', '山西', '贵州', '辽宁', '天津', '甘肃', '吉林', '内蒙古', '新疆', '宁夏', '香港', '青海', '台湾', '澳门', '西藏']

nums = [29631, 1151, 1092, 1073, 879, 830, 771, 492, 468, 466, 405, 337, 331, 299, 261, 218, 213, 210, 141, 136, 119,
        109, 107, 94, 83, 80, 58, 49, 49, 36, 18, 18, 10, 1]

colors = ['darkred', 'firebrick', 'indianred', 'lightcoral', 'lightsalmon']

for i in range(len(provinces)):
    info_dic[provinces[i]] = {'num': nums[i]}

for name in info_dic.keys():

    if info_dic[name]['num'] >= 10000:

        info_dic[name]['color'] = 'darkred'

    elif 1000 < 9999:

        info_dic[name]['color'] = 'firebrick'

    elif 100 < 999:

        info_dic[name]['color'] = 'indianred'

    elif 10 < 99:

        info_dic[name]['color'] = 'lightcoral'

    else:

        info_dic[name]['color'] = 'lightsalmon'