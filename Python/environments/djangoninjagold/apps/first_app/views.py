from django.shortcuts import render, HttpResponse, redirect
import random
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    else:
        count = request.session['count']
    if 'message' not in request.session:
        request.session['message'] = ''
    else:
        message = request.session['message']
    context = {
                'message' : request.session['message'],
                'count' : int(request.session['count']),
            }
    return render(request,'first_app/ngold.html', context)
def process(request):
    if request.POST['action'] == 'farm':
        request.session['count'] = request.session['count']+random.randrange(10,20)
        request.session['message'] = request.session['message']+'Where did you find '+str(request.session['count'])+' gold on a farm. '
    elif request.POST['action'] == 'cave':
        request.session['count'] = request.session['count']+random.randrange(5,10)
        request.session['message'] = request.session['message']+'Where did you find '+str(request.session['count'])+' gold in a cave. '
    elif request.POST['action'] == 'house':
        request.session['count'] = request.session['count']+random.randrange(2,5)
        request.session['message'] = request.session['message']+'Where did you find '+str(request.session['count'])+' gold in a house. '
    elif request.POST['action'] == 'casino':
        request.session['count'] = request.session['count']+50-random.randrange(0,100)
        request.session['message'] = request.session['message']+'Where did you find '+str(request.session['count'])+' gold in a casino. '
    return redirect('/')
