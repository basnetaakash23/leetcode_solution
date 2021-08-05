def unit_conversion(num, ini, fi):
    unit = {
        '1 km' : ['1000 m','3982 feet','0.625 mile'],
        '1 m' : ['100 km'],
        '1 feet': ['12 inch','0.001 km'],
        '1 inch': ['0.0833 feet'],
        '1 mile': ['1.6 km']    
    }
    k = ini  #1st key will be with 1 added to it
    v = unit["1 "+ini] 
    def convert(num, ini, k, f, t, c):
       
        if(c == 6):  #expecting a maximum of 6 level of recursion
            return
        if(k == f):
            print(num*t,f,"Ended")
            return
        val = unit["1 "+k]
        
        for ele in val:
            temp_ele = ele.split(" ")[1]
            if(temp_ele == ini):
                continue

            temp_val = float((ele.split(" ")[0]))
            convert(num, ini, temp_ele, f, t*temp_val, c+1)


    convert(num,ini, k, fi, 1, 0)
    

unit_conversion(24000, "inch", "mile")
