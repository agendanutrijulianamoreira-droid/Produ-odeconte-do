#!/usr/bin/env python3
"""
Gerador de slides em PDF e PNG para posts do Instagram.
Proporção 4:5 (2160x2700px) — tipografia editorial limpa, sem fotos.

Uso:
  python3 scripts/gerar-slides.py slides.json saida.pdf        → gera PDF
  python3 scripts/gerar-slides.py slides.json saida.pdf --png  → gera PDF + PNGs
"""

import sys
import os
import json
from weasyprint import HTML, CSS

HANDLE = "@nutridamulhermoderna"
NOME   = "Juliana Moreira"
CARGO  = "Nutricionista"
ANO    = "2026"

BASE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&display=swap');

@page {
    size: 2160px 2700px;
    margin: 0;
}
* { box-sizing: border-box; margin: 0; padding: 0; }

body {
    font-family: Georgia, 'Times New Roman', serif;
    background: #F4EFE4;
}

/* ── Slide base ── */
.slide {
    width: 2160px;
    height: 2700px;
    display: flex;
    flex-direction: column;
    padding: 160px 144px;
    page-break-after: always;
    page-break-inside: avoid;
    position: relative;
    overflow: hidden;
    background: #F4EFE4;
}

/* ── Número decorativo de fundo ── */
.numero-bg {
    position: absolute;
    bottom: -120px; right: -40px;
    font-family: Georgia, serif;
    font-size: 800px; font-weight: 700;
    color: #C9A435; opacity: 0.06;
    line-height: 1; pointer-events: none;
    user-select: none;
}

/* ── Barra de acento dourado ── */
.acento {
    width: 96px; height: 8px;
    background: #C9A435; border-radius: 4px;
    margin-bottom: 56px;
}

/* ── Tag / série ── */
.tag-serie {
    font-family: 'Lato', Arial, sans-serif;
    font-size: 28px; font-weight: 700;
    letter-spacing: 6px; text-transform: uppercase;
    color: #C9A435;
    margin-bottom: 56px;
}

