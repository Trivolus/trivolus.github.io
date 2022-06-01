avail = ['lettuce','tomatoes','celery','onions','spinach','broccoli']
unavail = ['carrots', 'zucchini']

print('Our available items are:')
print(avail)
print('Our unavailable items are:')
print(unavail)

takeprod = (input('Select which products you would like to take...'))
avail.remove(takeprod)
unavail.append(takeprod)
#input('Would you like another product?') - yes or no, if yes repeat lines 9-11

print('Our available items are:')
print(avail)
print('Our unavailable items are:')
print(unavail)

addprod = (input('Please select which product you would like to contribute back to the store...'))
unavail.remove(addprod)
avail.append(addprod)
#input('Would you like to add another product?') - yes or no, if yes repeat lines 18-21

print('Our available items are:')
print(avail)
print('Our unavailable items are:')
print(unavail)

new_produce ='artichoke;squash;potatoes;cabbage'
temp_stored_prod =  new_produce.split(';')
# = new_produce.replace(';',',')
print('Here are the new produce items we received:')
print(temp_stored_prod)
print('Here is our new available produce list:')
avail.extend(temp_stored_prod)
print(avail)