from django.shortcuts import *
from tendermanagement.models import *
from django.views.generic import TemplateView
import re
from django.views.decorators.cache import cache_control

def home(request):
	session={}
	if not request.session.get('user_id'):
		request.session['user_id']=0
		session['set']=request.session['user_id']
		return render_to_response("1home.html",{'session':session})
	elif request.session['user_id'] == 3:
		return render_to_response("1userpage.html")
	else:
		x = request.session['id']
		a = req_user.objects.values().filter(id=x)
		diction={}
		diction=a[0].copy()
		return render_to_response("1userpage.html", {'diction':diction})

def about(request):
	session={}
	if not request.session.get('user_id'):
		request.session['user_id']=0
	session['set']=request.session['user_id']
	return render_to_response("1about.html",{'session':session})

def login(request):
	diction={}
	diction['result']="null"
	return render_to_response("1login.html",diction)

def signup(request):
	return render_to_response("1signup.html")

def avail_tender(request):
	return render_to_response("1avail_tender.htm")

def contact(request):
	session={}
	if not request.session.get('user_id'):
		request.session['user_id']=0
	session['set']=request.session['user_id']
	return render_to_response("1contact.html",{'session':session})

def request_signup(request):
	diction={}
	diction['value']=0
	return render_to_response("1request_signup.html",diction)

def tender_request(request):
	diction={}
	diction['result']="null"
	return render_to_response("1tender_request.html")

def req_check(request):
	user_id = 2
	diction={}
	diction['value']=0
	flag = 1
	flag1 = 1
	flag2 = 1
	recaptcha_response = request.POST.get('g-recaptcha-response')
	len1=len(recaptcha_response)
	if len1==0:
		return render_to_response("1request_signup.html")
	if 'cb' in request.POST:
		cb1 = request.POST['cb']
	else:
		cb1 = 0
	print(cb1)
	email = request.POST['email']
	pwrd = request.POST['pwrd']
	pwrd1 = request.POST['pwrd1']
	company_name = request.POST['com_name']
	u_name = request.POST['name']
	phno = request.POST['phno']
	len1 = len(pwrd)
	if len1 < 6:
		flag = -1
	if phno[0] =='9' or phno[0] =='8' or phno[0] =='7':
		len1 = len(phno)
		if len1 != 10:
			flag1 = -1
	else:
		flag1 = -1
	diction['value']=1
	if pwrd != pwrd1:
		flag2 = -1
	#######################################################

	#for checking whether the email has been used or no
	a = req_user.objects.all().values()
	i = 0
	flag3=1
	len1 = len(a)
	while i<len1:
		if a[i]['email']==email:
			flag3 = -1
			break
		i+=1

	i=0
	phno = int(phno)
	flag4=1
	while i<len1:
		if int(a[i]['phno'])==phno:
			flag4 = -1
			break
		i+=1
	if flag3 == -1:
		diction['result']="Email ID has already been taken."
	elif flag == -1:
		diction['result']="Password less that 6 characters."
	elif flag2 == -1:
		diction['result']="Both passwords don't match."
	elif flag1 == -1:
		diction['result']="Invalid phone nummber. Please re-check."
	elif flag4 == -1:
		diction['result']="Phone nummber has already been used. Please re-check."
	elif cb1 == 0:
		diction['result']="Please check the box"
	else:
		s = req_user()
		s.email	= email
		s.passwrd = pwrd
		s.c_name = company_name
		s.uname = u_name
		phno = int(phno)
		s.phno = phno
		s.user_id = int(user_id)
		s.save();
		diction['result']="Signup sucessfull."
	return render_to_response("1request_signup.html",diction)

	#password detail validation - min 1 special char, 1 number, 1 Caps lock char(No name allowed)

def l_check(request):
	email = request.POST['email']
	passwrd = request.POST['pass']
	a = req_user.objects.all().values()
	i=0
	flag=-1
	len1=len(a)
	g = admin_users.objects.all().values()
	i=0
	while i<len(g):
		if email==g[i]['name'] and g[i]['pwrd'] == passwrd:
			request.session['user_id'] = 3
			request.session['id'] = g[i]['id']
			return render_to_response("1userpage.html")
		i+=1
	i=0
	if a:
		while i<len(a):
			if a[i]['email'] == email and a[i]['passwrd'] == passwrd:
				print("hello")
				flag=1
				break
			i+=1
		if flag==1:
			request.session['user_id']=a[i]['user_id']
			request.session['id']=a[i]['id']
			diction=a[i].copy()
			if request.session.get('search'):
				if request.session['search'] == "true":
					request.session['search'] == "false"
					if request.session['user_id'] == 2:
						return render_to_response("1userpage.html", {'diction':diction})
					else:
						session={}
						session['set']=request.session['user_id']
						diction={}
						diction['result'] = "false"
						return render_to_response("1search.html", {'diction':diction, 'session':session})
				else:
					return render_to_response("1userpage.html", {'diction':diction})
			else:
				return render_to_response("1userpage.html", {'diction':diction})
		else:
			diction={}
			request.session['user_id']=0
			diction['result']="Incorrect email or password"
			return render_to_response("1login.html",{'diction':diction})
	else:
		diction={}
		diction['result']="Incorrect email or password"
		return render_to_response("1login.html",{'diction':diction})

