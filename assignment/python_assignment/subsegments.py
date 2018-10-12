s = raw_input("Enter String: ").strip()
try:
  k = int(raw_input("Number of Segments: "))
  if (len(s) % k == 0) :
    i = 0
    while i < len(s):
      a = s[i:i+k]
      seen = set()
      print (''.join([x for x in a if not (x in seen or seen.add(x))]))
      i += k
  else:
    print("K is not factor of length of S")
except Exception as e:
  print(e)