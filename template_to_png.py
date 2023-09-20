import sys, getopt
import os
import subprocess

def main(argv):
    opts, args = getopt.getopt(argv,"hp:f:",[])
    for opt, arg in opts:
        if opt == '-h':
            print ('template_to_png.py -p <page num> -f <file>')
            sys.exit()
        elif opt in ("-f"):
            inputfile = arg
        elif opt in ("-p"):
            page_num = arg
    print ('Input file is ', inputfile)
    print ('Page number is ', page_num)
    print ('Starting export...')
    os.mkdir(inputfile[:-4])
    subprocess.run("pdfimages -f " + page_num + " -l " + page_num + " -png ./" + inputfile + " ./" + inputfile[:-4] + "/" + inputfile[:-4], shell=True)
    files = sorted(os.listdir("./" + inputfile[:-4]), reverse=True)
    cmd = "convert "
    for file in files:
        cmd += file + ' '
    cmd += '-append ' + inputfile[:-4] + '_' + 'result.png'
    subprocess.run([cmd],shell=True, cwd="./" + inputfile[:-4])
if __name__ == "__main__":
    main(sys.argv[1:])
