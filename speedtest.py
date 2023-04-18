import torrentAggregator
import time

startTime = time.time()

for i in torrentAggregator.search("demon slayer" ):
    print(str(i) + '\n\n')
print(f"execution time was {time.time()-startTime})")
