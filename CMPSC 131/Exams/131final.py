def time_converter(time):
        
    if time[:2] == "00":
        hour = "12"
    elif int(time[:2]) < 13:
        hour = str(int(time[:2]))       
    else:
        hour = str(int(time[:2])-12)

    part = ' a.m.' if int(time[:2]) < 12 else ' p.m.'    
    time = hour + ":" + time[3:] + part

    return time

time = "13:46"
newTime = time_converter(time)
print(newTime)