"""Gera a versão da LP para colar num widget HTML do Elementor (tema Hello Elementor).

uso: python3 wordpress/gerar.py <commit-do-github-com-os-assets>
saída: wordpress/elementor-html.html

- tira <html>/<head>/<body> e deixa só fontes, estilo, script e conteúdo;
- troca os caminhos assets/img/ por URLs do jsDelivr fixadas no commit (as imagens vêm do repo zephcompany/cleyton-cgroup);
- envolve o conteúdo em <div id="cg-root"> e acrescenta a camada de compatibilidade com o Hello Elementor e o container do Elementor.
"""
import re
import sys
from pathlib import Path

aqui = Path(__file__).resolve().parent
commit = sys.argv[1]
src = (aqui.parent / 'index.html').read_text(encoding='utf-8')

head = src[src.index('<head>') + 6: src.index('</head>')]
body = src[src.index('<body>') + 6: src.index('</body>')]

fontes = '\n'.join(re.findall(r'<link rel="preconnect"[^>]*>|<link href="https://fonts\.googleapis\.com[^>]*>', head))
script_js = re.search(r'<script>[^<]*classList\.add\(\'js\'\)</script>', head).group(0)
estilo = re.search(r'<style>(.*?)</style>', head, re.S).group(1)

compat = '''
/* ============ compatibilidade WordPress (Hello Elementor + Elementor) ============ */
h1,h2,h3,h4,h5,h6,p,ul,ol,li,figure,blockquote{margin:0}
ul,ol{padding:0}
.e-con:has(#cg-root),.e-con:has(#cg-root)>.e-con-inner{--padding-top:0px;--padding-right:0px;--padding-bottom:0px;--padding-left:0px;--gap:0px;--row-gap:0px;--column-gap:0px;--content-width:100%;--container-max-width:100%;padding:0!important;max-width:none!important;width:100%}
.elementor-widget:has(#cg-root){width:100%;margin:0!important;--kit-widget-spacing:0px}
.elementor-widget:has(#cg-root)>.elementor-widget-container{margin:0;padding:0}
#cg-root{width:100%;font-family:var(--font);text-align:left}
.nav__btn:hover,.nav__btn:focus,.rodape__ig:hover,.rodape__ig:focus{color:#fff}
.btn:hover,.btn:focus{color:#fff}.btn--inv:hover,.btn--inv:focus{color:#1247d1}
.nav__burger:hover,.nav__burger:focus{background:rgba(147,185,255,.14);border-color:rgba(147,185,255,.4);color:#fff}
'''

cdn = f'https://cdn.jsdelivr.net/gh/zephcompany/cleyton-cgroup@{commit}/assets/img/'
saida = (
    '<!-- LP C Grup Mídia: gerado por wordpress/gerar.py a partir do index.html. Não editar aqui. -->\n'
    + fontes + '\n' + script_js + '\n'
    + '<style>' + compat + estilo + '</style>\n'
    + '<div id="cg-root">' + body + '</div>\n'
).replace('assets/img/', cdn)

restos = re.findall(r'(?:src|href)="(?!https?:|#|data:)[^"]+"', saida)
assert not restos, restos
(aqui / 'elementor-html.html').write_text(saida, encoding='utf-8')
print('ok', len(saida), 'bytes;', saida.count(cdn), 'imagens no jsDelivr')
