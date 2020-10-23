import operator
import PySimpleGUI as sg
from main import readFile,percentData,subjectCodeDist,subjectPI,totalPI
# ------ Menu Definition ------ #
menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['Help', 'About...'], ]

# ------ Column Definition ------ #
column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('CBSE Result Analysis', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE,background_color="#fff2e5",text_color="#000")],
    [sg.Text('_' * 80,background_color="#FFF",text_color="#000")],
    [sg.Text('Select Result File:', size=(35, 1),background_color="#FFF",text_color="#000")],
    [sg.Text('Result File: ', size=(15, 1), auto_size_text=False, justification='right',background_color="#FFF",text_color="#000"),
     sg.InputText('Select result file',background_color="#fff2e5",text_color="#000",key="result_file_path"), sg.FileBrowse(),sg.Button("Submit", size=(9, 1))],

    [sg.Text('K V BHADARWAH DISTT DODA J&K', size=(52, 1), justification='center', font=("Helvetica", 15), relief=sg.RELIEF_RIDGE,background_color="#fff2e5",text_color="#000")],
    [sg.Text('School Code: ', size=(10, 1), auto_size_text=False, justification='left', background_color="#FFF",font=("Helvetica", 11),
             text_color="#000"),
     sg.Text('145875',size=(40, 1),justification='left', background_color="#FFF",
             text_color="#000",font=("Helvetica", 10)),
     sg.Text('Class: ', size=(10, 1), auto_size_text=False, justification='right', background_color="#FFF",
             font=("Helvetica", 11),
             text_color="#000"),
     sg.Text('X', justification='left', background_color="#FFF",
             text_color="#000", font=("Helvetica", 10))
     ],
    [sg.Text('Total Students: ', size=(12, 1), auto_size_text=False, justification='left', background_color="#FFF",
             font=("Helvetica", 11),
             text_color="#000"),
     sg.Text('41', size=(38, 1), justification='left', background_color="#FFF",
             text_color="#000", font=("Helvetica", 10)),
     sg.Text('Total Pass: ', size=(10, 1), auto_size_text=False, justification='right', background_color="#FFF",
             font=("Helvetica", 11),
             text_color="#000"),
     sg.Text('41', justification='left', background_color="#FFF",
             text_color="#000", font=("Helvetica", 10))
     ],
    [sg.Frame(layout=[
        [sg.Radio('Student Percentage    ', "RADIO1",key="stu_perc", default=True, size=(14, 1), text_color="#000",
                  background_color="#fff2e5"),
        sg.Radio('Top 3 Students     ', "RADIO1",key="top_3", default=True, size=(14, 1), text_color="#000",
                  background_color="#fff2e5"),
         sg.Radio('Absent List', "RADIO1",key="absent_list", size=(12, 1), text_color="#000", background_color="#fff2e5"),
         sg.Radio('Highest PI Subject', "RADIO1",key="high_PI", size=(13, 1), text_color="#000", background_color="#fff2e5"),
         ],
        [sg.Radio('Sub Wise Grades', "RADIO1",key="sub_wise", size=(13, 1), text_color="#000", background_color="#fff2e5")]],
        title='Reports', title_color='#000',font=("Helvetica", 12), background_color="#fff2e5", relief=sg.RELIEF_SUNKEN)],
    [sg.Frame(layout=[
    [sg.Radio('SubjectWise PI     ', "RADIO1",key="sub_wise_PI", default=True, size=(15,1),text_color="#000",background_color="#fff2e5"), sg.Radio('Overall PI', "RADIO1",key="overall_PI", size=(47,1),text_color="#000",background_color="#fff2e5")]], title='Performance Index (PI)',title_color='#000',background_color="#fff2e5", relief=sg.RELIEF_SUNKEN)],
    [sg.Frame(layout=[
    [sg.Text("From", text_color="#000",background_color="#fff2e5"),sg.Input(size=(4,1)),sg.Text("To", text_color="#000",background_color="#fff2e5"),sg.Input(size=(4,1)),sg.Text(size=(50,2),background_color="#fff2e5")]], title='Percentage Range',title_color='#000',background_color="#fff2e5", relief=sg.RELIEF_SUNKEN)],

    [sg.Button("Generate", size=(15, 1)),sg.Text(size=(37,1),background_color="#FFF"),sg.Button("Export to excel", size=(15, 1))],
    [sg.Output(size=(80,10))],
    [sg.Exit(button_color=("white", "red"),size=(15, 1))]
]


window = sg.Window('CBSE Result Analysis', layout,background_color="#FFFFFF", default_element_size=(40, 1), grab_anywhere=False)
check = False

while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    try:
        if event == 'Submit':
            if values['result_file_path'] == "Select result file":
                print("Please select result file path")
            else:
                #print(values['result_file_path'])
                path = values['result_file_path']
                readFile(path)
                check = True
                #print(values)
        elif event == 'Generate' and check:
                if values['top_3']:
                    print("Top 3 students\n")
                    print('{:20s} {:20s} {:40s}'.format("Roll No.", "Name","Percentage"))
                    for x in range(3):
                        print('{:20s} {:20s} {:40s}'.format(percentData[x]['rollNo'],percentData[x]['name'],percentData[x]['percentage']))
                elif values['sub_wise']:
                    for key, value in subjectCodeDist.items():
                        print(str(key) + "     A1 = " + str(value['A1']) + " A2 = " + str(
                            value['A2']) + " B1 = " + str(value['B1']) + " B2 = " + str(
                            value['B2']) + " C1 = " + str(value['C1']) + " C2 = " + str(
                            value['C2']) + " D1 = " + str(value['D1']) + " D2 = " + str(
                            value['D2']) + " E = " + str(value['E']) +"\n")
                elif values['stu_perc']:
                    print('{:20s} {:20s} {:40s}'.format("Roll No.", "Name","Percentage"))
                    for x in percentData:
                        print('{:20s} {:20s} {:40s}'.format(x['rollNo'],x['name'],x['percentage']))
                elif values['high_PI']:
                    sub_code = max(subjectPI.items(), key=operator.itemgetter(1))[0]
                    print(sub_code,"       ",round(float(subjectPI[sub_code])))
                elif values['sub_wise_PI']:
                    print('{:20s} {:20s}'.format("Subject Code", "PI"))
                    for x in subjectPI:
                        print(x,"                    ",round(float(subjectPI[x])))
                elif values['overall_PI']:
                        print('{:20s} {:20s}'.format("Overall PI","       ", totalPI[0]))

        else:
            sg.popup("Please select a result file", title="Error Occured")
    except Exception as e:
        print(e)

window.close()
