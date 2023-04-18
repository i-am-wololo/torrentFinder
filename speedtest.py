import main
import time

startTime = time.time()

for i in main.search("demon slayer" ):
    if i["magnet"][0]["quality"] is None:
        print(i)
print(f"execution time was {time.time()-startTime})")