def contract_signup(request):
	diction={}
	diction['value']=0
	return render_to_response("1contract_signup.html",diction)

def contract_check(request):
	diction={}
	user_id = 1
	diction['value']=0
	flag = 1
	flag1 = 1
	flag2 = 1
	recaptcha_response = request.POST.get('g-recaptcha-response')
	len1=len(recaptcha_response)
	if len1==0:
		return render_to_response("1request_signup.html")
	if 'cb' in request.POST:
		cb1 = request.POST['cb']
	else:
		cb1 = 0
	print(cb1)
	email = request.POST['email']
	pwrd = request.POST['pwrd']
	pwrd1 = request.POST['pwrd1']
	company_name = request.POST['com_name']
	u_name = request.POST['name']
	phno = request.POST['phno']
	len1 = len(pwrd)
	if len1 < 6:
		flag = -1
	if phno[0] =='9' or phno[0] =='8' or phno[0] =='7':
		len1 = len(phno)
		if len1 != 10:
			flag1 = -1
	else:
		flag1 = -1
	diction['value']=1
	if pwrd != pwrd1:
		flag2 = -1
	#######################################################

	#for checking whether the email has been used or no
	a = req_user.objects.all().values()
	i = 0
	flag3=1
	len1 = len(a)
	while i<len1:
		if a[i]['email']==email:
			flag3 = -1
			break
		i+=1

	i=0
	phno = int(phno)
	flag4=1
	while i<len1:
		if int(a[i]['phno'])==phno:
			flag4 = -1
			break
		i+=1
	if flag3 == -1:
		diction['result']="Email ID has already been taken."
	elif flag == -1:
		diction['result']="Password less that 6 characters."
	elif flag2 == -1:
		diction['result']="Both passwords don't match."
	elif flag1 == -1:
		diction['result']="Invalid phone nummber. Please re-check."
	elif flag4 == -1:
		diction['result']="Phone nummber has already been used. Please re-check."
	elif cb1 == 0:
		diction['result']="Please check the box"
	else:
		s = req_user()
		s.email	= email
		s.passwrd = pwrd
		s.c_name = company_name
		s.uname = u_name
		phno = int(phno)
		s.phno = phno
		s.user_id = int(user_id)
		s.save();
		diction['result']="Signup sucessfull."
	return render_to_response("1contract_signup.html",diction)

def save_tenderreq(request):
	u_id=request.session['id']
	flag=1
	flag1=1
	flag2=1
	diction={}
	t_type=request.POST['t_type']
	category=request.POST['category']
	print(category)
	prj_name=request.POST['prj_name']
	prj_desc=request.POST['prj_desc']
	reg_price=int(request.POST['reg_price'])
	if t_type=="Public":
		diction['result']="Public tenders are still under development"
	elif category=="":
		diction['result']="Please select the category."
	elif reg_price<100000:
		diction['result']="Minimum registration price is RS. 1,00,000."
	else:
		t_type = 2
		s = t_request()
		s.u_id	= u_id
		s.prj_name = prj_name
		s.t_type = t_type
		if category == "Educational Institutes":
			category = 1
		elif category == "Office Complex":
			category = 2
		elif category == "Entertainment":
			category = 3
		elif category == "Housing":
			category = 4
		elif category == "Hotels":
			category = 5
		s.category = category
		s.prj_desc = prj_desc
		s.reg_price = reg_price
		s.save();
		diction['result']="Request placed sucessfully."
	return render_to_response("1tender_request.html",diction)

class col1(TemplateView):
	template_name = "1menu.htm"

class col2(TemplateView):
	template_name = "1col2.htm"

def navbar(request):
	session={}
	if not request.session.get('user_id'):
		request.session['user_id']=0
	session['set']=request.session['user_id']
	return render_to_response("f_1navbar.html",{'session':session})

def under_dev(request):
	return render_to_response("1under_dev.html")

