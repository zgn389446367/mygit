from django import template
from django.urls import reverse
from django.http.request import QueryDict

register = template.Library()


@register.simple_tag
def reverse_url(request, url_name, *args, **kwargs):
    # 获取当前地址  下次操作完成后跳转回来
    next = request.get_full_path()
    # 生成一个QueryDict对象  可编辑
    qd = QueryDict(mutable=True)
    qd['next'] = next
    # URL反向解析
    base_url = reverse(url_name, args=args, kwargs=kwargs)
    return '{}?{}'.format(base_url,
                          qd.urlencode())
