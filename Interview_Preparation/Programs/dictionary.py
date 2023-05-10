d = {
    'course':'python',
    'fees' :8000,
    'duration':'2 months'

}
"""for a,b in d.items():
    print(a,b)"""# -----> 

"""del d['duration']
print(d)""" # -----> del will dont show 

"""print(d.pop('fees'))
print(d)"""# ------------> pop will remove value and also show the del items

"""n = d.get('duration')
print(n)""" # ---> using keys will get value

"""for a in d.keys():
    print(a)"""

"""for a in d.values():
    print(a)""" # ------> using values 