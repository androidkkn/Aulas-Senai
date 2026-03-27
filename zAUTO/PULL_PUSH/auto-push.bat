@echo off
echo Salvando seu codigo no GitHub...

cd C:\Users\46T1\Documents\Aulas-Kauan

:: Adiciona todas as modificacoes
git add .

:: Faz o commit com a data e hora atual
git commit -m "Auto backup de fim de expediente: %date% %time%"

:: Faz o push
git push origin main

echo.
echo Push concluido! Saindo do perfil em 5 segundos...

:: Pausa de 5 segundos para voce ler a mensagem
timeout /t 10

:: Comando para Fazer Logoff
shutdown /l