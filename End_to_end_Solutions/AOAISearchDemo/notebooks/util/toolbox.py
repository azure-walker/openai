import pandas as pd
import PySimpleGUI as sg

from azure.identity import DefaultAzureCredential
import os

def popup_choice():
    sg.theme('Dark Grey 9')   # Add a touch of color
    options = ["Brandon","Kevin","Charles"]
    # All the stuff inside your window.
    layout = [ 
                [
                    sg.Text(size=(30,5),text='Please ask a questions of your healthcare policies', text_color="Green", font=("Arial",22)), 
                    sg.Listbox(options,select_mode=sg.LISTBOX_SELECT_MODE_SINGLE,size=(80,len(options)), font=("Helvetica",25))
                ],
                [
                    sg.Button('Ok'), sg.Button('Cancel')
                ]
            ]

    # Create the Window
    window = sg.Window('Make your choice', layout)

    # Event Loop to process "events" and get the "values" of the input
    while True:
        event, values = window.read()
        print( f"event={event}" )
        if event is None or event == 'Ok' or event == 'Cancel': # if user closes window or clicks cancel
            break
            
    # close  the window        
    window.close()

    if event == "Cancel":
        print( "You cancelled" )
    else:
        if type(values[0]) is list:
            return values[0][0]
        else:
            return values[0]
        #print('You entered ', values[0])
        #sg.popup( f"You selected {values[0]}" )