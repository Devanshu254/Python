"""
1. split
2. join
3. replace
4. strip -> removes the spaces. End one and first one not the middle one.
"""
print('hi my name is Devanshu'.split())
# ['hi', 'my', 'name', 'is', 'Devanshu']

print('hi my name is Devanshu'.split('is'))
# ['hi my name ', ' Devanshu']

print("-".join(['hi','my','name','is','Devanshu']))
# hi-my-name-is-Devanshu

print('hi my name is nitish'.replace('nitish', 'Devanshu'))
# hi my name is Devanshu

print('Devanshu   '.strip())
# Devanshu