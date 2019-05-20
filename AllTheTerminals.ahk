togglecmder:=0
togglegitbash:=0
toggle:=0

<^<!t::
if (togglecmder=0){
  Run, cmdermode.vbs
  togglecmder:=!togglecmder
} else {
  Run, killcmder.vbs
  togglecmder:=!togglecmder
}
Return

<^<!c::
if (toggle=0){
  Run, cmd /k start_winguake.bat
  toggle:=!toggle
} else {
  Run, kill.vbs
  toggle:=!toggle
}
Return

<^<!b::
if (togglegitbash=0){
  Run, gitbashmode.vbs
  togglegitbash:=!togglegitbash
} else {
  Run, killgitbash.vbs
  togglegitbash:=!togglegitbash
}
Return
