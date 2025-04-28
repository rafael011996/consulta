@echo off
cd /d C:\TXT
git add produtos.csv
git commit -m "Atualização automática do CSV"
git push origin main
