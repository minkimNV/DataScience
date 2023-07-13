a, b = map(int, input().strip().split(' '))

for rows in range(b):
	for star in range(a):
		print("*", end="")
        # end="" 는 프린트하고 나면 계속 다음줄로 넘어가서 안넘어가게 하려고
	print() 
 # 한줄에 30개 찍으면 다음줄로 넘어가고 다음 줄 별찍으려고
