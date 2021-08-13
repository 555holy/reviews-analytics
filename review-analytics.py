import random
r = random.randint(0,10000)
data = []
count =0
with open('reviews.txt', 'r') as f:
	for line in f:
		count += 1
		data.append(line)
		if count % 1000 == 0:
			print(len(data))

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('讀取完畢，總共有', len(data), '筆資料')
print('留言平均長度為', sum_len/len(data), '個字')

flit = [d for d in data if 'good' in d] #list comprehension

print('有good的留言有', len(flit), '個')
print(flit[r])
