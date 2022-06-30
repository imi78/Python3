from collections import defaultdict

lst = ['luxuriant', 'silly', 'dizzy', 'frightening', 'blink', 'silly', 'enjoy', 'suspend', 'blink', 'reward', 'blink', 'fact', 'debt', 'marble', 'blink', 'yak', 'frightening', 'suspend', 'debt']

dct = defaultdict(str)
for i in lst:
    dct[i] += '*'
  

for k, v in dct.items():
    print(f"{k}| {v}")
