import time

def get_speed():
	# count speed per minute by dividing two values
	first_val = input("Value on start: ")
	print("Wait for one minute...")
	time.sleep(60)
	sec_val = input("Value on finish: ")
	start = int(first_val)
	finish = int(sec_val)
	result = finish - start
	# per minute
	print("Your speed is %s Mb/minute" % round(result, 2))

# speed is 20 Mb/minute

def how_long(already, speed=20, filesize=938):
	# get the speed and see how long it will take to download a file of 
	# given size
	already = int(already)
	res_time = (int(filesize) - already)/int(speed)
	message = "You will have to wait %s minutes till the file of %s Mb in size "
	message += "downloads at %s Mb/min speed"
	print(message % (round(res_time, 4), filesize, speed))

while True:
	print("\n\n\n")
	total = 938
	current = input("What does it look like now: > ")
	counted = (int(current)/total)*100

	message = "It means you're at %s %% now!" % round(counted, 2)
	print("\t" + "-" * len(message))
	print("\t" + message)
	print("\t" + "-" * len(message))

	decision = input("Next:\n\tN - exit\n\tO - get current speed\n\tW - how long will you wait\n\tY - continue\n\nMade up your mind? > ")
	if decision == 'N':
		break
	if decision == 'O':
		get_speed()
	if decision == 'W':
		already_downloaded = input("Already downloaded: ")
		first_parameter = input("Current speed: ")
		second_parameter = input("Total filesize: ")
		how_long(already_downloaded, first_parameter, second_parameter)
	else:
		continue