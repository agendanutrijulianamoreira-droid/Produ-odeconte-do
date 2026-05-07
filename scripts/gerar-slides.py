#!/usr/bin/env python3
"""
Gerador de slides em PDF para posts do Instagram.
Proporção 4:5 (2160x2700px) — tipografia editorial limpa, sem fotos.
Uso: python3 scripts/gerar-slides.py <arquivo_json_de_slides> <saida.pdf>
"""

import sys
import json
from weasyprint import HTML, CSS

HANDLE = "@nutridamulhermoderna"
NOME   = "Juliana Moreira"
CARGO  = "Nutricionista"
ANO    = "2026"

BASE_CSS = """
@page {
    size: 2160px 2700px;
    margin: 0;
}
* { box-sizing: border-box; margin: 0; padding: 0; }

body {
    font-family: Georgia, 'Times New Roman', serif;
    background: #fff;
}

/* ── Slide base ── */
.slide {
    width: 2160px;
    height: 2700px;
    display: flex;
    flex-direction: column;
    padding: 144px 176px;
    page-break-after: always;
    page-break-inside: avoid;
    position: relative;
    background: #F5F1EB;
}

/* ── Header ── */
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 40px;
    color: #7A7068;
    letter-spacing: 0.04em;
    padding-bottom: 72px;
}

/* ── Footer ── */
.footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 40px;
    color: #7A7068;
    letter-spacing: 0.04em;
    padding-top: 72px;
}

/* ── Body ── */
.body {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

/* ════════════════════════════════════════
   EDITORIAL — texto corrido com bold inline
   (Modelo principal — padrão imagem 1)
   ════════════════════════════════════════ */
.slide-editorial .body {
    gap: 64px;
    justify-content: center;
}
.slide-editorial .bloco {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 80px;
    line-height: 1.45;
    color: #1A1209;
    font-weight: normal;
}
.slide-editorial .bloco strong {
    font-weight: bold;
    color: #1A1209;
}
.slide-editorial .bloco em {
    font-style: italic;
    color: #B08A6A;
}

/* ════════════════════════════════════════
   FRASE — hook de 1 linha, impacto imediato
   ════════════════════════════════════════ */
.slide-frase .body {
    justify-content: center;
    gap: 48px;
}
.slide-frase .gancho {
    font-family: Georgia, serif;
    font-size: 128px;
    line-height: 1.12;
    color: #1A1209;
    font-weight: normal;
}
.slide-frase .gancho strong {
    font-weight: bold;
}
.slide-frase .gancho em {
    font-style: italic;
    color: #C9A435;
}
.slide-frase .complemento {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 68px;
    line-height: 1.5;
    color: #4A3F35;
}

/* ════════════════════════════════════════
   CAPA — abertura do carrossel
   ════════════════════════════════════════ */
.slide-capa .body {
    gap: 48px;
    justify-content: flex-end;
    padding-bottom: 32px;
}
.slide-capa .label {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 44px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #B08A6A;
}
.slide-capa h1 {
    font-size: 136px;
    line-height: 1.06;
    color: #1A1209;
    font-weight: normal;
}
.slide-capa h1 em {
    color: #C9A435;
    font-style: italic;
}
.slide-capa h1 strong {
    font-weight: bold;
}

/* ════════════════════════════════════════
   CONTEUDO — slides de carrossel numerados
   ════════════════════════════════════════ */
.slide-conteudo .numero {
    font-size: 200px;
    color: #EDE5D8;
    line-height: 1;
    font-family: Georgia, serif;
    margin-bottom: -32px;
}
.slide-conteudo h2 {
    font-size: 96px;
    line-height: 1.12;
    color: #1A1209;
    font-weight: bold;
}
.slide-conteudo .texto {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 64px;
    line-height: 1.55;
    color: #4A3F35;
    margin-top: 24px;
}
.slide-conteudo .texto strong {
    font-weight: bold;
    color: #1A1209;
}

/* ════════════════════════════════════════
   DESTAQUE — barra colorida + texto curto
   ════════════════════════════════════════ */
.slide-destaque .body {
    gap: 56px;
    justify-content: center;
}
.slide-destaque .barra {
    background: #2B1A10;
    color: #F5F1EB;
    padding: 28px 48px;
    display: inline-block;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 56px;
    letter-spacing: 0.04em;
}
.slide-destaque .barra em {
    color: #C9A435;
    font-style: italic;
}
.slide-destaque .texto {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 76px;
    line-height: 1.45;
    color: #1A1209;
}
.slide-destaque .texto strong {
    font-weight: bold;
}
.slide-destaque .rodape-texto {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 60px;
    line-height: 1.5;
    color: #4A3F35;
}

/* ════════════════════════════════════════
   CTA — chamada final para ação
   ════════════════════════════════════════ */
.slide-cta .body {
    gap: 56px;
    align-items: flex-start;
    justify-content: center;
}
.slide-cta .tag {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 40px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #B08A6A;
    background: #EDE5D8;
    padding: 20px 48px;
    display: inline-block;
}
.slide-cta h2 {
    font-size: 108px;
    line-height: 1.08;
    color: #1A1209;
    font-weight: normal;
}
.slide-cta h2 strong { font-weight: bold; }
.slide-cta .instrucao {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 64px;
    line-height: 1.5;
    color: #4A3F35;
}
.slide-cta .cta-box {
    background: #1A1209;
    color: #F5F1EB;
    padding: 52px 72px;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 60px;
    letter-spacing: 0.04em;
    margin-top: 16px;
}
"""

