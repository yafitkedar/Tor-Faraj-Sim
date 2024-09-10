def parse_res(in_file, out_file, row, height):
    fin = open(in_file,"r")
    lines = fin.readlines()
    fin.close()
    fout = open(out_file, "w")
    headers = lines[1].split(",")[1:]
    print(headers[2])
    print(headers[2].split("_")[3])
    for line in lines[2:]:
        f = line.split(",")
        sl = "Time : " + f[0] + "\n"
        fout.write(sl)
        i = 0
        sl = ""
        ind = 0
        for val in f[1:]:
            if (headers[ind].split("_")[3] != height):
                ind = ind + 1
                continue
            ind = ind + 1
            sl = sl + val + ", "
            i = i + 1
            if (i == row):
                i = 0
                sl = sl + "\n" 
                fout.write(sl)
                sl = ""
        fout.write(sl)
        fout.write("\n")
    fout.close()
    
def parser_new(in_file, out_file, time, height):
    fin = open(in_file, "r")
    lines = fin.readlines()
    fin.close()
    fields = lines[1].split(",")
    res = {}
    min_x = 1000
    max_x = 0
    min_y = 1000
    max_y = 0
    for line in lines[2:]:
        f = line.split(",")
        if (float(f[0]) - 5 < time) and (float(f[0]) + 5 > time):
            print("Found the required time line\n")
            for i in range(2, len(f)):
                try:
                    (t, x, y, z) = fields[i].replace("\"", "").split("_")
                except:
                    print(f[i].replace("\"", "").split("_"), i)
                if (int(z) == height):
                    res[(x,y)] = f[i]
                    if (int(x) < min_x):
                        min_x = int(x)
                    if (int(x) > max_x):
                        max_x = int(x)
                    if (int(y) < min_y):
                        min_y = int(y)
                    if (int(y) > max_y):
                        max_y = int(y)
            print(min_x, max_x, min_y, max_y)
    fout = open(out_file, "w")
    sl = ""
    for x in range(min_x, max_x, 5):
        sl = sl + ", " + str(x)
    sl = sl + "\n"
    fout.write(sl)
    for y in range(min_y, max_y, 5):
        sl = str(y)
        for x in range(min_x, max_x, 5):
            try:
                val = res[(str(x),str(y))]
            except:
                val = "0"
            sl  = sl + ", " + val
        sl = sl + "\n"
        fout.write(sl)
    fout.close()
    return(res)
            
            
            