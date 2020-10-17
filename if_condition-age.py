age = int(input('how old r u: ')) 
#casting型別轉換 把age從字串轉成整數

if 7 <= age < 13:
	print ('國小最開心')
elif 13 <= age < 16:
	print ('國中最好開始培養興趣與閱讀能力')
elif 16 <= age < 19:
	print ('高中這三年好好拼，未來就能自己決定')
elif 19 <= age < 22:
	if age < 20:
		print ('還不能投總統，但也可以關心國家大事了')
	elif age >= 20:
		print ('要好好投票，別浪費民主賦予的權利')
else:
	print ('不管還有沒有在讀書，都要開始有面對社會競爭力的準備！')