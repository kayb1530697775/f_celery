# -*- coding:utf-8 -*-
# @Time   : 12/7/19 6:57 PM
# @Author : Kayb

import os
import time
from f_module.f_celery.tasks import add

if __name__ == '__main__':
    print(add)
    print(dir(add))
    a = add.delay(12, 33)
    print('wait before', a.state)
    a.wait()
    print('wait after', a.state)
    print(a.get())
    print(a.result)
    while not a.ready():
        print(a.ready())
        time.sleep(1)
    print(a.ready())





