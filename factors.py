def factors(n):
  ret = []
  while(n > 3):
    ret += [2]
    n = n/2
    
  ret += [n]
  return ret