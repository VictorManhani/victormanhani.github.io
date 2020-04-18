from browser import document, alert
from browser.html import INPUT, H1, LABEL, BR, DIV, UL, FORM, A, LI, IMG, P

def cabecalho():
    div = DIV(Class = "cabecalho")

    logo = DIV(Class = "logo-cabecalho")
    logo <= A("Meu Blog", href = "index.html")
    
    pesquisa = DIV(Class = "pesquisa")
    pesquisa <= INPUT(type = "text")
    pesquisa <= INPUT(type = "submit", value = "Pesquisar")

    div <= logo
    div <= pesquisa
    return div

def menu():
    div = DIV(Class = "menu")
    ul = UL()

    li_inicio = LI(A('Início', href = "index.html"))
    li_sobre = LI(A('Sobre', href = "sobre.html"))
    
    a_utilidades = A('Utilidades', href = "utilidades.html", Class = "dropbtn")
    li_utilidades = LI(Class = "dropdown")
    li_utilidades <= a_utilidades
    div_utilidades = DIV(Class = "dropdown-content")
    div_utilidades <= A(
        'Sites Úteis', href = "sites.html") + A(
        'Dicas Úteis', href = "dicas.html") + A(
        'Códigos Úteis', href = "codigos.html") + A(
        'Livros Úteis', href = "livros.html") + A(
        'Programas Úteis', href = "programas.html") + A(
        'Frases Úteis', href = "frases.html") + A(
        'Materiais Úteis', href = "materiais.html")
    li_utilidades <= div_utilidades

    li_python = LI(A('Python', href = "python.html"))
    li_contato = LI(A('Contato', href = "contato.html"))

    ul <= li_inicio + li_sobre + li_utilidades + li_python + li_contato
    div <= ul
    return div

def barra_lateral():
    barraLateral = DIV(Class = "barra-lateral")
    espacamento = DIV(Class = "espacamento")
    mais = H1("Mais")
    palavra = P("Se algum de vocês tem falta de sabedoria, peça-a a Deus, que a todos dá livremente, de boa vontade; e lhe será concedida. - Tiago 1:5")
    img = IMG(src = "img/psg7.jpg")
    espacamento <= mais
    espacamento <= palavra
    espacamento <= img
    barraLateral <= espacamento
    return barraLateral

def rodape():
    return A(
        "Victor Manhani",
        href = "https://www.eletromanhani.com",
        target = "_blank",
        style = {'color': '#eee'}
    )