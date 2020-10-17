import PyPDF2, pyttsx3
from PySide2 import QtWidgets, QtGui, QtCore #核心, 標籤, 文字排版

a = 0
b = 0
voice_exe = ''
file_path:str = ''
voice_dict = {'Female-01 (Accent: Taiwanese)': 'F_CH',
              'Female-02 (Accent: American)': 'F_EN',
              'Male-01 (Accent: American)': 'M_EN'}

'''
底層區
'''
#創建QtApp的核心, 實體化/實例化一個APP
app = QtWidgets.QApplication()
#創立視窗(創建一個空的畫布)
my_widget = QtWidgets.QWidget()
my_widget.setWindowIcon(QtGui.QIcon('./DATA/icon2.png'))
#改title
my_widget.setWindowTitle('PDF Audio Reader')
my_widget.setGeometry(300, 300, 900, 450)


'''
標籤區
'''
#創建元件
my_label = QtWidgets.QLabel(' Your Best PDF Audio Reader')
my_label.setParent(my_widget)

#創建字體物件
my_font = QtGui.QFont('Calibri', 16, QtGui.QFont.Bold)  # title label
my_font2 = QtGui.QFont('Calibri', 10, QtGui.QFont.Thin) #file path label
my_font3 = QtGui.QFont('Calibri', 8, QtGui.QFont.Thin) #Voice choice label
my_font4 = QtGui.QFont('Calibri', 12, QtGui.QFont.Bold)
#my_font.setPointSize(20) #pixel

#把字體附加到my_label
my_label.setFont(my_font) # ->切字, ->resize label或者使用Geometry
my_label.setGeometry(100, 0, 900, 50)
my_label.setStyleSheet('background-color:#D2EDF9 ;color: #1764BB')


file_path = ' no file selected'
my_label2 = QtWidgets.QLabel(file_path)
my_label2.setParent(my_widget)
my_label2.setFont(my_font2)
my_label2.setGeometry(200, 100, 650, 30)
my_label2.setStyleSheet('background-color:#D2EDF9 ;color: #868686')

my_label3 = QtWidgets.QLabel(' Only English supported for the current version')
my_label3.setParent(my_widget)
my_label3.setFont(my_font3)
my_label3.setGeometry(100, 180, 400, 30)
my_label3.setStyleSheet('color:black')

total_pages = 0
my_label4 = QtWidgets.QLabel(' File Total Pages: '+ str(total_pages)+'\n\n Read The Following Page(s): ')
my_label4.setParent(my_widget)
my_label4.setFont(my_font2)
my_label4.setGeometry(100, 220, 400, 100)
my_label4.setStyleSheet('color:black')

# 輸入框
user_input = QtWidgets.QLineEdit()
user_input.setParent(my_widget)
user_input.show()
user_input.setGeometry(100, 320, 300, 30)
#設定提示文字
user_input.setPlaceholderText('Start/End')
user_input.setFont(my_font2)

my_label.show()
my_label2.show()
my_label3.show()
my_label4.show()
user_input.show()


'''
triggers
'''

def get_file_path():
    global file_path
    file_path = FileDialog.getOpenFileName(my_widget, "Select PDF file")
    short_path = ''
    if len(file_path[0])>50:
        short_path = file_path[0][0:30] + '.../' + file_path[0].split('/')[-1]
    else:
        short_path = file_path
    my_label2.setText(short_path)

    file_path = file_path[0]


my_box = QtWidgets.QComboBox()
def get_voice_selection():
    selected_voice = my_box.currentText().strip()
    print(voice_dict[selected_voice])
    return voice_dict[selected_voice]


def get_selected_pages():
    # 拿到輸入框的文字
    a, b = user_input.text().split('/')
    a, b = int(a), int(b)
    print(a, b)
    print(type(a))
    return a , b

def READ():
    from pdfreader_V2 import PDFreader
    a, b = get_selected_pages()
    PDFreader(get_voice_selection(), file_path, a, b)
    print(get_voice_selection(), file_path, a, b)


'''
button GUI
'''
file_dialog_but = QtWidgets.QPushButton('File Path')
file_dialog_but.setFont(my_font2)
file_dialog_but.setParent(my_widget)
file_dialog_but.setGeometry(100, 100, 85, 30)
FileDialog = QtWidgets.QFileDialog(my_widget)
file_dialog_but.clicked.connect(get_file_path)

# run but


run_but = QtWidgets.QPushButton('READ')
run_but.setParent(my_widget)
run_but.setGeometry(750, 300, 100, 60)
run_but.setFont(my_font2)
run_but.clicked.connect(get_selected_pages)
run_but.clicked.connect(get_voice_selection)

run_but.clicked.connect(READ)
#run_but.clicked.connect(READ)




'''
combobox zone
'''

#批量增加選項
my_box.addItems([' Female-01 (Accent: Taiwanese)', ' Female-02 (Accent: American)', ' Male-01 (Accent: American)'])
#增加單一選項
my_box.setFont(my_font2)
my_box.setParent(my_widget)
my_box.setGeometry(100, 150, 500, 30)
my_box.show()










'''===============================================
功能區  開始
================================================='''




'''===============================================
功能區 結束
================================================='''


'''

'''

my_widget.show()














#執行app
app.exec_()