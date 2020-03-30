#calculate elapsed time
import time

input("Press enter to start")
#variable to start stopwatch
startTime=time.time()

input("Press enter to stop ")
#variable to stop stopWatch
endTime=time.time()

#calculate elapsed time
elapsedTime=endTime-startTime
#calculate elapsed time in seconds
inSecond=elapsedTime%60
print("Elapsed time : ",inSecond," second")