/* ── Header ── */
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: 'Lato', Arial, sans-serif;
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
    font-family: 'Lato', Arial, sans-serif;
    font-size: 40px;
    color: #7A7068;
    letter-spacing: 0.04em;
    padding-top: 72px;
    margin-top: auto;
}
.footer .handle { color: #C9A435; font-weight: 700; }
.footer .num-slide { opacity: 0.5; }

/* ── Body ── */
.body {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

/* ════════════════════════════════════════
   EDITORIAL — texto corrido com bold inline
   ════════════════════════════════════════ */
.slide-editorial { background: #F4EFE4; }
.slide-editorial .body { gap: 64px; justify-content: center; }
.slide-editorial .bloco {
    font-family: Georgia, serif;
    font-size: 76px; font-weight: normal;
    line-height: 1.55; color: #1A1209;
}
.slide-editorial .bloco strong { font-weight: bold; }
.slide-editorial .bloco em { color: #C9A435; font-style: italic; }

/* ════════════════════════════════════════
   FRASE — hook de impacto imediato
   ════════════════════════════════════════ */
.slide-frase { background: #FFFFFF; }
.slide-frase .body { gap: 48px; justify-content: center; }
.slide-frase .gancho {
    font-family: Georgia, serif;
    font-size: 108px; font-weight: 700;
    line-height: 1.08; letter-spacing: -4px;
    color: #1A1209;
}
.slide-frase .gancho em { color: #C9A435; font-style: italic; }
.slide-frase .gancho strong { font-weight: 700; }
.slide-frase .complemento {
    font-family: 'Lato', Arial, sans-serif;
    font-size: 56px; font-weight: 300;
    line-height: 1.5; color: #666666;
}

/* ════════════════════════════════════════
   CAPA — gancho do carrossel
   ════════════════════════════════════════ */
.slide-capa { background: #F4EFE4; }
.slide-capa .body { gap: 0; justify-content: center; }
.slide-capa .label {
    font-family: 'Lato', Arial, sans-serif;
    font-size: 28px; font-weight: 700;
    letter-spacing: 6px; text-transform: uppercase;
    color: #C9A435;
    margin-bottom: 56px;
}
.slide-capa h1 {
    font-family: Georgia, serif;
    font-size: 112px; font-weight: 700;
    line-height: 1.08; letter-spacing: -4px;
    color: #1A1209;
}
.slide-capa h1 em { color: #C9A435; font-style: italic; }
.slide-capa h1 strong { font-weight: 700; }

/* ════════════════════════════════════════
   CONTEUDO — slides numerados do carrossel
   ════════════════════════════════════════ */
.slide-conteudo { background: #FFFFFF; }
.slide-conteudo.par { background: #F4EFE4; }
.slide-conteudo .body { gap: 0; justify-content: center; }
.slide-conteudo .numero {
    font-family: Georgia, serif;
    font-size: 56px; font-weight: 700;
    color: #C9A435;
    margin-bottom: 40px;
}
.slide-conteudo h2 {
    font-family: Georgia, serif;
    font-size: 88px; font-weight: 700;
    line-height: 1.1; letter-spacing: -2px;
    color: #1A1209;
    margin-bottom: 48px;
}
.slide-conteudo h2 strong { font-weight: 700; }
.slide-conteudo .texto {
    font-family: 'Lato', Arial, sans-serif;
    font-size: 60px; font-weight: 300;
    line-height: 1.55; color: #333333;
}
.slide-conteudo .texto strong { font-weight: 700; color: #1A1209; }

/* ════════════════════════════════════════
   DESTAQUE — slide de ruptura
   ════════════════════════════════════════ */
.slide-destaque { background: #F4EFE4; }
.slide-destaque .body { gap: 56px; justify-content: center; }
.slide-destaque .barra {
    background: #2B1A10; color: #F4EFE4;
    padding: 28px 56px;
    display: inline-block;
    font-family: 'Lato', Arial, sans-serif;
    font-size: 44px; letter-spacing: 0.04em;
}
.slide-destaque .barra em { color: #C9A435; font-style: italic; }
.slide-destaque .texto {
    font-family: 'Lato', Arial, sans-serif;
    font-size: 72px; line-height: 1.45; color: #1A1209;
}
.slide-destaque .texto strong { font-weight: bold; }
.slide-destaque .rodape-texto {
    font-family: 'Lato', Arial, sans-serif;
    font-size: 60px; line-height: 1.5; color: #4A3F35;
}

/* ════════════════════════════════════════
   CTA — slide final (fundo escuro)
   ════════════════════════════════════════ */
.slide-cta {
    background: #2B1A10;
    align-items: center;
    text-align: center;
}
.slide-cta .circulo {
    position: absolute;
    width: 1200px; height: 1200px;
    border-radius: 50%;
    border: 2px solid rgba(201,164,53,0.15);
    top: 50%; left: 50%;
    margin-top: -600px; margin-left: -600px;
}
.slide-cta .body { gap: 56px; align-items: center; justify-content: center; }
.slide-cta .linha-cta {
    width: 120px; height: 8px;
    background: #C9A435; border-radius: 4px;
}
.slide-cta .tag {
    font-family: 'Lato', Arial, sans-serif;
    font-size: 32px; letter-spacing: 10px;
    text-transform: uppercase; color: rgba(244,239,228,0.5);
}
.slide-cta h2 {
    font-family: Georgia, serif;
    font-size: 100px; font-weight: 700;
    line-height: 1.1; letter-spacing: -2px;
    color: #F4EFE4; max-width: 1600px;
}
.slide-cta h2 strong { font-weight: 700; }
.slide-cta .instrucao {
    font-family: 'Lato', Arial, sans-serif;
    font-size: 52px; font-weight: 300;
    line-height: 1.5; color: rgba(244,239,228,0.7);
}
.slide-cta .cta-box {
    font-family: 'Lato', Arial, sans-serif;
    font-size: 48px; font-weight: 700;
    letter-spacing: 3px; text-transform: uppercase;
    color: #C9A435;
}
.slide-cta .footer .handle { color: #C9A435; }
.slide-cta .footer { color: rgba(244,239,228,0.4); }
"""

def header_html():
    return f'<div class="header"><span>{NOME}</span><span>{CARGO}</span></div>'

def footer_html(handle=None, num_slide=""):
    h = handle or HANDLE
    num_html = f'<span class="num-slide">{num_slide}</span>' if num_slide else f'<span>{ANO}</span>'
    return f'<div class="footer"><span class="handle">{h}</span>{num_html}</div>'

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
            <div class="acento"></div>
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
        <div class="numero-bg">01</div>
        {header_html()}
        <div class="body">
            {label_html}
            <div class="acento"></div>
            <h1>{titulo}</h1>
        </div>
        {footer_html(num_slide="01")}
    </div>"""

def slide_conteudo(dados):
    numero    = dados.get("numero", "")
    titulo    = dados.get("titulo", "")
    texto     = dados.get("texto", "")
    par       = dados.get("par", False)
    par_class = " par" if par else ""
    num_bg    = f'<div class="numero-bg">{numero}</div>' if numero else ""
    num_html  = f'<div class="numero">— {numero}</div>' if numero else ""
    return f"""
    <div class="slide slide-conteudo{par_class}">
        {num_bg}
        {header_html()}
        <div class="body">
            {num_html}
            <div class="acento"></div>
            <h2>{titulo}</h2>
            <p class="texto">{texto}</p>
        </div>
        {footer_html(num_slide=numero)}
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
        <div class="circulo"></div>
        {header_html()}
        <div class="body">
            <div class="linha-cta"></div>
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
    return len(slides)


def gerar_png(pdf_path, output_dir=None):
    """Converte cada página do PDF em PNG 2160x2700px — formato padrão Instagram 4:5."""
    try:
        from pdf2image import convert_from_path
    except ImportError:
        print("⚠ pdf2image não instalado. Rode: pip install pdf2image --break-system-packages")
        return

    if output_dir is None:
        output_dir = os.path.splitext(pdf_path)[0] + "_slides"

    os.makedirs(output_dir, exist_ok=True)

    # size=(2160, 2700) fixa o tamanho exato — pronto para subir no Instagram
    imagens = convert_from_path(pdf_path, fmt="png", size=(2160, 2700))

    for i, img in enumerate(imagens, start=1):
        nome = os.path.join(output_dir, f"slide_{i:02d}.png")
        img.save(nome, "PNG")
        print(f"  ✓ slide_{i:02d}.png — {img.size[0]}×{img.size[1]}px")

    print(f"\n✓ {len(imagens)} slides PNG prontos em: {output_dir}/")
    return output_dir


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 gerar-slides.py slides.json saida.pdf [--png]")
        sys.exit(1)

    json_path   = sys.argv[1]
    pdf_path    = sys.argv[2]
    gerar_pngs  = "--png" in sys.argv

    n_slides = gerar_pdf(json_path, pdf_path)

    if gerar_pngs:
        print(f"\nConvertendo {n_slides} slides para PNG...")
        gerar_png(pdf_path)

