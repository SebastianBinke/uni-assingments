def phi(n: int) -> int:
   if n <= 0:
      raise ValueError("Zahl größer 0")
   result = n
   p = 2
   while p * p <= n:
      if n % p == 0:
         while n % p == 0:
            n //= p
         result -= result // p
      p += 1 if p == 2 else 2
   if n > 1:
      result -= result // n
   return result

#testcase für debugging
value = 85
result = phi(value) #erwarte 64
print(result) 