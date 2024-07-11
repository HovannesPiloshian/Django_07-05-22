from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def calculator(request):
    res = 0
    if request.method == "POST":
        number1 = int(request.POST.get('number1'))
        char = request.POST.get('char')
        number2 = int(request.POST.get('number2'))
        if char == '+':
            res = number1 + number2
        elif char == '-':
            res = number1 - number2
        elif char == '*':
            res = number1 * number2
        elif char == '/':
            try:
                res = number1 / number2
            except ZeroDivisionError:
                res = 'ERROR'
        elif char == '**':
            res = number1 ** number2
        elif char == '%':
            res = number1 % number2
        elif char == '//':
            res = number1 // number2
    return render(request, 'calculator.html', context={
        'res':res
    })

def fibonacci(request):
    n1 = 0
    n2 = 1
    res = sequence = []
    if request.method == 'POST':
        number = int(request.POST.get('number'))
        while len(sequence)< number:
            sequence.append(n1)
            n1, n2  = n2, n1 + n2
    return render(request, 'fib.html', context={
        'res':res

    })

def factorial(request):
    res = 1
    if request.method == 'POST':
        number = int(request.POST.get('number'))
        for i in range(1, number + 1):
            res *= i
    return render(request, 'fact.html', context={
        'res':res
    })

def hello(request):
    res = ''
    if request.method == "POST":
        name = request.POST.get("name")
        res = name
    return render(request,'hello.html',context={
        "res":res,
    })
            
        
