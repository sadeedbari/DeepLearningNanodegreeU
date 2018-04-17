import urllib.request

def read_text():
    file = open(r'''C:\Users\sami\Desktop\Udacity\read_from_file_ex.txt''')
    contents_of_file = file.read()
    print(contents_of_file)
    file.close()
'''
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.request.urlopen("www.google.com/"+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Alert!!")
    elif "false" in output:
        print("all good")
    else:
        print("scan error")
'''

read_text()
