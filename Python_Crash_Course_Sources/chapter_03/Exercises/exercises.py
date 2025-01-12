names=['Premi','Prabha','Deepthi']
print(names[0])
print(names[1])
print(names[2])

print(f'The name of my friend is {names[0]}')
print(f'The name of my friend is {names[1]}')
print(f'The name of my friend is {names[2]}')

mybucketlist=['Paris','Dubai','switzerland']
print(f'I would like to visit {mybucketlist[0]} with my husband and I would like to visit {mybucketlist[1]} with my parents.Finally, I would like to visit {mybucketlist[2]} with my parents,in-laws and my husband. ')


Guest_list=['Premi','Prabha','Deepthi']
print(f'Hi {Guest_list[0]}, {Guest_list[1]} and {Guest_list[2]}, I would like to invite you for dinner at my place on 13th of January 2025')
print(Guest_list.pop(0))
Guest_list.insert(0,'RV')
print(f'Hi {Guest_list[0]}, {Guest_list[1]} and {Guest_list[2]}, I would like to invite you for dinner at my place on 13th of January 2025')

print('Hi all, I have found a bigger dinner table and I would like to invite more guests. I will be inviting 3 more guests and will send a revised invitation soon')
Guest_list.insert(0,'Advaith')
Guest_list.insert(2,'Adi')
Guest_list.append('Maggi')
print(f'Hi {Guest_list[0]}, {Guest_list[1]}, {Guest_list[2]}, {Guest_list[3]}, {Guest_list[4]} and {Guest_list[5]}, I would like to invite you for dinner at my place on 13th of January 2025')

print('I am sorry to inform you that I can invite only 2 guests for dinner as the table will not be delivered on time.')
Removed_guest=Guest_list.pop()
print(f'Sorry {Removed_guest}, I will not be able to invite you for dinner')
Removed_guest=Guest_list.pop()
print(f'Sorry {Removed_guest}, I will not be able to invite you for dinner')
Removed_guest=Guest_list.pop()
print(f'Sorry {Removed_guest}, I will not be able to invite you for dinner')
Removed_guest=Guest_list.pop()
print(f'Sorry {Removed_guest}, I will not be able to invite you for dinner')
print(f'I am happy to inform you that {Guest_list[0]} and {Guest_list[1]} are still invited for dinner')
del Guest_list[0]
del Guest_list[0]
print(Guest_list)

travel_bucketlist=['Paris','Dubai','switzerland','New York','London']
print(travel_bucketlist)
print(sorted(travel_bucketlist))
print(travel_bucketlist)
print(sorted(travel_bucketlist,reverse=True))
print(travel_bucketlist)
travel_bucketlist.reverse()
print(travel_bucketlist)
travel_bucketlist.reverse()
print(travel_bucketlist)
travel_bucketlist.sort()
print(travel_bucketlist)
travel_bucketlist.sort(reverse=True)
print(travel_bucketlist)

print(len(travel_bucketlist))