MOD = 10**9 + 7

def pow_mod(n, k, mod):
  if k == 0:
    return 1
  if k % 2 == 1:
    return (n * pow_mod(n, k-1, mod)) % mod
  else:
    r = pow_mod(n, k // 2, mod)
    return (r * r) % mod

def mod_inverse(n, mod):
  return pow_mod(n, mod - 2, mod)

def fact_mod(n, mod):
  res = 1
  for i in range(2, n+1):
    res = (res * i) % mod
  return res

def choose_mod(n, k, mod):
  return (fact_mod(n, mod) * mod_inverse(fact_mod(k, mod), mod) * mod_inverse(fact_mod(n - k, mod), mod)) % mod 

if __name__ == '__main__':
  n, m = map(int, input().split())
  print(choose_mod(n + 2*m - 1, 2*m, MOD))
