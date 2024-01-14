import PySimpleGUI as sg

label1 = sg.Txt("Enter feet: ")
input1 = sg.InputText(tooltip="feet")

label2 = sg.Txt("Enter inches: ")
input2 = sg.InputText(tooltip="inches")

button = sg.Button("Convert")

window = sg.Window("Convertor",
                   layout=[[label1, input1],
                           [label2, input2], [button]])
window.read()
window.close()
