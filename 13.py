s = "АВД БАД ВГ ГДЖ ДВЖ ЕДБЖ ЖМКИ ИЕ КМИ ЛГ МЛ"

d = {c[0]: c[1:] for c in s.split()}


def f(s):
    if len(s) > 1 and s[-1] == 'Д': return 1
    else: return sum(f(s + c) for c in d[s[-1]] if c not in s[1:])


print(f("Д"))

# 17
