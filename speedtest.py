import main
import time

startTime = time.time()

for i in main.search("kimetsu no yaiba"):
    print(i["title"])
print(f"execution time was {time.time()-startTime})")
