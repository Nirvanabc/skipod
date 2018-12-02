f_in = open("result.txt")
f_out = open("prepared_data.txt", "w")

line = f_in.readline()
while line != '':
    if len(line) < 10:
        line = f_in.readline()
        continue
    print(line)
    _, thr, _, m_size, _, time = line.split()
    f_out.write(thr + " " + m_size + " " + time + "\n")
    line = f_in.readline()
f_in.close()
f_out.close()
