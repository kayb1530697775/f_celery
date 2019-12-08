# -*- coding:utf-8 -*-
# @Time   : 12/7/19 3:17 AM
# @Author : Kayb

from celery import Celery
from celery.signals import before_task_publish, task_postrun


@before_task_publish.connect
def after_task_publish(sender=None, headers=None, body=None, **kwargs):
    print('=='*8, sender, headers, body, kwargs)


@task_postrun.connect
def task_exec_after(task_id=None, task=None, retval=None, state=None, *args, **kwargs):
    print('after-->>--', task_id, task, retval, state)




c_app = Celery('f_celery', include=['f_module.f_celery.tasks', 'f_module.f_celery.f_celery_signals'])
c_app.config_from_object('f_module.f_celery.celery_config')


if __name__ == '__main__':
    pass




