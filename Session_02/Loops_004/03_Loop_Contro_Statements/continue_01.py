"""
Real life example where a programmer will use continue
When we want to skip a product in e-commerce. We don't want to show those items whose stock is 0.
"""
# In continue we skip the iteration.
for i in range(1,10):
    if i==5:
        continue
    print(i)


