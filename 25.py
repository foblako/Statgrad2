from fnmatch import *

for i in range(0,10**9, 3123):
    if fnmatch(str(i), "12*63?5?"):
        print(i)

# 12363957
# 120663351
# 120963159
# 124763850
# 125063658
