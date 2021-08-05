def sort_list(d):
    # def helper(eme):
    #     total_sales = 0
    #     for k,v in eme['unit_sales'].items():
    #         #print(k)
    #         total_sales += v

    #     return total_sales

    d.sort(key = lambda x: sum(v for k,v in x['unit_sales'].items()))
    print(d)

def sort_tuple(d):
    d.sort(key = lambda x: sum(x[3]))
    print(d)

r = [('Aakash',19,8,[10,8]),('Pragya',9,4,[10,90]),('Dirghya',10,6,[10,11])]
sort_tuple(r)
m = [('A',(9,8,15)),('B',(4,7,9)),('D',(6,9,10))]
m.sort(key =lambda x:x[1][2])
print(m)
d = [
    {'name':'Aakash',
    'unit_sales':{
        'orange':5,
        'apple':2,
        'mango':3,
        'pineapple':4
    }
    },
    {
        'name':'Pragya',
        'unit_sales':{
            'orange':8,
            'apple':4
        }
    }
]

sort_list(d)


