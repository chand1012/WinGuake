toggle:=0

<^<!t::
if (toggle=0){
  Run, gitbashmode.vbs
  toggle:=!toggle
} else {
  Run, killgitbash.vbs
  toggle:=!toggle
}
Return
