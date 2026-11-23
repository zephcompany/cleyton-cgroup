# C Grup Mídia

Landing page da C Grup Mídia: engenharia de marketing e vendas.

Site estático (HTML + imagens).

- `index.html` — a página inteira (estilos e scripts inclusos)
- `assets/img/` — logo, símbolo, foto do Cleyton, favicon e imagem de compartilhamento
- Contato: constante `WHATSAPP` no fim do `index.html` (DDI + DDD + número, só dígitos).
  Vazia, os botões abrem a mensagem direta do Instagram `@cgroupmidia_`; preenchida, abrem o WhatsApp e o botão flutuante aparece.

## Deploy

`deploy.php` baixa a branch `main` deste repositório e atualiza os arquivos do site.
Depois que o domínio estiver na hospedagem, coloque o `deploy.php` na pasta do site e cadastre um webhook
do GitHub (evento push, JSON) apontando para `https://SEU-DOMINIO/deploy.php`:
cada envio para a `main` passa a ir para o ar sozinho.

Os arquivos `README.md` e `.gitignore` ficam só aqui no GitHub.
