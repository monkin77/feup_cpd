f = open("2.txt", "r")
lines = f.readlines()
gflops = []
sizes = []
times = []

for line in lines:
    parsed = line.split()
    size = int(parsed[0])
    time = float(parsed[2])

    gflop = 2 * (size**3) / time

    gflops.append(gflop)
    sizes.append(size)
    times.append(time)

w = open("out.txt", "w")
for i in range(len(gflops)):
    w.write(str(sizes[i]) + " - " + str(times[i]) + " - " + str(gflops[i]) + "\n")

f.close()
w.close()