def edu_insti(request):
	a = t_request.objects.values().filter(category="1")
	diction={}
	d={}
	if a:
		len1 = len(a)
		i = 0
		while i<len1:
			d.update(a[i])
			diction[i]=d
			print(diction)
			d={}
			i+=1
		diction['result'] = "true"
	else:
		diction['category'] = 1
		diction['result'] = "false"
	return render_to_response("1proj_page.html", {'diction':diction})

def office(request):
	a = t_request.objects.values().filter(category="2")
	diction={}
	d={}
	if a:
		len1 = len(a)
		i = 0
		while i<len1:
			d.update(a[i])
			diction[i]=d
			print(diction)
			d={}
			i+=1
		diction['result'] = "true"
	else:
		diction['category'] = 2
		diction['result'] = "false"
	return render_to_response("1proj_page.html", {'diction':diction})

def entertainment(request):
	a = t_request.objects.values().filter(category="3")
	diction={}
	d={}
	if a:
		len1 = len(a)
		i = 0
		while i<len1:
			d.update(a[i])
			diction[i]=d
			print(diction)
			d={}
			i+=1
		diction['result'] = "true"
	else:
		diction['category'] = 3
		diction['result'] = "false"
	return render_to_response("1proj_page.html", {'diction':diction})

def housing(request):
	a = t_request.objects.values().filter(category="4")
	diction={}
	d={}
	if a:
		len1 = len(a)
		i = 0
		while i<len1:
			d.update(a[i])
			diction[i]=d
			print(diction)
			d={}
			i+=1
		diction['result'] = "true"
	else:
		diction['category'] = 4
		diction['result'] = "false"
	return render_to_response("1proj_page.html", {'diction':diction})

def hotels(request):
	a = t_request.objects.values().filter(category="5")
	diction={}
	d={}
	if a:
		len1 = len(a)
		i = 0
		while i<len1:
			d.update(a[i])
			diction[i]=d
			print(diction)
			d={}
			i+=1
		diction['result'] = "true"
	else:
		diction['category'] = 5
		diction['result'] = "false"
	return render_to_response("1proj_page.html", {'diction':diction})
#def col1(request):
#	return render_to_response("1menu.htm")

#def col2(request):
#	return render_to_response("1menu.htm")

def search(request):
	diction={}
	if not request.session.get('user_id'):
		diction['result'] = "null"
		request.session['search'] = "true"
		return render_to_response("1login.html", {'diction':diction})
	session={}
	session['set']=request.session['user_id']
	diction['result'] = "false"
	return render_to_response("1search.html", {'diction':diction, 'session':session})

def bidsearch(request):
	search = request.POST['search']
	a = t_request.objects.values().filter(prj_name=search)
	diction={}
	if a:
		diction['values'] = a[0]
		diction['result'] = "true"
		request.session['tender_bid'] = diction['values']['prj_name']
	else:
		diction['result'] = "false!"
	session={}
	session['set']=request.session['user_id']
	return render_to_response("1search.html", {'diction':diction, 'session':session})

def tender_bid(request):
	n = bid_request.objects.all().values()
	x = request.session['id']
	search = request.session['tender_bid']
	a = t_request.objects.values().filter(prj_name=search)
	diction={}
	if a:
		diction['values'] = a[0]
		request.session['whos_tender'] = a[0]['u_id']
		request.session['tender_id'] = a[0]['id'] 
		diction['result'] = "true"
		diction['result2'] = "null"
		request.session['tender_bid'] = diction['values']['prj_name']
	else:
		diction['result'] = "false!"
	i=0
	flag10=1
	while i<len(n):
		if x == n[i]['who_bid_for_it'] and a[0]['id'] == n[0]['tender_id']:
			flag10=-1
			break
		i+=1
	if flag10 == -1:
		diction['result23'] = "You cant bid for the same Project"
	else:
		diction['result23'] = "null"
	return render_to_response("1tender_bid.html", {'diction':diction})

