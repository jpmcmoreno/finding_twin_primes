def test_lucasian(n):
  for i in range (1,n+1):
    M = (2**i)+1
    if( (3**((M-1)/2))%M == M-1 ):
      print(M)