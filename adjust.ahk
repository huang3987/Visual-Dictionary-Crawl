counter = 121
hotkey RButton, dotheloop
Esc::ExitApp
return 

dotheloop:

loop , %counter%														
{
send {tab 14}
Sleep 500
send ^{a}
Sleep 500
send ^{x}
Sleep 500
send {f3}
Sleep 500
send ^{v}
Sleep 500
send {enter}
Sleep 500*3
send {tab 2}
Sleep 500
send ^{a}
Sleep 500
send ^{x}
Sleep 500
send ^{t}
Sleep 500
send {tab 2}
Sleep 500
send {enter}
Sleep 500*20
send +{tab 16}
Sleep 500
send {down}
Sleep 500

}

ExitApp
return 


