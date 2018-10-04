from django.db import models

# Create your models here.


class kettle_job_config(models.Model):
    job_name = models.CharField(max_length=128)
    step_type = models.CharField(max_length=8)
    exec_type = models.IntegerField()
    exec_time_interval = models.IntegerField()
    exec_time_begin = models.DateTimeField()
    exec_time_end = models.DateTimeField()
    vaild_flag = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    remark = models.CharField(max_length=255)

