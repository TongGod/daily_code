# @Time    : 2021/3/13 9:27
# @Author  : GodWei
# @File    : 构建cookie.py

from random import shuffle


def shuffle_str(s):
    # 将字符串转换成列表
    str_list = list(s)
    # 调用random模块的shuffle函数打乱列表
    shuffle(str_list)
    # 将列表转字符串
    return ''.join(str_list)


def get_cookie():
    JSESSIONID = "DCADCB2FD65D5D7A1B7DC88CDFF501D.7"
    neCYtZEjo8GmS = "5CY1xuuLx.8o1J3fip.ToUbt.WE8Sa_vre9gCARbGnizPM7n.1NlLRlL0plLHzIZm9ut4DRK4KX4TiGTOOpghYa"
    cw_tc = "b65cfd3216155985305838375e062709e8a4a8e9d2863e0445ac6c05780c5a"
    neCYtZEjo8GmT = "53lasADrWlZVqqqmgt170zGNgiE.wtaBqmREopURCydCFNEmyd2DirkS.zRIwnM0UIHFP4_vxjRsJ4Sa804a8WcCO0_2bQmDSMUN4JCWdcEJtia4yUwj16.3c_qtZdcPXf3auOuuEzZCoNDQ2mI8ONVTWA5xn3uepYMMLNv.yy2YyUqFdtdFYoMCnWoQ3uwHZlVZvxqhRXTH_jPYXqmDwQdMtSoIogYWrvki_PmqbccobDlliE5NgOi8T0piMSqYl3"
    cookie = "JSESSIONID=" + JSESSIONID + ";neCYtZEjo8GmS="+shuffle_str(neCYtZEjo8GmS)\
             +";cw_tc=" + shuffle_str(cw_tc) +";neCYtZEjo8GmT=" + shuffle_str(neCYtZEjo8GmT)

    return cookie

