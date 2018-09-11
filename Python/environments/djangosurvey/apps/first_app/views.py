from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'first_app/index.html')
def user(request):
    if request.method == "POST":
        context = {
            'lang' : request.POST['lang'],
            'loc' : request.POST['loc'],
            'email' : request.POST['email'],
            'comment' : request.POST['comment'],
        }
        request.session['context'] = context
        return redirect("/result")
    else:
        return redirect("/")
def result(request):
    context = request.session['context']
    return render(request,'first_app/show.html', context)
#WORD ASSIGNMENT
def word(request):
    if 'wordlist'not in request.session:
        context = {}
    else: 
        context = {
            'list' : request.session['wordlist']
        }
    return render(request,'first_app/word.html', context)
def sesh(request):
    if request.method == "POST":
        if 'wordlist'not in request.session:
            if 'big_font' in request.POST:
                showbig = 1
            else:
                showbig = 0
            context = {
                'word' : request.POST['word'],
                'color' : request.POST['color'],
                'big_font' : int(showbig),
            }
            request.session['wordlist'] = [context]
        else:
            wordlist = request.session['wordlist']
            if 'big_font' in request.POST:
                showbig = 1
            else:
                showbig = 0
            wordlist.append({"word": request.POST['word'], "color": request.POST['color'], "show_big": int(showbig)})
            request.session['wordlist'] = wordlist
        return redirect("/session_word")
    else:
        return redirect("/session_word")