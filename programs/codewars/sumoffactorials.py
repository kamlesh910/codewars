def sum_factorial(lst):
   sum=0
   for it in lst:
       t1=1
       for x in range(1,it+1):
           t1=t1*x
       sum+=t1
   return sum