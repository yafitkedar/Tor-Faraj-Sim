def parse_res(in_file, out_file, col, row):
    fin = open(in_file,"r")
    lines = fin.readlines()
    fin.close()
    fout = open(out_file, "w")
    for line in lines[2:]:
        f = line.split(",")
        sl = "Time : " + f[0] + "\n"
        fout.write(sl)
        i = 0
        sl = ""
        for val in f[1:]:
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