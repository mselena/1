'''user_info={'first_name':'','last_name':''}
first_name= input('введите имя')
user_info['first_name']= first_name
last_name= input('введите фамилию')
user_info['last_name']= last_name
print(user_info)'''
def get_summ(one, two):
    get_summ1= (one + two).upper()
    return get_summ1
print (get_summ('helo', 'world'))
