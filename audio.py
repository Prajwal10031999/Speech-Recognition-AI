import pyaudio
import wave
import speech_recognition as sr
import subprocess
import webbrowser
import win32com.client as wincl

def echo(text):
    subprocess.call('say ' + text, shell=True)

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()
    
    stream = pa.open(
            format=pa.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True
    )
    
    
    data_stream = wf.readframes(chunk)
    
    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)
        
    stream.close()
    pa.terminate()
    


r = sr.Recognizer()

def initSpeech():
    print("Listening....")
    play_audio("./audio/bubbling-up.wav")
    
    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)
        
    play_audio("./audio/case-closed.wav")
    
    command = ""
    
    try:
        command = r.recognize_google(audio)
    except:
        print("Couldn't get you buddy..")
        
    print("Your command:")
    print(command)
    
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak("okay i will search for " + command)
    webbrowser.open_new(command)
    
    
    
initSpeech()
