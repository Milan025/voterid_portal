from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import auth
from evoterid.models import Suggestion#import pymysql
from evoterid.models import User
from evoterid.models import deletetable
from evoterid.models import modification
from django.template.context_processors import csrf
from django.template import RequestContext
from django.views import generic# Create your views here.
from django.core.mail import EmailMultiAlternatives
import uuid

class UserListView(generic.ListView):
	model = User

class SuggestionListView(generic.ListView):
	model = Suggestion

class deleteListView(generic.ListView):
	model = deletetable

class modificationListView(generic.ListView):
	model = modification

def getuserinfo(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('index.html', c)

def deluserinfo(request):
	uid = request.session.get('id')
	user = User.objects.filter(id = uid)
	u = User.objects.get(id = uid)
	subject, from_email, to = 'confirm Email', 'from@example.com',u.email_id
	text_content =( "hey! " + u.name +  " you applied application Rejected please apply again")
	msg = EmailMultiAlternatives(subject,text_content,from_email,[to])
	try:
		msg.send()
	except:
		print('some problem')
		return HttpResponse("ERROR")
	for u in user:
		u.delete()
	return render_to_response('delrecord.html')

def deluserinfo8(request):
	uid = request.session.get('id')
	user = modification.objects.filter(voterid = uid)
	u = User.objects.get(id = uid)
	subject, from_email, to = 'confirm Email', 'from@example.com',u.email_id
	text_content =( "hey! " + u.name +  " you applied update application  was Rejected please apply again")
	msg = EmailMultiAlternatives(subject,text_content,from_email,[to])
	try:
		msg.send()
	except:
		print('some problem')
		return HttpResponse("ERROR")
	for u in user:
		u.delete()
	return render_to_response('delrecode2.html')

def deluserinfo7(request):
	uid = request.session.get('id')
	print(uid)
	u = deletetable.objects.get(voterid = uid)

	print(u.email_id)
	subject, from_email, to = 'confirm Email', 'from@example.com',u.email_id
	text_content =( "hey! " + u.name +  " you applied delete application  was successfully  applied")
	msg = EmailMultiAlternatives(subject,text_content,from_email,[to])
	try:
		msg.send()
	except:
		print('some problem')
		return HttpResponse("ERROR")
	u = deletetable.objects.filter(voterid = uid)
	u.delete()
	return render_to_response('deleterecord.html')

def adduserinfo(request):
	ustate = request.POST.get('state', '')
	udistrict = request.POST.get('district', '')
	uassembly = request.POST.get('assembly', '')
	unm = request.POST.get('anm', '')
	uasurnm = request.POST.get('asurnm', '')
	uarnm = request.POST.get('arnm', '')
	uarsurnm = request.POST.get('arsurnm', '')
	urelation = request.POST.get('relation', '')
	udob = request.POST.get('dob', '')
	ugender = request.POST.get('gender', '')
	ushouseno = request.POST.get('hno', '')
	uaddress = request.POST.get('street', '')
	utown = request.POST.get('town', '')
	upin = request.POST.get('pin', '')
	uemail = request.POST.get('email', '')
	umo_number = request.POST.get('mno', '')
	uphoto = request.FILES['photo']
	uageproof = request.FILES['ageproof']
	utypeageproof = request.POST.get('typeageproof', '')
	uaddproof = request.FILES['addproof']
	utypeaddproof = request.POST.get('typeaddproof', '')
	uplace = request.POST.get('place', '')
	u = User(state = ustate,district = udistrict,assembly = uassembly,name = unm,srname = uasurnm,r_name = uarnm,r_srname = uarsurnm,relation = urelation,birthday = udob,gender = ugender,houseno = ushouseno,address = uaddress,town = utown,pin = upin,email_id = uemail,mo_number = umo_number,photo = uphoto,age_p = uageproof,typeageproof = utypeageproof,add_p = uaddproof,typeaddproof = utypeaddproof,place = uplace )
	u.save()

	return HttpResponseRedirect('/evoterid/addsuccess/')

def addsuccess(request):
	u=User.objects.all()
	k=''
	e=''
	name=''
	for i in u:
		id=i.id
		k=i.id
		e=i.email_id
		name=i.name
	subject, from_email, to = 'confirm Email', 'from@example.com',e
	text_content =( "hey! " + name +  " you apply successfull " + " your temparory application id: "  + str(k))
	msg = EmailMultiAlternatives(subject,text_content,from_email,[to])
	try:
		msg.send()
	except:
		print('some problem')
		return HttpResponse("ERROR")
	context={
		'users':id,
		'name':name
		}
	return render(request,'success.html',context=context)

def addsuccess1(request):
	u=modification.objects.all()
	for i in u:
		id=i.voterid
		print(id)
		name=i.name
		print(name)
	context={
		'users':id,
		'name':name
		}
	return render(request,'success1.html',context=context)

def addsuccess2(request):
	u=deletetable.objects.all()
	for i in u:
		id=i.voterid
		print(id)
		name=i.name
		print(name)
	context={
		'users':id,
		'name':name
		}
	return render(request,'success2.html',context=context)

def idmodification(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('idmodification.html',c)

def form6(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('form6.html',c)

def form8(request):
	uid = request.POST.get('id', '')
	uname = request.POST.get('name', '')
	print(uid)
	print(uname)
	c = {}
	c.update(csrf(request))
	u=User.objects.get(id=uid)
	name=u.name
	print(u.birthday)
	print(name)
	context={
		'user':u
	}
	print(name==uname)
	if name==uname:
		print("enter")
		return render(request,'form8.html',context=context)
	else:
		print("wait")
		return render_to_response('idmodification.html',c)

def form7(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('form7.html',c)

def search(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('search.html',c)

def treak(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('treak.html',c)

def treak1(request):
	uid = request.POST.get('id', '')
	u=User.objects.filter(id=uid)
	print(u)
	context={

		'name':u
		}
	return render(request,'treak1.html',context=context)

def verify(request):
	return render_to_response('verify.html')

def admin(request):
	return render_to_response('admin.html')

def about(request):
	return render_to_response('about.html')

def contact(request):
	return render_to_response('contact.html')

def soon(request):
	return render_to_response('soon.html')

def sugcom(request):
	return render_to_response('sugcom.html')

def addmodificationinfo(request):
	ustate = request.POST.get('state', '')
	udistrict = request.POST.get('district', '')
	uassembly = request.POST.get('assembly', '')
	uoldnm = request.POST.get('oldname', '')
	uoldsrnm = request.POST.get('oldsrnmae', '')
	uvoterid = request.POST.get('vidno', '')
	unm = request.POST.get('anm', '')
	uasurnm = request.POST.get('asurnm', '')
	uarnm = request.POST.get('arnm', '')
	uarsurnm = request.POST.get('arsurnm', '')
	urelation = request.POST.get('relation', '')
	udob = request.POST.get('dob', '')
	ugender = request.POST.get('gender', '')
	ushouseno = request.POST.get('hno', '')
	uaddress = request.POST.get('street', '')
	utown = request.POST.get('town', '')
	upin = request.POST.get('pin', '')
	uemail = request.POST.get('email', '')
	umo_number = request.POST.get('mno', '')
	uphoto = request.FILES['photo']
	uageproof = request.FILES['ageproof']
	utypeageproof = request.POST.get('typeageproof', '')
	uaddproof = request.FILES['addproof']
	utypeaddproof = request.POST.get('typeaddproof', '')
	uplace = request.POST.get('place', '')
	print(unm)
	print(utown)
	print(uarnm)
	print(uphoto)
	u = modification(state = ustate,district = udistrict,assembly = uassembly,oldname = uoldnm,oldsrname = uoldsrnm,voterid = uvoterid,name = unm,srname = uasurnm,r_name = uarnm,r_srname = uarsurnm,relation = urelation,birthday = udob,gender = ugender,houseno = ushouseno,address = uaddress,town = utown,pin = upin,email_id = uemail,mo_number = umo_number,photo = uphoto,age_p = uageproof,typeageproof = utypeageproof,add_p = uaddproof,typeaddproof = utypeaddproof,place = uplace )
	u.save()
	print(u.photo)
	return  HttpResponseRedirect('/evoterid/addsuccess1/')


def deleteform(request):
	ustate = request.POST.get('state', '')
	udistrict = request.POST.get('district', '')
	uassembly = request.POST.get('assembly', '')
	uvoterid = request.POST.get('voterid', '')
	ureason = request.POST.get('objr', '')
	unm = request.POST.get('name', '')
	uasurnm = request.POST.get('asurnm', '')
	udelete = request.POST.get('reason', '')
	ushouseno = request.POST.get('hno', '')
	uaddress = request.POST.get('street', '')
	utown = request.POST.get('town', '')
	upin = request.POST.get('pin', '')
	uemail = request.POST.get('email', '')
	umo_number = request.POST.get('mno', '')
	uplace = request.POST.get('place', '')
	uphoto = request.FILES['photo']
	u = deletetable(photo=uphoto,state = ustate,district = udistrict,assembly = uassembly,voterid = uvoterid,reason=ureason,delete =udelete,name = unm,srname = uasurnm,houseno = ushouseno,address = uaddress,town = utown,pin = upin,email_id = uemail,mo_number = umo_number,place = uplace )
	u.save()
	return HttpResponseRedirect('/evoterid/addsuccess2/')

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	targate = request.POST.get('blo', '')
	print(username)
	print(password)
	print(targate)
	user = auth.authenticate(username=username,password=password)
	if user is not None:
		auth.login(request, user)
		if targate=="verification":
			return HttpResponseRedirect('/evoterid/loggedin/',RequestContext(request))
		elif targate=="update":
			return HttpResponseRedirect('/evoterid/modification/',RequestContext(request))
		elif targate=="delete":
			return HttpResponseRedirect('/evoterid/delete/',RequestContext(request))
	else:
		return HttpResponseRedirect('/evoterid/invalidlogin/',RequestContext(request))

def loggedin(request):
    return HttpResponseRedirect('/evoterid/users/',RequestContext(request))
def invalidlogin(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('verify.html',c)





def logout(request):
    auth.logout(request)
    return render_to_response('index.html')
def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('verify.html', c)

def getsearchname(request):
	c = {}
	c.update(csrf(request))
	return render(request,'search.html', c)


def searchresult(request):
	uid=request.POST.get("search")
	u=User.objects.filter(uuid=uid)
	if u is None:
		context={
			'users':None,
			}
	else:
		users=User.objects.all()
		context={
			'users':u,
			}

	return render(request,'searchresult.html',context=context)


def suggestion(request):
	utarget = request.POST.get('cs', '')
	print(utarget)
	request.session['T'] = utarget
	username = request.POST.get('unm', '')
	password = request.POST.get('pass', '')
	print(username)
	print(password)
	if(utarget == "officer"):
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('/evoterid/loggedin1/',RequestContext(request))
		else:
			return HttpResponseRedirect('/evoterid/invalidlogin1/',RequestContext(request))
	else:
		return HttpResponseRedirect('/evoterid/loggedin1/',RequestContext(request))

def loggedin1(request):
    return HttpResponseRedirect('/evoterid/feedback/',RequestContext(request))

def invalidlogin1(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('sugcom.html',c)

def login1(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('sugcom.html', c)

def feedback(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('feedback.html',c)

def addsugcom(request):
	uname = request.POST.get('name', '')
	sugcom = request.POST.get('suggestion', '')
	utarget = request.session.get('T')
	u = Suggestion(name = uname,suggestion = sugcom,target=utarget )
	u.save()
	return HttpResponseRedirect('/evoterid/addsuccess4/')

def addsuccess4(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('successfeedback.html',c)

def verification(request):
	uid = request.session.get('id')
	User.objects.filter(id = uid).update(status = "verify")
	u=User.objects.get(id = uid)
	userid = uuid.uuid4()
	arr=str(userid).split("-")
	print (arr[0])
	subject, from_email, to = 'confirm Email', 'from@example.com',u.email_id
	text_content =( " hey! " + u.name +  " your varification successfully " + "your voter id: "  + str(arr[0]) )
	msg = EmailMultiAlternatives(subject,text_content,from_email,[to])
	try:
		msg.send()
	except:
		print('some problem')
		return HttpResponse("ERROR")
	User.objects.filter(id = uid).update(uuid = arr[0])
	return HttpResponseRedirect('/evoterid/successverify/')

def successverify(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('home.html',c)

def update(request):
	uid = request.session['id']
	print(uid)
	M=modification.objects.get(voterid = uid)
	print(M)
	print(M.voterid)
	User.objects.filter(id = M.voterid).update(state = M.state,district = M.district,assembly = M.assembly,name = M.name,srname = M.srname,r_name = M.r_name,r_srname = M.r_srname,relation = M.relation,birthday = M.birthday,gender = M.gender,houseno = M.houseno,address = M.address,town = M.town,pin = M.pin,email_id = M.email_id,mo_number = M.mo_number,photo = M.photo,age_p = M.age_p,typeageproof = M.typeageproof,add_p = M.add_p,typeaddproof = M.typeaddproof,place = M.place )
	M.delete()
	u=User.objects.get (id = uid)
	subject, from_email, to = 'confirm Email', 'from@example.com',u.email_id
	text_content =( " hey! " + u.name +  " your id  modification successfully update   ")
	msg = EmailMultiAlternatives(subject,text_content,from_email,[to])
	try:
		msg.send()
	except:
		print('some problem')
		return HttpResponse("ERROR")
	context={
		'user':u,
	}
	return render(request,'updatesucess.html',context)

def view(request):
	uid=request.POST.get("id")
	request.session['id'] = uid
	u=User.objects.filter(id=uid)
	if u is None:
		context={
			'users':None,
			}
	else:
		users=User.objects.all()
		context={
			'users':u,
			}

	return render(request,'view.html',context=context)

def view1(request):
	uid=request.POST.get("id")
	request.session['id'] = uid
	u=User.objects.filter(id=uid)
	if u is None:
		context={
			'users':None,
			}
	else:
		users=User.objects.all()
		context={
			'users':u,
			}

	return render(request,'onlyview.html',context=context)

def updateview(request):
	uid=request.POST.get("id")
	request.session['id'] = uid
	print(uid)
	u=User.objects.filter(id=uid)
	print(u)
	M=modification.objects.filter(voterid=uid)
	print(M)
	if u is None:
		context={
			'users':None,
			}
	else:
		context={
			'users':u,
			'modification':M,
			}
	return render(request,'updateview.html',context=context)

def deleteview(request):
	uid=request.POST.get("id")
	request.session['id'] = uid
	u=deletetable.objects.filter(voterid=uid)
	if u is None:
		context={
			'users':None,
			}
	else:
		context={
			'users':u,
			}

	return render(request,'deleteview.html',context=context)

def allview(request):
	u=User.objects.all()
	for i in u:
		id=i.id
	print(i)
	print(u)

	if u is None:
		context={
			'users':None,
			}
	else:
		context={
			'users':u,
			}

	return render(request,'allview.html',context=context)

def admin_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	targate = request.POST.get('admin', '')
	print(username)
	print(password)
	print(targate)
	if targate=="suggestion" and username == 'krinish' and password == "shree291":
		return HttpResponseRedirect('/evoterid/loggedin2/',RequestContext(request))
	elif targate=="Alluser" and username == 'krinish' and password == "shree291":
		return HttpResponseRedirect('/evoterid/allview/',RequestContext(request))
	else:
		return HttpResponseRedirect('/evoterid/invalidlogin2/',RequestContext(request))
def login2(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('admin.html', c)
def loggedin2(request):
    return HttpResponseRedirect('/evoterid/Suggestion/',RequestContext(request))
def invalidlogin2(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('admin.html',c)
