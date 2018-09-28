#Import modules for the program
import urllib.request
import subprocess
import time

print("Please be aware that as of recently iNeal has cut off 32bit devices on the API so this program is now 64bit only")

#Set the version for comparison (Change if you want but it auto updates)
set_version = ('11.2.6')

#Ask user for their device information
device = input("What is your device identifier? (eg. iPhone10,6) ")
ecid = input("What is your ECID? ")

#Start a while loop
while True:
    #Contact iNeal's API and split to get latest signed version
    url = 'http://api.ineal.me/tss/%s/includebeta' % (device)
    request_text = urllib.request.urlopen(url)
    returned_values = request_text.read()
    current_firmware = returned_values.decode('utf-8')
    current_signed_version = current_firmware.split('"')[31]

    #Start another loop for saving the blobs
    while True:
        #Save blobs if the current signed version is higher than latest
        if current_signed_version > set_version:
            print("A new firmware is signed!")
            
            subprocess.call(['tsschecker_windows.exe', '-d', device, '-l', '-e', ecid, '-s'])
            
            set_version = current_signed_version

            break
        else:
            #If the latest version is 11.2.5 then print this repeatedly
            print("Latest is", current_signed_version)
            #This is here to stop us accidentally DoSing iNeal
            time.sleep(4)
