def get_key(obj, key):
    for k, v in obj.items():
        #print(k,v)
        if (k != key) & isinstance(v, dict):  
            get_key(v, key)
        elif k == key:
            print(v) 
            break
        else:
            continue
            

def test():
    s = {'q': 1, 'b': {'c': 3, 'd':4}, 'e': 5}
    get_key(s, 'b')
    s = {
    'Keepers':{'Loris Karius':1,'Simon Mignolet':2,'Alex Manninger':3},
    'Defenders':{'Nathaniel Clyne':3,'Dejan Lovren':4,'Joel Matip':5,'Alberto Moreno':6,'Ragnar Klavan':7,'Joe Gomez':8,'Mamadou Sakho':9}
    }
    get_key(s, 'Joel Matip')

if __name__ == '__main__':
    test()
    
