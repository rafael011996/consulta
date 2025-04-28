import subprocess
import datetime

# Caminho até o repositório local
CAMINHO_REPOSITORIO = r'C:\TXT'  # <-- ajuste aqui se for outro caminho

def atualizar_git():
    try:
        # Entrar na pasta do projeto
        subprocess.run(['cd', CAMINHO_REPOSITORIO], shell=True)

        # Comandos git
        subprocess.run(['git', 'add', '.'], cwd=CAMINHO_REPOSITORIO)
        subprocess.run(['git', 'commit', '-m', f'Atualização automática: {datetime.datetime.now()}'], cwd=CAMINHO_REPOSITORIO)
        subprocess.run(['git', 'push'], cwd=CAMINHO_REPOSITORIO)
        
        print(f"[{datetime.datetime.now()}] Atualizado com sucesso!")

    except Exception as e:
        print(f"Erro ao atualizar: {e}")

if __name__ == "__main__":
    atualizar_git()
