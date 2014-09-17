def factors(n):
  ret = []
  div = 2
  while(n >= 2):
    if(n%div == 0):
      ret += [div]
      n = n/div
      div = 2
    else:
      div += 1

  return ret