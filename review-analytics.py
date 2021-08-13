data = []
count =0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('讀取完畢，總共有', len(data), '筆資料')
print('留言平均長度為', sum_len/len(data), '個字')
