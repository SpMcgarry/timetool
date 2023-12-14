#timetool experimenting without the time related python libraries to see what i can figure out that might work. started with trying to figure a calandar relating multiple simezones
#I understand there is a library for this but trying to see what i can get without it.
def timenow():

    hourInput = input("hours")
    hours = hourInput
    minutesInput = input("minutes")
    minutes = minutesInput
    secondsInput = input("seconds")
    seconds = secondsInput
    inputTime = [hours + ":" + minutes +":"+ seconds]
    nytime = (inputTime)
    if nytime:
        califtime = nytime - nytime[3,0 ,0]
        londontime = nytime + nytime[5, 0, 0]
    return nytime , califtime , londontime

nye = timenow()



print(nye)


def timetool(hours, minutes, seconds):
    seconds = []
    for i in range(1, 60):
        seconds.append(i)

    minutes = []
    for i in range(1, 60):
        minutes.append(i)

    hours = []

    for i in range(1, 24):
        if i in range(1, 12):
            hours.append(i)
        print(hours + ": " + minutes + ": " + seconds + ": " + "AM")

        if i in range(13, 24):
            hours.append(i)
        print(hours + ": " + minutes + ": " + seconds + ": " + "PM")

testtime = timetool(nye)