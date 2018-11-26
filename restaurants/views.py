from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	"my_list": [

    			{
    			"restaurant_name": "ShrimpoO",
    			 "food_type": "seafood"
    			}, 
    			{
    			"restaurant_name": "Nino",
    			 "food_type": "italian food"
    			},
    			{
    			"restaurant_name": "Taj",
    			 "food_type": "indian food"
    			},
    	]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	"my_object": {

    			"restaurant_name": "Breadtalk",
    			 "food_type": "sweets and cake"
    	}

    }
    return render(request, 'detail.html', context)
