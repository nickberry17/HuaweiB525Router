import huawei_lte.router as lte
import huawei_lte.xmlobjects as xmlobjects
from huawei_lte.errors import RouterError

import PySimpleGUI as sg      

# Very basic window.  Return values as a list      

layout = [      
            [sg.Text('Please enter your Name, Address, Phone')],      
            [sg.Text('Name', size=(15, 1)), sg.InputText('name')],      
            [sg.Text('Address', size=(15, 1)), sg.InputText('address')],      
            [sg.Text('Phone', size=(15, 1)), sg.InputText('phone')],      
            [sg.Submit(), sg.Cancel()]      
            ]      

window = sg.Window('Simple data entry window').Layout(layout)         
button, values = window.Read() 

print(button, values[0], values[1], values[2])

def lockBands():
        #Connect to the router
        router = lte.B525Router('192.168.8.1')
        router.login(username='admin', password='opHD7kKS')

        #Get a list of what API calls appear to be are supported (GET requests only)
        #response = router.features

        #response = router.net.mode #Current supported 2G/3G/4G mode and bands
        #response = router.net.modelist #Expanded list of supported bands, contains non-XML value lists
        # response = router.net.modelist2 #CUSTOM: Provides an XML format friendly expanded list

        response = router.net.set_lte_band({'bands': ['B40', 'B28', 'B7', 'B1', 'B3', 'B8']})
        #response = router.net.set_lte_band({'bands': ['B40']})
        #response = router.net.set_lte_band({'bands': ['B40', 'B7', 'B3']})
        # response = router.net.set_network_band({'bands': ['W2100', 'GSM900', 'W850', 'GSM1800', 'GSM850', 'GSM1900', 'W1900', 'W900']})

        print(response)
        #Logout
        router.logout() #Throws RouterError on a logout error
