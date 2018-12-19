import numpy as np
f_in = open("prepared_data.txt")
f_out = open("prepared_data_complete.txt", "w")

line = f_in.readline()
while line != '':
    time_list = []
    for i in range(4):
        thr, m_size, time = line.split()
        time_list.append(float(time))
        line = f_in.readline()
    time_avg = np.average(time_list)
    f_out.write(thr + " " + m_size + " " + str(time_avg) + "\n")
f_in.close()
f_out.close()
