#List comprehension
a = [i for i in range(10) if i % 2 == 0]

print a,'---',type(a) 

seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    seq[i] = '%d: %s' % (i, seq[i])
print seq

def _treatment(pos, element):
    return '%d: %s' % (pos, element)

seq = ['one', 'two', 'three']
seq = [_treatment(i, el) for i, el in enumerate(seq)]
print seq
