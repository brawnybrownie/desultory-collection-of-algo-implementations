
from bs4 import BeautifulSoup
import urllib
import ctypes
import time
## def sendAndNotif(head, link):

def alert(title, text, style):
    ##  Styles:
    ##  0 : OK
    ##  1 : OK | Cancel
    ##  2 : Abort | Retry | Ignore
    ##  3 : Yes | No | Cancel
    ##  4 : Yes | No
    ##  5 : Retry | No 
    ##  6 : Cancel | Try Again | Continue
    ctypes.windll.user32.MessageBoxA(0, text, title, style)

def checkIfReleased():
    url = "https://play.google.com/store/devices/details?id=nexus_9_black_16gb_wifi"
    page = urllib.urlopen(url)
    content = page.read()
    page.close()
    soup = BeautifulSoup(content)
    if not soup.find_all('div','not-available'):
        alert("","Nexus 9 is now available. \n https://play.google.com/store/devices/details?id=nexus_9_black_16gb_wifi ", 0)
    else:
        alert("","Not yet", 0)

while True:
    try:
        checkIfReleased()
    except (IOError):
        alert("" ,"Internet disconnected.", 0)
    time.sleep(21600)
    
