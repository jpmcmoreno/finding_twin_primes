def test_fermat(n):
  for i in range (1,n+1):
    if(2**(i-1) % i == 1 % i):
      print(i)