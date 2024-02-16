a = b = c = 10**18
for(
   if(x[i] < c):
      c = x[i]
   if(c < b) swap(b, c)
   if(b < a) swap(a, b)
   if(b > c) swap(b, c)