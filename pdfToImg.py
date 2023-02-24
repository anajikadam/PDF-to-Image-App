import sys
import fitz
import PySimpleGUI as sg
from sys import exit
import os, time

sg.theme('GreenTan')

layout = [[sg.Text('PDF to Image Converter')],
          [sg.Text('PDF to Image Converter and All images store in folder or the Exit button')],
          [sg.Button('Go'), sg.Button('Exit')]]

window = sg.Window('PDF to Image Converter', layout, enable_close_attempted_event=True)

while True:
    event, values = window.read()
    print(event, values)
    if ( event == 'Go'):
        fname = sg.popup_get_file('PDF Browser', 'PDF file to open', file_types=(("PDF Files", "*.pdf"),))
        if fname is None:
            sg.popup_timed('Cancelling')
            sg.popup_error('Cancel')
            # sg..popup_cancel('popup_cancel')
            exit(0)
        else:
            print(fname)
            print(os.path.basename( fname )) 
            # sg.popup_error( fname)
            basenameFile = os.path.basename( fname )  # GoogleTrans.pdf
            # print(os.path.dirname( fname ))
            fpath = os.path.dirname( fname )          # C:/Users/user/Desktop/
            fileName = basenameFile.split('.')[0]     # GoogleTrans
            # fileNamewithEx = fname.split('/')[-1]
            # fpath = fname.replace(fileNamewithEx, '')
            # fpath = '/'.join(fname.split('/')[:-1])
            t = time.localtime()
            timestamp = time.strftime('%b%d_%H%M', t)
            folderPath0 = fileName + '_' + timestamp        # GoogleTrans_Dec20_1251
            folderPath = os.path.join(fpath, folderPath0 )  # C:/Users/user/Desktop\GoogleTrans_Dec20_1251
            if not os.path.isdir(folderPath):
                os.mkdir(folderPath)
            # print(folderPath)

            doc = fitz.open(fname)
            i = 0
            l1 = []
            for page in doc:
                i += 1
                pix = page.get_pixmap(dpi=500)
                outputFile = fileName+"_" + str(i) + ".png"
                ofpath = os.path.join(folderPath, outputFile)
                print(ofpath)
                l1.append('{}. {}'.format(i, ofpath))
                pix.save(ofpath)
            strl1 = '\n'.join(l1)
            sg.popup_scrolled(strl1, title="List of Image files", font=('Arial', 10))
            # sg.popup('OK')
            # exit(0)
    if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit') and sg.popup_yes_no('         Do you really want to exit?           ') == 'Yes':
        break
    

window.close()
