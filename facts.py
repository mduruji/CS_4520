def facts(x):
    if x == 0: return 1
    else: return x * facts(x-1)

print(facts(3))