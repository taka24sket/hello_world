# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 22:56:00 2020

@author: takashi.shiozawa
"""


def house_for_rent(bedroom=2,walk_min=6,house_type="アパート",rent_yen=50):
    return{"bedroom":bedroom,"walk_min":walk_min,"house_type":house_type,"rent_yen":rent_yen}

house_for_rent

def number_to_day(num=0):
    if num==0:
        day = "今日"
    elif num==1:
        day = "明日" 
    elif num==-1:
        day = "昨日"
    else:
        day = "それ以外"
    return day

number_to_day()
number_to_day(1)
number_to_day(3)
number_to_day(-1)

def perran(m=100):
    a,b,c = 3,0,2
    result = []
    while a < m:
        result.append(a)
        a,b,c = b,c,a+b
    return result

perran()

def show_args(*args):#引数の数は任意
    print("Positional aruguments:",args)
    return args

show_args(1,2,3,"da!")

def show_kwargs(**kwargs):
    print("Keywprd arguments:",kwargs)
    return kwargs

a = show_kwargs(pasta="ペンネ",drink="赤ワイン",main_dish="肉料理",n_customers=3)

positional_args = [4,5,6,"ya"]
show_args(*positional_args)

keyword_args = {"pasta":"ペンネ","drink":"赤ワイン","main_dish":"肉料理","n_customers":3}
show_kwargs(**keyword_args)

def concat_word(*args,separator ="."):
    return separator.join(args)

b = concat_word("a","b","c","d",separator = "_")

Positional_args = (4,5,6,"ya")
a = Positional_args

names = ("b","c","d")

many_number = list(range(100))

def func_square(*args):
    results = []
    for i in args:
        results.append(i*i)
    return results

numbers = [1,2,3,4]
func_square(*many_number)

animal = "cat"

def my_func():
    vegetable = "carot"
    print("animal in my_func:", animal)
    print("vegetable in my_func:", vegetable)
    
my_func()
print(animal)    
print(vegetable)


global_list = ["tomato","spninach","pumpkin"]

def add_to_head(i):
    print("global_list:",global_list)
    global_list.insert(0,i)
    print("global_list_add")
    print("global_list:",global_list)
    
add_to_head("egg")    




