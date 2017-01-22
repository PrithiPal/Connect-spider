import getopt
import os
import sys



#start accepting arguments
user = ''
passw = ''

options, args = getopt.getopt(sys.argv[1:],'u:p:',['username=','password='])

for opt,arg in options :
    if opt in ('-u','--username') :
        user = str(arg)
    elif opt in ('-p','--password') :
        passw = str(arg)

print("USER: ",str(user))
print("PASSW: ",str(passw))

next_command = 'scrapy crawl connect_spider -a username=' + str(user) + ' -a password=' + str(passw)
os.system(next_command)