def header_html():
    return f'<div class="header"><span>{NOME}</span><span>{CARGO}</span></div>'

def footer_html():
    return f'<div class="footer"><span>{HANDLE}</span><span>{ANO}</span></div>'

def slide_editorial(dados):
    blocos = dados.get("blocos", [])
    if isinstance(blocos, str):
        blocos = [blocos]
    html_blocos = "".join(f'<p class="bloco">{b}</p>' for b in blocos)
    return f"""
    <div class="slide slide-editorial">
        {header_html()}
        <div class="body">{html_blocos}</div>
        {footer_html()}
    </div>"""

def slide_frase(dados):
    gancho      = dados.get("gancho", "")
    complemento = dados.get("complemento", "")
    comp_html   = f'<p class="complemento">{complemento}</p>' if complemento else ""
    return f"""
    <div class="slide slide-frase">
        {header_html()}
        <div class="body">
            <p class="gancho">{gancho}</p>
            {comp_html}
        </div>
        {footer_html()}
    </div>"""

def slide_capa(dados):
    label  = dados.get("label", "")
    titulo = dados.get("titulo", "")
    label_html = f'<div class="label">{label}</div>' if label else ""
    return f"""
    <div class="slide slide-capa">
        {header_html()}
        <div class="body">
            {label_html}
            <h1>{titulo}</h1>
        </div>
        {footer_html()}
    </div>"""

def slide_conteudo(dados):
    numero = dados.get("numero", "")
    titulo = dados.get("titulo", "")
    texto  = dados.get("texto", "")
    num_html = f'<div class="numero">{numero}</div>' if numero else ""
    return f"""
    <div class="slide slide-conteudo">
        {header_html()}
        <div class="body">
            {num_html}
            <h2>{titulo}</h2>
            <p class="texto">{texto}</p>
        </div>
        {footer_html()}
    </div>"""

def slide_destaque(dados):
    barra       = dados.get("barra", "")
    texto       = dados.get("texto", "")
    rodape      = dados.get("rodape", "")
    barra_html  = f'<div class="barra">{barra}</div>' if barra else ""
    rodape_html = f'<p class="rodape-texto">{rodape}</p>' if rodape else ""
    return f"""
    <div class="slide slide-destaque">
        {header_html()}
        <div class="body">
            {barra_html}
            <p class="texto">{texto}</p>
            {rodape_html}
        </div>
        {footer_html()}
    </div>"""

def slide_cta(dados):
    tag       = dados.get("tag", "")
    titulo    = dados.get("titulo", "")
    instrucao = dados.get("instrucao", "")
    cta       = dados.get("cta", "")
    tag_html  = f'<div class="tag">{tag}</div>' if tag else ""
    cta_html  = f'<div class="cta-box">{cta}</div>' if cta else ""
    return f"""
    <div class="slide slide-cta">
        {header_html()}
        <div class="body">
            {tag_html}
            <h2>{titulo}</h2>
            <p class="instrucao">{instrucao}</p>
            {cta_html}
        </div>
        {footer_html()}
    </div>"""

TIPOS = {
    "editorial":  slide_editorial,
    "frase":      slide_frase,
    "capa":       slide_capa,
    "conteudo":   slide_conteudo,
    "destaque":   slide_destaque,
    "cta":        slide_cta,
}

def gerar_pdf(slides_json_path, output_pdf_path):
    with open(slides_json_path, "r", encoding="utf-8") as f:
        slides = json.load(f)

    html_slides = ""
    for s in slides:
        tipo = s.get("tipo", "editorial")
        fn   = TIPOS.get(tipo, slide_editorial)
        html_slides += fn(s)

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head><meta charset="utf-8"></head>
<body>{html_slides}</body>
</html>"""

    css = CSS(string=BASE_CSS)
    HTML(string=html).write_pdf(output_pdf_path, stylesheets=[css])
    print(f"✓ PDF gerado: {output_pdf_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 gerar-slides.py slides.json saida.pdf")
        sys.exit(1)
    gerar_pdf(sys.argv[1], sys.argv[2])