def payment_gateway(request):
	diction={}
	request.session['payment_id'] = 0
	x = request.session['id']
	j = card_details.objects.values().filter(user_id=x)
	s = bid_request()
	s.who_bid_for_it=x
	s.whos_tender=request.session['whos_tender']
	s.tender_id=request.session['tender_id']
	s.org_name=request.POST['org_name']
	s.org_file=request.FILES['org_file']
	s.time=request.POST['time']
	s.cost=request.POST['cost']
	s.save()
	if j:
		diction=j[0].copy()
		diction['result']="true"
		if diction['exp_month'] == "01":
			diction['month'] = "January"
		elif diction['exp_month'] == "02":
			diction['month'] = "Febuary"
		elif diction['exp_month'] == "03":
			diction['month'] = "March"
		elif diction['exp_month'] == "04":
			diction['month'] = "April"
		elif diction['exp_month'] == "05":
			diction['month'] = "May"
		elif diction['exp_month'] == "06":
			diction['month'] = "June"
		elif diction['exp_month'] == "07":
			diction['month'] = "July"
		elif diction['exp_month'] == "08":
			diction['month'] = "August"
		elif diction['exp_month'] == "09":
			diction['month'] = "September"
		elif diction['exp_month'] == "10":
			diction['month'] = "October"
		elif diction['exp_month'] == "11":
			diction['month'] = "November"
		elif diction['exp_month'] == "12":
			diction['month'] = "December"
		print(diction)
		request.session['payment_id'] = diction['id']
		return render_to_response("1card_details.html",{'diction':diction})
	else:
		diction['result']="false"
		return render_to_response("1card_details.html",{'diction':diction})

@cache_control(no_cache=True,must_revalidate=True)
def logout(request):
	for key in list(request.session.keys()):
		del request.session[key]
	request.session.flush()
	session={}
	session['set']=0
	return render_to_response("1home.html",{'session':session})

def bid_confirm(request):
	diction={}
	user_id = request.session['id']
	card_owner = request.POST['owner_name']
	card_number = request.POST['card_number']
	exp_month = request.POST['month']
	exp_year = request.POST['year']
	cvv = request.POST['cvv']
	if len(cvv)!=3:
		diction['result'] = "Invalid CVV" 
	else:
		print(request.session['payment_id'])
		if request.session['payment_id'] != 0:
			x = request.session['payment_id']
			s = req_user.objects.get(id=x)
			s.user_id = user_id
			s.card_owner = card_owner
			s.card_number = card_number
			s.exp_month = exp_month
			s.exp_year = exp_year
			s.save()
		else:
			s = card_details()
			s.user_id = user_id
			s.card_owner = card_owner
			s.card_number = card_number
			s.exp_month = exp_month
			s.exp_year = exp_year
			s.save()
		diction['result'] = "Bid has been placed sucessfully."
	return render_to_response("1card_details.html",{'diction':diction})

def userpage(request):
	return render_to_response("1userpage.html", {'diction':diction})

def user_menu(request):
	if request.session['user_id'] == 1:
		diction={}
		diction['key1'] = "User Profile"
		diction['key2'] = "Edit user profile"
		diction['key3'] = "Still thinking"
	elif request.session['user_id'] == 2:
		diction={}
		diction['key1'] = "User Profile"
		diction['key2'] = "Edit user profile"
		diction['key3'] = "View requested tenders"
	elif request.session['user_id'] == 3:
		diction={}
		diction['key1'] = "View all users"
		diction['key2'] = "View all tenders"
		diction['key3'] = "Delete a user"
		diction['key5'] = "View Feedbacks"
		diction['key4'] = "Generate Report"
		return render_to_response("1admin_menu.html",{'diction':diction})
	diction['user_id'] = request.session['user_id']
	return render_to_response("1user_menu.html",{'diction':diction})

def welcome(request):
	if request.session['user_id'] == 3:
		x = request.session['id']
		a = admin_users.objects.values().filter(id=x)
		diction={}
		diction=a[0].copy()
		diction['uname'] = diction['name']
		return render_to_response("1welcome.html",{'diction':diction})
	x = request.session['id']
	a = req_user.objects.values().filter(id=x)
	diction={}
	diction=a[0].copy()
	print(diction)
	return render_to_response("1welcome.html",{'diction':diction})

def profile(request):
	x = request.session['id']
	a = req_user.objects.values().filter(id=x)
	diction={}
	diction=a[0].copy()
	print(diction)
	return render_to_response("1profile.html",{'diction':diction})

def update(request):
	x = request.session['id']
	a = req_user.objects.values().filter(id=x)
	diction={}
	diction=a[0].copy()
	diction['result'] = "true"
	return render_to_response("1update.html",{'diction':diction})

