def is_prime(n):
  cont = 0
  for i in range(1,n+1):
    if (n % i) == 0:
      cont += 1
  if cont == 2:
    return True
  else:
    return False

n = 100000000

for i in range(1,n+1):
  if(is_prime(i)):
    print(i)