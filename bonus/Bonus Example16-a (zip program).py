import PySimpleGUI as sg
import  zip_creator as zip

label1 = sg.Txt("Select files to compress")
input1 = sg.InputText(tooltip="files to compress", key='file')
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Txt("Select destination folder")
input2 = sg.InputText(tooltip="destination folder", key='folder')
choose_button2 = sg.FolderBrowse("Choose", key="folderpass")

label3 = sg.Txt("  Enter  Zip  file  name   ")
input3 = sg.InputText(tooltip="zip name", key='zip')

output = sg.Txt("",key='output', text_color="green")
button4 = sg.Button("Compress")

window = sg.Window("Compressor Program",
                   layout=[[label1, input1, choose_button1], [label2, input2, choose_button2],
                           [label3, input3], [button4, output]])

while True:
    event, value = window.read()
    files = value["files"].split(';')
    folder = value['folderpass']
    zip_name = value['zip']
    match event:
        case "Compress":
            zip.make_archive(zip_name, files, folder)
            window['output'].update("Successful Zipping")
        case sg.WINDOW_CLOSED:
            break


window.close()
