script=[]
with open("adjust.ahk",'r') as ahk_script:
    script = ahk_script.readlines()
    print script
with open("adjust.ahk",'w') as ahk_script:    
    script[0] = 'counter = %s\n' % str(100)
    ahk_script.writelines(script)

