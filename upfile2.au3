;ControlFocus("title","text",controlID) Edit1=Edit instance 1
ControlFocus("��", "","Edit1")


; Wait 10 seconds for the Upload window to appear
  WinWait("[CLASS:#32770]","",10)


; Set the File name text on the Edit field

  ControlSetText("��", "", "Edit1", "D:\upload_file.txt")

  Sleep(2000)

; Click on the Open button

  ControlClick("��", "","Button1");