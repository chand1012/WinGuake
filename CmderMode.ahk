toggle:=0

<^<!t::
if (toggle=0){
  Run, cmdermode.vbs
  toggle:=!toggle
} else {
  Run, kill.vbs
  toggle:=!toggle
}
Return
