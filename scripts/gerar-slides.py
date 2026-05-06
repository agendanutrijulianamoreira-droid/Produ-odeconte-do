#!/usr/bin/env python3
"""
Gerador de slides em PDF para posts do Instagram.
Proporção 4:5 (2160x2700px) — fundo limpo, pronto para editar no Canva.
Uso: python3 scripts/gerar-slides.py <arquivo_json_de_slides> <saida.pdf>
"""

import sys
import json
import os
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

.slide {
    width: 2160px;
    height: 2700px;
    display: flex;
    flex-direction: column;
    padding: 72px 80px;
    page-break-after: always;
    page-break-inside: avoid;
    position: relative;
    background: #FAF8F4;
}

/* ── Header ── */
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 22px;
    color: #999;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    padding-bottom: 40px;
    border-bottom: 1px solid #E8E0D6;
}

/* ── Body ── */
.body {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 28px;
}

/* ── Footer ── */
.footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 22px;
    color: #999;
    letter-spacing: 0.04em;
    padding-top: 40px;
    border-top: 1px solid #E8E0D6;
}

/* ── Tipos de slide ── */

/* CAPA */
.slide-capa .body {
    gap: 36px;
    justify-content: flex-end;
    padding-bottom: 20px;
}
.slide-capa .label {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 24px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #B08A6A;
}
.slide-capa h1 {
    font-size: 76px;
    line-height: 1.08;
    color: #1A1209;
    font-weight: normal;
}
.slide-capa h1 em {
    color: #B08A6A;
    font-style: italic;
}

/* CONTEÚDO */
.slide-conteudo .numero {
    font-size: 120px;
    color: #EDE5D8;
    line-height: 1;
    font-family: Georgia, serif;
    margin-bottom: -16px;
}
.slide-conteudo h2 {
    font-size: 54px;
    line-height: 1.15;
    color: #1A1209;
    font-weight: bold;
}
.slide-conteudo .texto {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 30px;
    line-height: 1.65;
    color: #4A3F35;
}

/* TEXTO PURO (sem número) */
.slide-texto .titulo {
    font-size: 52px;
    line-height: 1.2;
    color: #1A1209;
}
.slide-texto .titulo span {
    color: #B08A6A;
    font-weight: bold;
}
.slide-texto .texto {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 30px;
    line-height: 1.65;
    color: #4A3F35;
}

/* CTA */
.slide-cta .body {
    gap: 40px;
    align-items: flex-start;
}
.slide-cta .tag {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 22px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #B08A6A;
    background: #F0E6D6;
    padding: 10px 24px;
    display: inline-block;
}
.slide-cta h2 {
    font-size: 62px;
    line-height: 1.1;
    color: #1A1209;
    font-weight: normal;
}
.slide-cta h2 strong {
    font-weight: bold;
}
.slide-cta .instrucao {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 30px;
    line-height: 1.5;
    color: #4A3F35;
}
.slide-cta .cta-box {
    background: #1A1209;
    color: #FAF8F4;
    padding: 28px 40px;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 28px;
    letter-spacing: 0.04em;
    margin-top: 8px;
}
"""

def header_html():
    return f'<div class="header"><span>{NOME}</span><span>{CARGO}</span></div>'

def footer_html():
    return f'<div class="footer"><span>{HANDLE}</span><span>{ANO}</span></div>'

def slide_capa(dados):
    label = dados.get("label", "")
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

def slide_texto(dados):
    titulo = dados.get("titulo", "")
    texto  = dados.get("texto", "")
    return f"""
    <div class="slide slide-texto">
        {header_html()}
        <div class="body">
            <p class="titulo">{titulo}</p>
            <p class="texto">{texto}</p>
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
    "capa":      slide_capa,
    "conteudo":  slide_conteudo,
    "texto":     slide_texto,
    "cta":       slide_cta,
}

def gerar_pdf(slides_json_path, output_pdf_path):
    with open(slides_json_path, "r", encoding="utf-8") as f:
        slides = json.load(f)

    html_slides = ""
    for s in slides:
        tipo = s.get("tipo", "conteudo")
        fn   = TIPOS.get(tipo, slide_conteudo)
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
