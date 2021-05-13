# @Time    : 2020/11/17 21:38
# @Author  : GodWei
# @File    : forms.py
from django import forms
from .models import Comment


# Django表单，通过继承Form基类创建了一个表单
class EmailPostForm(forms.Form):
    # 该字段类型显示为<input type='text'>HTML元素
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()


class CommentForm(forms.ModelForm):
    # 1.required=False 将comments设置为可选项等
    # 2.默认的微件可通过widget被覆写，如下使用了Textarea微件，
    #   将其显示为<textarea>HTML元素，而非默认状态下的<input>元素
    comments = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        # 指定一个模型创建Meta类中的表单。
        model = Comment
        # 通知当前框架希望在表单中包含哪些字段；也可采用exclude列表定义希望排除的字段
        fields = ('comments',)
