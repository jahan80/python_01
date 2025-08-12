list_t =  [1,2,2,2,3,3]

set_t={1,2,2,2,3,3}  # set detected unic val

print(list_t,set_t)

set_t2=set(list_t )
print(list_t,set_t,set_t2)


set_t2.add(3) # if val 3 exist not add  else add

print(set_t | set_t2) # demorgan '|,&,-,^'

dict_t = {'key1':'value1','key2':'value2'}
print(dict_t['key1'])
print(dict_t.get('key1'))
print(dict_t.get('val')) # if val exist print val  else print None
