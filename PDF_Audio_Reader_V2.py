import PyPDF2, pyttsx3
from PySide2 import QtWidgets, QtGui, QtCore #核心, 標籤, 文字排版

a = 0
b = 0
file_path:str = ''
voice_dict = {'Female-01 (Accent: Taiwanese)': 'F_CH',
              'Female-02 (Accent: American)': 'F_EN',
              'Male-01 (Accent: American)': 'M_EN'}
total_pages = 0

'''
fundamental
'''
app = QtWidgets.QApplication()
my_widget = QtWidgets.QWidget()
my_widget.setWindowIcon(QtGui.QIcon('icon2.png'))
my_widget.setWindowTitle('PDF Audio Reader')
my_widget.setGeometry(300, 300, 1000, 300)


'''
labels
'''
my_label = QtWidgets.QLabel('        Your Best PDF Audio Reader')
my_label.setParent(my_widget)

my_font = QtGui.QFont('Calibri', 16, QtGui.QFont.Bold)  # title label
my_font2 = QtGui.QFont('Calibri', 10, QtGui.QFont.Thin) #file path label
my_font3 = QtGui.QFont('Calibri', 8, QtGui.QFont.Thin) #Voice choice label
my_font4 = QtGui.QFont('Calibri', 12, QtGui.QFont.Bold)
my_label.setFont(my_font)
my_label.setGeometry(0, 0, 1000, 50)
my_label.setStyleSheet('background-color:#D2EDF9 ;color: #1764BB')


file_path = ' no file selected'
my_label2 = QtWidgets.QLabel(file_path)
my_label2.setParent(my_widget)
my_label2.setFont(my_font2)
my_label2.setGeometry(150, 75, 650, 30)
my_label2.setStyleSheet('background-color:#D2EDF9 ;color: #868686')

my_label3 = QtWidgets.QLabel(' (Only English supported)')
my_label3.setParent(my_widget)
my_label3.setFont(my_font3)
my_label3.setGeometry(460, 140, 400, 30)
my_label3.setStyleSheet('color:black')

total_pages = 0
my_label4 = QtWidgets.QLabel(' File Total Pages: [ '+ str(total_pages)+' ]')
my_label4.setParent(my_widget)
my_label4.setFont(my_font2)
my_label4.setGeometry(50, 160, 300, 100)
my_label4.setStyleSheet('color:black')


my_label5 = QtWidgets.QLabel(' Read The Following Page(s): ')
my_label5.setParent(my_widget)
my_label5.setFont(my_font2)
my_label5.setGeometry(300, 160, 300, 100)
my_label5.setStyleSheet('color:black')


my_label6 = QtWidgets.QLabel('The App Is Compatible With Windows 10 Only ! ')
my_label6.setParent(my_widget)
my_label6.setFont(my_font3)
my_label6.setGeometry(670, 260, 400, 30)
my_label6.setStyleSheet('color:grey')

# 輸入框
user_input = QtWidgets.QLineEdit()
user_input.setParent(my_widget)
user_input.show()
user_input.setGeometry(550, 195, 250, 30)
#設定提示文字
user_input.setPlaceholderText('Start/End')
user_input.setFont(my_font2)



'''
triggers
'''

def get_file_path():
    global file_path, my_label4

    file_path = FileDialog.getOpenFileName(my_widget, "Select PDF file")
    short_path = ''
    if len(file_path[0])>50:
        short_path = file_path[0][0:30] + '.../' + file_path[0].split('/')[-1]
    else:
        short_path = file_path
    my_label2.setText(short_path)
    file_path = file_path[0]

    pre_reader = PyPDF2.PdfFileReader(open(file_path, 'rb'))
    total_pages:int = pre_reader.numPages
    my_label4.setText(' File Total Pages: [ '+ str(total_pages)+' ]')

    #print(total_pages)




my_box = QtWidgets.QComboBox()
def get_voice_selection():
    selected_voice = my_box.currentText().strip()
    # print(voice_dict[selected_voice])
    return voice_dict[selected_voice]


def get_selected_pages():
    if user_input.text().isdigit():
        a = b = user_input.text()
        a, b = int(a), int(b)
        # if a > total_pages:
        #     my_label__.setText()
    else:
        a, b = user_input.text().split('/')
        a, b = int(a), int(b)
    return a, b

def READ():
    from pdfreader_V3 import PDFreader
    a, b = get_selected_pages()
    PDFreader(get_voice_selection(), file_path, a, b)
    print(get_voice_selection(), file_path, a, b)

'''
button GUI
'''
file_dialog_but = QtWidgets.QPushButton('File Path')
file_dialog_but.setFont(my_font2)
file_dialog_but.setParent(my_widget)
file_dialog_but.setGeometry(50, 75, 85, 30)
FileDialog = QtWidgets.QFileDialog(my_widget)
file_dialog_but.clicked.connect(get_file_path)

# run but

run_but = QtWidgets.QPushButton()
pixmap = QtGui.QPixmap("icon3.png")
button_icon = QtGui.QIcon(pixmap)
run_but.setIcon(button_icon)
run_but.setIconSize(QtCore.QSize(148, 148))
run_but.setParent(my_widget)
run_but.setGeometry(820, 73, 156, 156)
run_but.clicked.connect(get_selected_pages)
run_but.clicked.connect(get_voice_selection)
run_but.clicked.connect(READ)
# run_but.show()

'''
combobox
'''
my_box.addItems([' Female-01 (Accent: Taiwanese)', ' Female-02 (Accent: American)', ' Male-01 (Accent: American)'])
my_box.setFont(my_font2)
my_box.setParent(my_widget)
my_box.setGeometry(50, 135, 400, 30)
#my_box.show()


my_widget.show()
app.exec_()