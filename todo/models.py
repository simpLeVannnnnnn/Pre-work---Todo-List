# coding:utf-8
from django.db import models




class Todo(models.Model):

    todo = models.CharField(max_length=100)  # 待办事项内容

    expire_date = models.DateTimeField(auto_now_add=True)  # 待办事项到期时间

    todo_sign = models.CharField(max_length=2)  # 待办事项完成标记

    todo_priority = models.CharField(max_length=2)  # 待办事项优先级

    def __unicode__(self):
        return u'%s %s %s' % (self.todo, self.todo_sign, self.todo_priority)

class Meta:
    ordering = ('todo_priority', 'expire_date')