try:
  N, M = map(int, raw_input().split(' '))
  a = [map(int, raw_input().split(' ')) for _ in range(N)]
  K = int(raw_input())

  for x in sorted(a, key=lambda x:x[K]):
      print ' '.join(map(str, x))
except Exception as e:
  print(e)