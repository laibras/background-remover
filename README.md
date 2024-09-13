# Background Removal Script

Este é um script em Python para remover o fundo de imagens usando a biblioteca `rembg`. 

## Como Usar

1. **Baixe o código**

   Faça o download ou clone este repositório para sua máquina local.

2. **Instale as dependências**

   Instale as bibliotecas necessárias executando o seguinte comando:

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

   Abra o script `seu_script.py` em uma IDE ou editor de texto que suporte Python. Certifique-se de definir os caminhos corretos para as pastas de entrada e saída dentro do script.

   Depois, execute o script:

    ```bash
    python seu_script.py
    ```

5. **Verifique a pasta de saída**

   As imagens com o fundo removido serão salvas na pasta de saída especificada no script.


