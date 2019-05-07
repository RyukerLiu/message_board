#-*- encoding: utf-8 -*-
from django import forms
from mysite import models
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
	CITY = [
		['TP','Taipei'],
		['TY', 'Taoyuang'],
		['TC', 'Taichung'],
		['TN', 'Tainan'],
		['KS', 'Kaohsiung'],
		['NA', 'Others'],
	]
	user_name = forms.CharField(label='您的姓名', max_length=50, initial='李大仁')
	user_city = forms.ChoiceField(label='居住城市', choices=CITY)
	user_school = forms.BooleanField(label='是否在學', required=False)
	user_email = forms.EmailField(label='電子郵件')
	user_message = forms.CharField(label='您的意見', widget=forms.Textarea)
	
class PostForm(forms.ModelForm):
	captcha = CaptchaField(label='機器人測試')
	class Meta:
		model = models.Post
		fields = ['mood', 'nickname', 'message']
		labels = {'mood':'現在心情',
		'nickname':'你的暱稱',
		'message':'心情留言',
		}

