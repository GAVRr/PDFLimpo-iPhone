# PDFLimpo para iPhone

Esta cópia mantém a aplicação Python recebida e acrescenta ajustes de tela para celular e metadados de instalação na tela inicial do iPhone. `app_original.py` é uma cópia intacta do `app.py` recebido; `app.py` contém, ao final, somente a camada adicional para celular.

## Publicar e abrir no iPhone

O caminho de publicação preparado é GitHub + Streamlit Community Cloud. O código fica no repositório GitHub e o serviço gera um endereço HTTPS para abrir no Safari.

1. Publique o conteúdo desta pasta em um repositório **público** no GitHub, como você escolheu.
2. Abra [share.streamlit.io](https://share.streamlit.io/) e conecte o GitHub.
3. Crie um app apontando para o repositório, a branch `main` e o arquivo `cloud_app.py`.
4. Em **Advanced settings → Secrets**, configure `OPENAI_API_KEY = "sua-chave"`. Não coloque a chave no repositório nem compartilhe o conteúdo dos Secrets.
5. Depois do primeiro deploy, abra **Manage app → Settings** e deixe o app **Private**. O repositório pode ser público enquanto o app fica restrito à sua conta.
6. Aguarde a implantação e copie o endereço HTTPS mostrado pelo Streamlit.
7. No iPhone, abra o endereço no Safari, toque em **Compartilhar** e em **Adicionar à Tela de Início**.

A visibilidade do app acompanha a configuração no Streamlit Community Cloud. A cópia preparada inclui `.gitignore` para manter `.env`, PDFs enviados e o banco de vetores fora do GitHub.

## Executar localmente

- Requer Python 3.10 ou superior.
- Instale os pacotes: `pip install -r requirements.txt`.
- Configure a chave `OPENAI_API_KEY` no ambiente ou num `.env` local (use `.env.example` como referência).
- Execute `streamlit run app.py`.

A tela inicial abre o site em modo de app. O processamento continua no servidor e requer internet; este pacote não é um binário nativo `.ipa` nem inclui publicação na App Store.

## Conteúdo

- `app.py`: cópia de trabalho com a camada iPhone acrescentada ao final
- `app_original.py`: cópia inalterada do app.py recebido
- `cloud_app.py`: inicializador para usar o segredo do Streamlit Community Cloud
- `main.py` e `criar_banco.py`: cópias dos arquivos fonte recebidos
- `logo/`: imagem usada pela aplicação
- `static/`: ícone e manifesto para instalação
- `base/` e `db/`: pastas de execução vazias; são preenchidas quando o usuário envia um PDF
- `.env` e o ambiente virtual da pasta original não foram copiados
