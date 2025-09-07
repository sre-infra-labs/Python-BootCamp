def foo(a,b,*args,**kwargs):
  print(a,b)
  
  for num in args:
    print(f'args {num}')
  
  for key in kwargs:
    print(f"kwargs['{key}'] = {kwargs[key]}")

# all arguments
foo(1,2,3,4,5,6,seven=7,eight=8)

# No args
foo(1,2,seven=7,eight=8)

# No kwargs
foo(1,2,3,4,5,6)
