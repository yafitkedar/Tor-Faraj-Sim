import os

def run_simulations_all():
    sim_tests = [("350"), ("215"), ("340"), ("220"), ("330"), ("225"), ("320"), ("230"), ("310"), ("235"), ("300"), ("290"), ("280"), 
                 ("240"), ("245"), ("250"), ("255"), ("260"), ("265"), ("270"), ("275"), ("285"), ("295"),
                 ("305"), ("315"), ("325"), ("335"), ("345"), ("355")]

	#fin = open('conf_sleep_front.txt', 'r')
	#start_buf = fin.readlines()
	#fin.close()
    fin = open('conf_all.fds.txt', 'r')
    end_buf = fin.readlines()
    fin.close()
    for test in sim_tests:
        try:
            os.mkdir(test)
        except:
            print("directory already exists")
        #print test
        #file_text = '&HOLE XB= ' + test[1] + ', ' + test[2] + ', 5.0, 5.5, 0.0, ' + test[3] + ' / Open Door in Wall\n' 
        file_text = "&HEAD CHID='Tor Faraj', TITLE='Tor Faraj Rockshelter' /\n&MESH IJK=20,60,40, XB= 0.0, 10.0, 0.0, 30.0, 0.0, 20.0 /\n"
        file_text = file_text + '&TIME T_END=1800. /\n\n&WIND SPEED=5., DIRECTION=' + test + ', Z_0=0.15, L=500. /\n'
        f = open(test + '/conf_file.fds', "w")
		#for l in start_buf:
		#	f.write(l)
        f.write(file_text)
        for l in end_buf:
            f.write(l)
        f.close()
        os.chdir(test)
        print("Now in angle " + test)
		#os.system("../../../../../../Build/gnu_linux_64/fds_gnu_linux_64.exe conf_file.fds")
        os.system("fds_local conf_file.fds")
        os.chdir("../")
    return (file_text)
	
def run_simulations_sleep():
    sim_tests = [("0"), ("5"), ("10"), ("15"), ("20"), ("25"), ("30"), ("35"), ("40"), ("45"), ("50"), ("55"),
                 ("60"), ("65"), ("70"), ("75"), ("80"), ("85"), ("90"), ("95"), ("100"), ("105"), ("110"), ("115"),
                 ("120"), ("125"), ("130"), ("135"), ("140"), ("145"), ("150"), ("155"), ("160"), ("165"), ("170"), ("175"),
                 ("180"), ("185"), ("190"), ("195"), ("200"), ("205"), ("210"), ("215"), ("220"), ("225"), ("230"), ("235"), 
                 ("240"), ("245"), ("250"), ("255"), ("260"), ("265"), ("270"), ("275"), ("280"), ("285"), ("290"), ("295"),
                 ("300"), ("305"), ("310"), ("315"), ("320"), ("325"), ("330"), ("335"), ("340"), ("345"), ("350"), ("355")]

	#fin = open('conf_sleep_front.txt', 'r')
	#start_buf = fin.readlines()
	#fin.close()
    fin = open('conf_middle.fds.txt', 'r')
    end_buf = fin.readlines()
    fin.close()
    for test in sim_tests:
        try:
            os.mkdir(test[0])
        except:
            print("directory already exists")
        #print test
        #file_text = '&HOLE XB= ' + test[1] + ', ' + test[2] + ', 5.0, 5.5, 0.0, ' + test[3] + ' / Open Door in Wall\n' 
        file_text = "&HEAD CHID='Tor Faraj', TITLE='Tor Faraj Rockshelter' /\n&MESH IJK=20,60,40, XB= 0.0, 10.0, 0.0, 30.0, 0.0, 20.0 /\n"
        file_text = file_text + '&TIME T_END=3600. /\n\n&WIND SPEED=5., DIRECTION=' + test[0] + ', Z_0=0.15, L=500. /\n'
        f = open(test[0] + '/conf_file.fds', "w")
		#for l in start_buf:
		#	f.write(l)
        f.write(file_text)
        for l in end_buf:
            f.write(l)
        f.close()
        os.chdir(test[0])
        print("Now in angle " + test[0])
		#os.system("../../../../../../Build/gnu_linux_64/fds_gnu_linux_64.exe conf_file.fds")
        os.system("fds_local conf_file.fds")
        os.chdir("../")
    return (file_text)
