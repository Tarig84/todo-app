import PySimpleGUI as sg

label1 = sg.Txt("Select files to compress")
input1 = sg.InputText(tooltip="files to compress")
choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Txt("Select destination folder")
input2 = sg.InputText(tooltip="destination folder")
choose_button2 = sg.FolderBrowse("Choose")

button3 = sg.Button("Compress")

window = sg.Window("Compressor Program",
                   layout=[[label1, input1, choose_button1], [label2, input2, choose_button2],
                           [button3]])
window.read()
window.close()