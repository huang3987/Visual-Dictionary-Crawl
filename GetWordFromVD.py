    #_*_ coding:utf-8 _*_

import re
import codecs
import ConfigParser
import os


local_first_URL = 'H:/visual.merriam-webster.com/plants-gardening/plants/alga/examples-algae.php.htm'

local_current_URL = local_first_URL

local_next_URL = ''


filename = 'profile.ini'

progress = 23
cf=ConfigParser.ConfigParser()

if os.path.exists(filename):
    cf.read(filename)
    if 'mission' not in cf.sections():
        cf.add_section('mission')
    
        
    if 'progress' not in cf.options("mission"):
        cf.set('mission','progress',progress)      
    else:
        progress = cf.getint('mission','progress')

    if 'url' not in cf.options("mission"):
        cf.set('mission','url',local_first_URL) 
    else:
        local_current_URL = cf.get('mission','url')
        local_first_URL = local_current_URL

else:
    cf.add_section('mission')
    cf.set('mission','progress',progress)
    cf.set('mission','url',local_first_URL)

section = progress
page_num = 7*section-6
page_end = 7*section

#print "page_num = " + str(page_num)

while True:

    html_file = codecs.open(local_current_URL,'r','utf-8')

    html_file_text = html_file.read()

    ##print html_file_text

    #print "local_current_URL = " + local_current_URL

    local_current_URL = local_current_URL.split('/')

    local_current_URL.pop()

    ##print "local_current_URL = " + local_current_URL

    

    html_file_text = re.sub(r'\&\#160;', " ", html_file_text, re.S)
    html_file_text = re.sub(r'\&\#\d{4}', "", html_file_text, re.S)
    html_file_text = re.sub(r'\&\#\d{3}', "", html_file_text, re.S)
    
    decker = re.findall(r'index\.php(.*?)</div>', html_file_text, re.S)

    decker01 = re.findall(r'>(.*?)</a>', decker[0], re.S)
    del decker01[0]
    
    subject = decker01[-1]
    subject = re.sub(r':', "", subject, re.S)
    decker_name = str(page_num)+'-'+subject+".dec"
    
    decker02 = "::".join(decker01)
    
    #print "deck = " + decker02
    #print "decker_name=" + decker_name
    
    with open(decker_name, 'w') as decker_file:        
        decker_file.write(decker02)
    
    #we will find out the pciture path below
       
    pic_path = re.findall(r'<div><img src=\"(.*?).jpg', html_file_text, re.S)
    #print '*'*40
    ##print pic_path
    
       
    pic_path_temp = local_current_URL[:]
    
    temp_pic = pic_path[0].split('/')
    
    temp_temp = []
    
    ##print temp
    for n in range(len(temp_pic)):
        if temp_pic[n]=='..':
            pic_path_temp.pop()    
        else :
             temp_temp.append(temp_pic[n])
    
    temp_pic = temp_temp
    temp_pic[-1] = temp_pic[-1] + ".jpg"
    pic_path_temp.extend(temp_pic)
    pic_path = "/".join(pic_path_temp)
    #print pic_path
    
    #print '*'*40
    
    #print "local_current_URL = "
    #print local_current_URL
    
    #we find out the text below

    content = []
    noun = ""
    sentences = re.findall(r'descript(.*?)v>', html_file_text, re.S)
    #print '*'*40
    #print sentences
    for n in range(len(sentences)):
        line = [] 

        #sentence = re.findall(r'h4(.*?)/di', sentences[n], re.S)
        ##print sentence
        sentence = re.sub(r'><', '', sentences[n], re.S)
        #print "1"
        #print sentence
        sentence = re.sub(r'\&\#8217', "'", sentence, re.S)
        #print "2"
        #print sentence
        sentence = ' '.join(sentence.split())
        #print "3"
        #print sentence
        sentence = re.sub(r'> <', '', sentence, re.S)
        #print "4"
        #print sentence
        sentence = re.findall(r'>(.*?)<', sentence, re.S)
        #print "5"
        #print sentence
        if len(sentence)==3:
            del sentence[-1]
            #print "6"
            #print sentence
        #del sentence[0]
        noun = sentence[0]

        line.append(noun)
        line.append(pic_path)
        
        sentence =  ":".join(sentence)

        line.append(sentence)
        line.append(sentence)
        line = '\\'.join(line)
        content.append(line)

        ##print '*'*40

        
    #for n in range(len(content)):
        #print content[n]

      

    with open(str(page_num)+'-'+subject+".txt","wb") as content_file:
        ##print "content ="
        ##print content
        content_file.write("\n".join(content).encode('utf-8'))

    
    content_file = str(page_num)+".txt"
    

    local_next_URL = re.findall(r'href(.*?)>next<',html_file_text)
    #print "local_next_URL = "
    #print local_next_URL
    ##print html_file_text
    #print "URL 1 = " + local_next_URL[0]
    local_next_URL = re.findall(r'=\"(.*?)\"',local_next_URL[0])
    #print "URL 2 =" + local_next_URL[0]
    temp = local_next_URL[0].split('/')
    temp_temp = []
    
    #print "temp = "
    #print temp
    for n in range(len(temp)):
        if temp[n]=='..':
            local_current_URL.pop()    
        else :
             temp_temp.append(temp[n])
    
    temp = temp_temp

    if temp[-1] == "examples-hooves.php.htm":
        temp[-1] = "examples of hooves.php.htm"

    #print "local_current_URL = "
    #print local_current_URL
    
    local_next_URL = local_current_URL

    local_next_URL.extend(temp)

    local_next_URL = "/".join(local_next_URL)
    
    if local_next_URL == local_first_URL:
        break

   

    #print "local_next_URL = " +  local_next_URL
    local_current_URL = local_next_URL

    if page_num == page_end:
        break
    

    page_num = page_num + 1
    
    #print "page_num = " + str(page_num)
    
cf.set('mission','progress',progress+1)
cf.set('mission','URL',local_next_URL)
cf.write(open("profile.ini", "w"))
