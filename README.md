## Como Usar

1. **Clone este repositório**

   Primeiro, clone o repositório em sua máquina local:

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. **Instale as dependências**

   Certifique-se de que você tem Python instalado. Em seguida, instale as bibliotecas necessárias com o comando:

    ```bash
    pip install rembg pillow numpy
    ```

3. **Configure o caminho das pastas**

   No script `seu_script.py`, você precisará definir o caminho para as pastas de entrada e saída. Abra o script e modifique as variáveis `input_folder` e `output_folder` com os caminhos apropriados para suas pastas:

    ```python
    input_folder = r'C:\caminho\para\a\pasta\de\entrada'
    output_folder = r'C:\caminho\para\a\pasta\de\saida\semFundo'
    ```

   **Certifique-se de usar barras invertidas duplas (`\\`) ou barras normais (`/`) no caminho do Windows.**

4. **Execute o script**

   Após configurar os caminhos, execute o script com o comando:

    ```bash
    python seu_script.py
    ```

5. **Verifique as imagens processadas**

   As imagens com o fundo removido serão salvas na pasta especificada por `output_folder`. Verifique essa pasta para encontrar os arquivos processados.



