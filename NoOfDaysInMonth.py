month = 12
year=2012
    
if((month==2) and ((year%4==0)  or ((year%100==0) and (year%400==0)))) :
    # if leap year feb will has 29 days
    print("Number of days is 29");

elif(month==2) :
    # feb has 28
    print("Number of days is 28");

elif(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) :
    print("Number of days is 31");

else :
    print("Number of days is 30");