seconds = int(input())
hour = str(seconds // 3600)
minutes = (seconds // 60) % 60
sec = seconds % 60
if minutes < 10:
    minutes = '0' + str(minutes)
else:
    minutes = str(minutes)
if sec < 10:
    sec = '0' + str(sec)
else:
    sec = str(sec)
print(hour + ':' + minutes + ':' + sec)







