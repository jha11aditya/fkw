import sys
import os

targ_ext = "html,js,htm,xml"
domain_url = sys.argv[1]
dname = domain_url.split("://")[1]

stream = os.popen("ls")
flist = stream.read().strip().split()
# print(flist)
if dname not in flist:
    stream = os.popen( '  wget -A ' + targ_ext + ' --recursive --html-extension --page-requisites --convert-links --no-parent  ' + domain_url )
    out = stream.read()
    print(out)


print("##############################################################")

while True:
    print("Enter keyword to search,\nEnter \\q for close,\nEnter \\d\\q for delete&close")
    inp = str(input("enter: "))

    if str(inp) == "\d\q":
        stream = os.popen("rm -rf " + dname )
        print(stream.read())
        break
    elif str(inp) == "\q":
        break
    else:    
        stream = os.popen('grep --color=always -nR "' + inp + '" ' + dname)
        print(stream.read())


# print(dname)