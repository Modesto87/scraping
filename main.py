import subprocess
import sys
import os
import logging
from Scraping.models import clear_database


# ========================
# Nova configuração de logging
# ========================

# Criação de um logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Nível de log (pode ser DEBUG, INFO, etc.)

# Criação de um manipulador de arquivo
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)

# Criação de um manipulador de console (para exibir no terminal)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formato dos logs
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Adicionar os manipuladores ao logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# ========================
# Resto do seu código
# ========================

# Adiciona o diretório 'Scraping' ao caminho de busca de módulos
sys.path.append(os.path.join(os.path.dirname(__file__), 'Scraping'))

try:
    from models import clear_database
except Exception as e:
    logger.error(f"Erro ao importar clear_database: {e}")
    sys.exit(1)

# Verificar se o Scrapy está instalado
try:
    subprocess.run(['scrapy', '--version'], check=True)
except FileNotFoundError:
    logger.error("O Scrapy não está instalado ou não foi encontrado no PATH.")
    sys.exit(1)


def main():
    try:
        question = "Voulez-vous faire le scraping? (y/n): "
        answer = input(question).strip().lower()

        if answer == 'y':
            # Limpar a base de dados antes de executar o scraping
            clear_database()
            logger.info("Base de dados limpa.")

            # Substitua 'abola' pelo nome da spider que deseja executar
            spider_name = "abola"

            # Executa o comando do Scrapy para rodar a spider
            cmd = ["scrapy", "crawl", spider_name]
            logger.info(f"Executando comando: {' '.join(cmd)}")

            # Captura a saída padrão e de erro do processo
            result = subprocess.run(cmd, capture_output=True, text=True)
            logger.info(f"Saída padrão: {result.stdout}")
            logger.error(f"Saída de erro: {result.stderr}")

            logger.info(f"Comando executado com código de retorno: {result.returncode}")
        elif answer == 'n':
            logger.info("Fermeture de l'application.")
        else:
            logger.warning("Réponse non valide. Fermeture de l'application.")
    except Exception as e:
        logger.error(f"Erro no main: {e}")


if __name__ == "__main__":
    main()

# Manter o terminal aberto após execução
input("Pressione Enter para sair...")
