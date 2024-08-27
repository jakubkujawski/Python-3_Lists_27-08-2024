Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
nums = [25, 12,36, 95,14]
nums
[25, 12, 36, 95, 14]
nums[0]
25
nums[54\]
     
SyntaxError: unexpected character after line continuation character
nums[3]
     
95
nums[2:]
     
[36, 95, 14]
nums[4]
     
14
nums[-1]
     
14
names = ['Jakub','Tom','Mark']
     
names
     
['Jakub', 'Tom', 'Mark']
values =[9.5, 'Jakub', 25]
     
mil = [nums, names]
     
mil
     
[[25, 12, 36, 95, 14], ['Jakub', 'Tom', 'Mark']]
nums.append(45)
     
nums
     
[25, 12, 36, 95, 14, 45]

nums.insert(2,77)
     
nums
     
[25, 12, 77, 36, 95, 14, 45]

# when calling function .insert then first number specify for index and second for value of the number
     
nums.remove(14)
     
nums
     
[25, 12, 77, 36, 95, 45]

nums.pop(1)
     
12
>>> nums
...      
[25, 77, 36, 95, 45]
>>> 
>>> nums.pop()
...      
45
>>> nums
...      
[25, 77, 36, 95]
>>>  del nums[1:]
...      
SyntaxError: unexpected indent
>>> del nums[2:]
...      
>>> nums
...      
[25, 77]
>>> 
>>> nums.extend([29,12,14,36])
...      
>>> nums
...      
[25, 77, 29, 12, 14, 36]
>>> 
>>> min(nums)
...      
12
>>> max(nums)
...      
77
>>> sum(nums)
...      
193
>>> nums.sort()
...      
>>> nums
...      
[12, 14, 25, 29, 36, 77]
