from django.http import HttpResponse
from django.shortcuts import render
from operator import itemgetter
def Homepage(request):
    return render(request, 'home.html')

def counter(request):


    data = request.GET['fulltext']

    word_list = data.split()
    words= len(word_list)
    worddictionary = {}
    for kv in word_list:
        if kv in worddictionary:
            worddictionary[kv] += 1
        else:
            worddictionary[kv] = 1
    sorted_list = sorted(worddictionary.items(), key=itemgetter(1), reverse=True)

    return render(request, 'counting.html', {'fullcontentt': data, 'length': words, 'frequencycounter': sorted_list})
