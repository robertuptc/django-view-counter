from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import random
import datetime
# Create your views here.
users = {}

def index(request):
    print(users)
    user_id_number = request.COOKIES.get('user_id_number')
    print(user_id_number)
    user = users.get(user_id_number)
    if not user:
        user_id_number = str(random.randint(100000,999999))
        
        users[user_id_number] = {
            'count': 1,
            'start_time': datetime.datetime.now()
        }
    else:
        users[user_id_number]['count'] += 1
    response = render(request, "pages/index.html", users[user_id_number])
    # print(response)
    response.set_cookie('user_id_number', user_id_number)
    print(response)
    return response

# return render(request, "pages/index.html")
