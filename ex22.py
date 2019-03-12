from sys import argv
from os.path import exists

script, from_file, to_file = argv

def write_into_file(*args):
    arg1, arg2, arg3, arg4 = args
    
    print """
    Read file: %r\n
    Write file: %r\n 
    SAMPLE RANI%r\n
    OG KANI: %r""" % (arg1, arg2, arg3, arg4)
    in_file = open(arg1)
    indata = in_file.read()
    print "The input file is %d bytes long" % len(indata)

    print "Before Write: \n%s \n" % open(arg2).read()
    out_file = open(arg2, 'w')    
    out_file.write(indata)    
    in_file.close()
    out_file.close()
    print "After Write: \n%s \n" % open(arg2).read()

    print "Alright, all done."    

write_into_file(from_file,to_file,"","")
