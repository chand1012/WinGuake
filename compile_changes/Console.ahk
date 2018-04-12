toggle:=0

<^<!t::
if (toggle=0){
  Run, cmd /k winguakew.exe
  toggle:=!toggle
} else {
  Run, python kill.pyw
  toggle:=!toggle
}
Return
