import urllib

def read_text():
    speech = open(r"C:\Users\rosar\Desktop\file.txt")
    contents_of_file = speech.read()
    #print(contents_of_file)
    speech.close()
    get_pirate_speech(contents_of_file)

def get_pirate_speech(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()

read_text()
