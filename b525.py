import huawei_lte.router as lte
import huawei_lte.xmlobjects as xmlobjects
from huawei_lte.errors import RouterError

from tkinter import *
from tkinter.ttk import *

def lockBands(bands, user, passwd, ip):
        print(bands)
        #Connect to the router
        router = lte.B525Router(ip)
        router.login(username=user, password=passwd)

        #Get a list of what API calls appear to be are supported (GET requests only)
        #response = router.features

#        response = router.net.mode #Current supported 2G/3G/4G mode and bands
        #response = router.net.modelist #Expanded list of supported bands, contains non-XML value lists
        # response = router.net.modelist2 #CUSTOM: Provides an XML format friendly expanded list

        response = router.net.set_lte_band({'bands': bands})
        #response = router.net.set_lte_band({'bands': ['B40']})
        #response = router.net.set_lte_band({'bands': ['B40', 'B7', 'B3']})
        # response = router.net.set_network_band({'bands': ['W2100', 'GSM900', 'W850', 'GSM1800', 'GSM850', 'GSM1900', 'W1900', 'W900']})

        print(response)
        return response
        #Logout
        router.logout() #Throws RouterError on a logout error
############# END lockBands() #####################

window = Tk()

window.title("Huawei B525 Band Locker by Telco Antennas for Optus v0.1")

window.geometry('600x300')
lbl = Label(window, text="Fill out all fields, select required bands and click Lock Bands.")
lbl.grid(column=0, row=0)

lblUser = Label(window, text="Username")
lblUser.grid(column=0, row=1)
enterUser = Entry(window,width=15)
enterUser.grid(column=1, row=1)

lblPasswd = Label(window, text="Password")
lblPasswd.grid(column=0, row=2)
enterPasswd = Entry(window,width=15)
enterPasswd.grid(column=1, row=2)

lblIP = Label(window, text="IP Address")
lblIP.grid(column=0, row=3)
enterIP = Entry(window,width=15)
enterIP.grid(column=1, row=3)


band1 = BooleanVar()
band3 = BooleanVar()
band7 = BooleanVar()
band8 = BooleanVar()
band28 = BooleanVar()
band40 = BooleanVar()

b1 = Checkbutton(window, text='B1', var=band1)
b3 = Checkbutton(window, text='B3', var=band3)
b7 = Checkbutton(window, text='B7', var=band7)
b8 = Checkbutton(window, text='B8', var=band8)
b28 = Checkbutton(window, text='B28', var=band28)
b40 = Checkbutton(window, text='B40', var=band40)

global bands
global user
global passwd
global IP

bands = []

def doLockBands():

    user = enterUser.get()
    passwd = enterPasswd.get()
    ip = enterIP.get()

    if band1.get() == True:
        bands.append(b1.cget("text"))
    if band3.get() == True:
        bands.append(b3.cget("text"))
    if band7.get() == True:
        bands.append(b7.cget("text"))
    if band8.get() == True:
        bands.append(b8.cget("text"))
    if band28.get() == True:
        bands.append(b28.cget("text"))
    if band40.get() == True:
        bands.append(b40.cget("text"))

    if not bands:
        lbl.configure(text="Error: you must select at least one band.")
    else:

        if (lockBands(bands, user, passwd, ip).find("OK")):
            lbl.configure(text="Locked to " + ''.join([str(x + ", ") for x in bands]))
        else:
            lbl.configure(text="Error, please try again")

b1.grid(column=1, row=5)
b3.grid(column=1, row=6)
b7.grid(column=1, row=7)
b8.grid(column=1, row=8)
b28.grid(column=1, row=9)
b40.grid(column=1, row=10)

btn = Button(window, text="Lock Bands", command=doLockBands)
btn.grid(column=1, row=11)

window.mainloop()
