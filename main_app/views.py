from django.shortcuts import render

# Create your views here.
coins = [
    {'name':'Saint-Gaudens Double Eagle','country':'United States','year':'1907 to 1933','original_price':'$20','current_price':'$20,212,100'},   
    {'name':'Flowing Hair Silver Dollar','country':'United States','year':'1794 to 1795','original_price':'$1','current_price':'$13,311,850'}, 
    {'name':'Brasher Doubloon','country':'United States','year':'1787','original_price':'$15','current_price':'$10,009,500'},
    {'name':'Edward III Florin','country':'England','year':'1343 ','original price':'6 shillings','current_price':'$6,816,000'},
    {'name':'Umayyad Gold Dinar','country':'Umayyad','year':'723','original_price':'Unknown','current_price':'5,418,400'},
    {'name':'Canadian Gold Maple Leaf','country':'Canada','year':'2007','original_price':'$1,000,000','current_price':'5,315,400'},
    {'name':'Liberty Head V Nickel','country':'United States','year':'1913 ','original_price':'5 cents','current_price':'$5,262,100'},
    {'name':'Barber Dime','country':'United States','year':'1894','original_price':'$0.10','current_price':'$2,412,200'},
    {'name':'Lincoln Head Copper Penny','country':'United States','year':'1943 ','original_price':'1 cent','current_price':'$2,325,200'},
    {'name':'Morgan Silver Dollar','country':'United States','year':'1893','original_price':'$1','current_price':' $551,272'},
    {'name':'Sacagawea Cheerios Dollar','country':'United States','year':'2000','original_price':'$1','current_price':'$25,058'}
]


def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')

def about(request):

    return render(request, 'about.html')

def coins_index(request):
    #we pass data to a template like we did in express 
    return render(request, 'coins/index.html', {
        'coins': coins
    })
