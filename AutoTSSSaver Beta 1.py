#Import modules for the program
import urllib.request
import subprocess

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
    set_version = ('11.2.5')

    #Start another loop for saving the blobs
    while True:
        #Save blobs if the current signed version is higher than latest
        if current_signed_version > set_version:
            print("A new firmware is signed!")
            
            subprocess.call(['./tsschecker_macos', '-d', device, '-l', '-e', ecid, '-s'])
            
            set_version = current_signed_version

            break
        else:
            #If the latest version is 11.2.5 then print this repeatedly
            print("Latest is", current_signed_version)
