
import PyPDF2
import pyttsx3

engine = pyttsx3.init()
reader = PyPDF2.PdfReader('.pdf')
file = open('doc.docx','w')
for i in range(0,len(reader.pages)):
    page =reader.pages[i]
    text = page.extract_text()
    # engine.say(text)
    engine.save_to_file(text, 'audio.mp3')
    engine.runAndWait()
#Done
