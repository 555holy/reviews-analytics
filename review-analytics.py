import random
r = random.randint(0,10000)
data = []
count = 0
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

wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] > 100000:
		print(word, wc[word])

while True:
	word = input('請問你要查甚麼字？')
	if word == 'q':
		break
	if word in wc:
		print(word,'出現', wc[word],'次')
	else:
		print('沒有這個字喔')
print('感謝使用！')