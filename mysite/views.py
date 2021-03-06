from django.shortcuts import render, redirect
from mysite import models, forms
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

# Create your views here.
def index(request):
	posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
	moods = models.Mood.objects.all()
	try:
		user_id = request.GET['user_id']
		user_pass = request.GET['user_pass']
		user_post = request.GET['user_post']
		user_mood = request.GET['mood']
	except:
		user_id = None
		message = '如要張貼訊息，則每一欄都要填寫...'
	
	if user_id != None:
		mood = models.Mood.objects.get(status=user_mood)
		post = models.Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
		post.save()
		message='儲存成功! 請記得你的編輯密碼 [{}]!，訊息審查後才會顯示。'.format(user_pass)
		
	return render(request, 'index.html', locals())

def listing(request):
	posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
	moods = models.Mood.objects.all()
	return render(request, 'listing.html', locals())

def posting(request):
	moods = models.Mood.objects.all()
	try:
		user_id = request.POST['user_id']
		user_pass = request.POST['user_pass']
		user_post = request.POST['user_post']
		user_mood = request.POST['mood']
	except:
		user_id = None
		message = '如要張貼訊息，則每一欄都要填寫...'
	
	if user_id != None:
		mood = models.Mood.objects.get(status=user_mood)
		post = models.Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
		post.save()
		message='儲存成功! 請記得你的編輯密碼 [{}]!，訊息審查後才會顯示。'.format(user_pass)
		
	return render(request, 'posting.html', locals())


def contact(request):
	if request.method == 'POST':
		form = forms.ContactForm(request.POST)
		if form.is_valid():
			message = "感謝您的來信"
			user_name = form.cleaned_data['user_name']
			user_city = form.cleaned_data['user_city']
			user_school = form.cleaned_data['user_school']
			user_email = form.cleaned_data['user_email']
			user_message = form.cleaned_data['user_message']
			
			mail_body = u'''
網友姓名:{}
網友信箱:{}
居住城市:{}
是否在學:{}
反應意見如下:{}
'''.format(user_name, user_email, user_city, user_school, user_message)

			email = EmailMessage( '來自留言小天地網站的網友意見', mail_body, user_email, ['alex03100310@gmail.com'])
			email.send()

		else:
			message = "請檢查您輸入的資訊是否正確! "
	else:
		form = forms.ContactForm()
	return render(request, 'contact.html', locals())

def post2db(request):
	if request.method == 'POST':
		post_form = forms.PostForm(request.POST)
		if post_form.is_valid():
			post_form.save()
			return redirect('/')
		else:
			message = "每個欄位都要填喔"
	else:
		post_form = forms.PostForm()
		message = '如要張貼訊息，則每一欄都要填寫'

	return render(request, 'post2db.html', locals())
	
def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['alex03100310@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('/')