def save_update(request):
	x = request.session['id']
	j = req_user.objects.values().filter(id=x)
	diction={}
	diction=j[0].copy()
	email=request.POST['email']
	phno=request.POST['phno']
	c_name=request.POST['com_name']
	uname=request.POST['name']
	a = req_user.objects.all().values()
	i = 0
	flag=1
	len1 = len(a)
	while i<len1:
		if diction['email'] == email:
			flag = 1
			break
		if a[i]['email'] == email:
			flag = -1
			break
		i+=1
	b = re.search(r'^[789]\d{9}$',phno)
	if b:
		flag2=1
	else:
		flag2=-1
	if flag == -1:
		diction['result']="Email has already been used"
	elif flag2 == -1:
		diction['result']="Invalid contact number"
	else:
		s = req_user.objects.get(id=x)
		s.email=email
		s.c_name=c_name
		s.uname=uname
		s.phno=phno
		s.save()
		diction['result']="Update Sucessfull"
	return render_to_response("1update.html",{'diction':diction})

def view_req_tenders(request):
	x = request.session['id']
	j = t_request.objects.values().filter(u_id=x)
	diction={}
	i=0
	if j:
		while i<len(j):
			diction[i]=j[i]
			i+=1
	else:
		diction['result']="false"
	print(diction)
	return render_to_response("1view_req_tenders.html",{'diction':diction})

def storefeedback(request):
	s = feedback()
	s.uname = request.POST['name']
	s.email = request.POST['email']
	s.subject = request.POST['subject']
	s.message = request.POST['message']
	s.save()
	session={}
	if not request.session.get('user_id'):
		request.session['user_id']=0
		session['set']=request.session['user_id']
		return render_to_response("1home.html",{'session':session})
	else:
		x = request.session['id']
		a = req_user.objects.values().filter(id=x)
		diction={}
		diction=a[0].copy()
		return render_to_response("1userpage.html", {'diction':diction})

def view_users(request):
	a = req_user.objects.all().values()
	i=0
	diction={}
	if a:
		while i<len(a):
			diction[i] = a[i]
			i+=1
		diction['result'] = "true"
	else:
		diction['result'] = "false"
	return render_to_response("1view_users.html", {'diction':diction})

def view_tenders(request):
	a = t_request.objects.all().values()
	i=0
	diction={}
	if a:
		while i<len(a):
			diction[i] = a[i]
			i+=1
		diction['result'] = "true"
	else:
		diction['result'] = "false"
	return render_to_response("1view_tenders.html", {'diction':diction})

def delete_user(request):
	return render_to_response("1user_search.html")

def user_search(request):
	name=request.POST['search']
	a = req_user.objects.all().values()
	i=0
	flag=-1
	diction={}
	if a:
		while i<len(a):
			if name==a[i]['uname']:
				diction[0] = a[i].copy
				flag=1
				break
			i+=1
		if flag==1:
			diction['result'] = "true"
			request.session['delete'] = a[i]['id']
		else:
			diction['result'] = "User not found."
	else:
		diction['result'] = "User not found"
	return render_to_response("1user_search.html", {'diction':diction})

def delete_all_user_details(request):
	x = request.session['delete']
	j = req_user.objects.filter(id=x)
	if j:
		j.delete()
	j = t_request.objects.filter(u_id=x)
	if j:
		j.delete()
	j = bid_request.objects.filter(whos_tender=x)
	if j:
		j.delete()
	diction={}
	diction['result23'] = "true"
	return render_to_response("1user_search.html", {'diction':diction})

def generate_report(request):
	f = open("report.txt","w+")
	a = req_user.objects.all()
	f.write("\n USER DETAILS\n ------------\n")
	f.write("\n The number of users registered: "+str(len(a)))
	a = req_user.objects.filter(user_id=1)
	f.write("\n The number contractors registered: "+str(len(a)))
	a = req_user.objects.filter(user_id=2)
	f.write("\n The number requesters registered: "+str(len(a)))
	a = t_request.objects.all()
	f.write("\n\n Tender Categories\n -----------------\n\n")
	a = tender_type.objects.all().values()
	i = 0
	while i<len(a):
		f.write(" "+str(i+1)+". "+str(a[i]['t_type'])+"\n")
		i+=1
	f.write("\n Private tenders\n ---------------\n")
	a = t_request.objects.all()
	f.write("\n The number of private tenders requested: "+str(len(a)))
	a = category_type.objects.all().values()
	i=0
	j=1
	print(a)
	while i<len(a):
		b = t_request.objects.filter(category=int(j))
		print(len(b))
		f.write("\n The number of tenders ("+str(a[i]['category'])+") requested: "+str(len(b)))
		i+=1
		j+=1
	return render_to_response("1generate.html")

def view_feedbacks(request):
	a = feedback.objects.all().values()
	i=0
	diction={}
	if a:
		while i<len(a):
			diction[i] = a[i]
			i+=1
		diction['result'] = "true"
		print(diction)
	else:
		diction['result'] = "false"
	return render_to_response("1view_feedbacks.html", {'diction':diction})