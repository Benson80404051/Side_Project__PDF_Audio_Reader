import PyPDF2, pyttsx3
'''
SECTION 1 
設定語音參數
'''
# 依序為女聲(中英), 女聲(英), 男聲(英)
voice_bank = {
    'F_CH':'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-TW_HANHAN_11.0',
    'F_EN':'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0',
    'M_EN':'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'}

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voice_bank['M_EN'])

# 語速控制
rate = engine.getProperty('rate')
print('rate: ', rate)
engine.setProperty('rate', rate-30)

# 音量控制
volume = engine.getProperty('volume')
print('volume:', volume)
engine.setProperty('volume', volume)

# engine.say('語音合成開始')
# engine.runAndWait()

'''
SECTION 2
讀取PDF, 轉成文字檔
'''
file = open('stories_to_tell_to_children_fi.pdf', 'rb')
file_reader = PyPDF2.PdfFileReader(file)
pages = file_reader.numPages
print(file_reader.numPages)

'''
SECTION 3
打文字檔丟給speaker(engine)
'''

for i in range(200, pages):
    k = file_reader.getPage(i).extractText()
    print(k)

    engine.say(k)
    engine.runAndWait()









# 聲音選擇
voice_bank = {
    'F_CH':'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-TW_HANHAN_11.0',
    'F_EN':'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0',
    'M_EN':'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'}

engine.setProperty('voice', voice_bank['M_EN'])
engine.say('to be or not to be, that is a question')
engine.say('從方法宣告上來看，第一個引數指定的是語音驅動的名稱。')
engine.runAndWait()
