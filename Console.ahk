toggle:=0

<^<!t::
if (toggle=0){
  Run, start Cmder
  toggle:=!toggle
} else {
  Run, kill.vbs
  toggle:=!toggle
}
Return
