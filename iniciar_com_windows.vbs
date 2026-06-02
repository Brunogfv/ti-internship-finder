' Inicia a API e o Agendador em segundo plano (sem janela)
' Coloque este arquivo em: shell:startup

Set Shell = CreateObject("Wscript.Shell")
Shell.CurrentDirectory = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)

' Inicia a API (sem janela visivel)
Shell.Run "python -m uvicorn api:app --host 0.0.0.0 --port 8000", 0, False

' Inicia o agendador (sem janela visivel)
Shell.Run "python scheduler.py", 0, False
