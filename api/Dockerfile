FROM us-east1-docker.pkg.dev/indoor-tracking-team/ar-backend/machine-learning-api-prod:latest

# Remova o diretório antigo e crie um novo
RUN rm -rf /app && mkdir -p /app
WORKDIR /app

# Exiba o conteúdo inicial do diretório do contêiner
RUN echo "Conteúdo inicial do contêiner:" && ls -la / && ls -la /app

# Copie os arquivos para o contêiner
COPY . /app

# Exiba o conteúdo após a cópia
RUN echo "Conteúdo do diretório após COPY:" && ls -la /app

# Opcionalmente, instale 'tree' para uma visualização hierárquica (caso não esteja disponível)
RUN apt-get update && apt-get install -y tree

# Exiba a estrutura hierárquica do diretório
RUN echo "Estrutura de diretórios:" && tree /app

# Exiba arquivos específicos, se necessário
RUN echo "Arquivos específicos:" && ls -la /app/main.py

# Comando padrão para execução
CMD ["python", "main.py"]
