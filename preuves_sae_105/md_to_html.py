import sys
import markdown

def convert(f_md: str, f_html: str):
    """
    Lit un fichier au format Markdown, convertit son contenu en HTML 
    grâce à la bibliothèque 'markdown', et écrit le résultat dans un fichier de sortie.
    """
    with open(f_md, 'r', encoding='utf-8') as contenu_md:
        text = contenu_md.read()
    html_body = markdown.markdown(text)
    #Produit par l'IA car non demandé à la base mais necessaire pour une meilleure lisibilité.
    css = """
<style>
    :root {
        --primary: #3498db;
        --primary-dark: #2980b9;
        --bg: #f0f2f5;
        --text: #2c3e50;
        --card-bg: #ffffff;
        --warning-bg: #fff3cd;
        --warning-text: #856404;
    }

    body {
        font-family: 'Segoe UI', system-ui, sans-serif;
        line-height: 1.6;
        color: var(--text);
        max-width: 1000px;
        margin: 0 auto;
        padding: 40px 20px;
        background-color: var(--bg);
    }

    h1 { 
        color: #1a1a1a; 
        text-align: center; 
        font-size: 3.5em; 
        letter-spacing: -1px;
        margin-bottom: 20px;
    }

    h2 { 
        border-bottom: 3px solid var(--primary); 
        padding-bottom: 8px; 
        color: var(--primary-dark); 
        margin-top: 50px;
        font-weight: 1000;
    }

    h3 { 
        background: linear-gradient(135deg, var(--primary), var(--primary-dark));
        color: white; 
        padding: 12px 25px; 
        border-radius: 50px; 
        display: block; 
        margin: 0 auto 25px auto;
        box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3);
        text-align: center;
        max-width: fit-content;
    }

    img {
        display: block;
        width: 50%;
        max-width: 100%; 
        height: auto;
        margin-left: auto; /* Centrage automatique à gauche */
        margin-right: auto; /* Centrage automatique à droite */
        margin-top: 30px;
        margin-bottom: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        border: 1px solid rgba(0,0,0,0.05);
    }

    h5 { 
        font-size: 1rem; 
        margin: 10px 0; 
        padding: 12px;
        background: rgba(255, 255, 255, 0.5);
        border-radius: 8px;
        border-left: 4px solid var(--primary);
        font-weight: 400;
    }

    h5 strong { color: var(--text); }

    h4 em strong, h4 strong em { 
        display: block; 
        background: var(--warning-bg); 
        color: var(--warning-text); 
        padding: 20px; 
        border-left: 6px solid #ffeeba; 
        border-radius: 8px; 
        margin: 30px 0; 
        font-style: italic;
        text-align: center;
    }

    h4 { color: #1a1a1a; margin-top: 40px; font-size: 1.4em; text-align: center }

    ul { 
        background: var(--card-bg); 
        padding: 30px; 
        border-radius: 15px; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.05); 
        list-style-type: none; 
        margin-bottom: 30px; 
        border: 1px solid turquoise;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    ul:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px turquoise;
    }

    li { 
        margin-bottom: 8px; 
        font-size: 0.95em; 
        border-bottom: 1px solid #f8f9fa; 
        padding-bottom: 5px;
        display: flex;
    }

    li:last-child { border-bottom: none; }

    li strong { 
        color: var(--primary); 
        min-width: 200px; 
        flex-shrink: 0;
    }

    hr { 
        border: 0; 
        height: 1px; 
        background: linear-gradient(to right, transparent, #dcdde1, transparent); 
        margin: 50px 0; 
    }

    @media (max-width: 768px) {
        body { padding: 20px; }
        li { flex-direction: column; }
        li strong { margin-bottom: 2px; }
        h1 { font-size: 2.5em; }
    }
</style>
"""
    page_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rapport d'analyse</title>
    {css}
</head>
<body>
    {html_body}
</body>
</html>"""
    with open(f_html, 'w', encoding='utf-8') as contenu_html:
        contenu_html.write(page_html)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Utilisation : python3 md_to_html.py *fichier.md* *fichier.html*")
    else:
        convert(sys.argv[1], sys.argv[2])