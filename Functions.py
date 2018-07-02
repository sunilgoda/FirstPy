def add(a,b):
    return a + b;
print(add(2,3))

def divide():
    print('=====')

def divide2(ch,n):
    print(ch*n)

divide()
divide2('-',10)

#------------------------

def output(text):
    print(text)
text ='outer'
print('from outer scope:' + text)

output('inner')
print(text)

#------------------------
def count_gc(sequence):
    gc =0
    for base in sequence:
        if base in 'GC': gc+=1.0
        elif base in 'DH': gc+=0.5
    return gc

def gc_content(sequence):
    if not sequence:  # TODO get what this does ? how does null work in python
        print("sequence is empty")
        return 0
    sequence = sequence.upper().replace('-','')
    return 100.0 * count_gc(sequence) /len(sequence)
print(gc_content('actacgcttagag'))
print(gc_content(None))
print(gc_content(''))
#------------------------





