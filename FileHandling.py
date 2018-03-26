wf = open("top_fliers.txt", "w")

with open("flying_circus.txt") as f:
    for line in f:
        line = line.strip()
        arr = line.split(",")
        print (arr[0])
        wf.write(arr[0]+"\n")

wf.close()

