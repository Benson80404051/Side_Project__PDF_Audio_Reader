import PyPDF2, pyttsx3

class PDFreader:
    def __init__(self, voice_selection, path, start, end):
        voice_bank = {
            'F_CH': 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-TW_HANHAN_11.0',
            'F_EN': 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0',
            'M_EN': 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'}
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voice_bank[voice_selection])
        self.file = open(path,'rb')
        self.file_reader = PyPDF2.PdfFileReader(self.file)
        self.pages:int = self.file_reader.numPages

        # 語速控制
        self.rate = self.engine.getProperty('rate')
        print('rate: ', self.rate)
        self.engine.setProperty('rate', self.rate - 20)

        for i in range(start, end+1):
            k = self.file_reader.getPage(i).extractText()
            self.engine.say(k)
            self.engine.runAndWait()

if __name__ == '__main__':
    PDFreader('M_EN','stories_to_tell_to_children_fi.pdf', 4, 7)









# 聲音選擇
# voice_bank = {
#     'F_CH':'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-TW_HANHAN_11.0',
#     'F_EN':'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0',
#     'M_EN':'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'}
#
# engine.setProperty('voice', voice_bank['M_EN'])
# engine.say('to be or not to be, that is a question')
# engine.say('從方法宣告上來看，第一個引數指定的是語音驅動的名稱。')
# engine.runAndWait()
