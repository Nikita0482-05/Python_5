import random as rnd
import statistics as st
import math

nums = [rnd.randint(1, 100) for num in range(100)]  

mean = st.mean(nums)          
median = st.median(nums)      
stdev = st.stdev(nums)        
sqrt_sum = math.sqrt(sum(nums)) 

print(f"Среднее: {round(mean, 2)}, "
      f"Медиана: {median}, "
      f"Стандартное отклонение: {round(stdev, 2)}, "
      f"Корень из суммы: {round(sqrt_sum, 2)}")



