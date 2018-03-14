from django.shortcuts import render, render_to_response
from math import sqrt
import time

def fibonacci(request):
    if request.method == 'GET':
        return render(request, 'welcome.html')
    else:
        start_time = time.time()
        n = int(request.POST.get('index_value'))
        t = ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
        print("--- %s seconds ---" % (time.time() - start_time))
        # return render_to_response('welcome.html', {'fib_value': int(t), 'time': time.time() - start_time})
        return render(request, 'welcome.html', {'fib_value': int(t), 'time': time.time() - start_time})