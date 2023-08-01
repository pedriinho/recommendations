from django.shortcuts import render
import json
# Create your views here.
def increment_recommendation(data, item1, item2):
    if item1 == item2:
        return

    if item1 not in data:
        data[item1] = {}
    if item2 not in data[item1]:
        data[item1][item2] = 0

    data[item1][item2] += 1

def index(request):
    context = {}

    if request.method == 'POST':
        purchase = json.loads(request.body.decode('utf-8'))
        with open('app/dados.json', 'r') as file:
            data = json.load(file)
            
            for i, item1 in enumerate(purchase['items']):
                for j in range(i + 1, len(purchase['items'])):
                    increment_recommendation(data, item1, purchase['items'][j])
                    increment_recommendation(data, purchase['items'][j], item1)
        
        with open('app/dados.json', 'w') as file:
            file.write(json.dumps(data))

            


    return render(request, 'index.html', context)