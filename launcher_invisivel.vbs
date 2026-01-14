Set WshShell = CreateObject("WScript.Shell") 
' O número 0 ali no final significa "Esconda a janela"
WshShell.Run chr(34) & "C:\Projetos\Python\ferramentas-automacao-python\executor_robo.bat" & Chr(34), 0
Set WshShell = Nothing