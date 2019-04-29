from django.db import models


# Create your models here.


class UserProfile(models.Model):
    """
    用户表
    """
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(verbose_name='密码', max_length=128)
    name = models.CharField('名字', max_length=32)
    mobile = models.CharField('手机', max_length=32, default=None, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.name)


class Customer(models.Model):
    """
    客户表
    """
    qq = models.CharField('QQ', max_length=64, unique=True, help_text='QQ号必须唯一')
    name = models.CharField('姓名', max_length=32, blank=True, null=True, help_text='学员报名后，请改为真实姓名')
    sex_type = (('male', '男'), ('female', '女'))
    sex = models.CharField("性别", choices=sex_type, max_length=16, default='male', blank=True, null=True)
    birthday = models.DateField('出生日期', default=None, help_text="格式yyyy-mm-dd", blank=True, null=True)
    phone = models.BigIntegerField('手机号', blank=True, null=True)
    consultant = models.ForeignKey('UserProfile', verbose_name="管理员", related_name='customers', blank=True, null=True, )

    def __str__(self):
        return "{} - {}".format(self.qq, self.name)
