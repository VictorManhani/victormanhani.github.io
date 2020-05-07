document.getElementById('cabecalho').innerHTML = `
<div class="logo-cabecalho">
    <a href="../index.html">Um Blog</a>
</div>
`

document.getElementById('menu').innerHTML = `
<ul>
    <li> <a href="../index.html">Início</a> </li>
    <li> <a href="../pages/curriculo.html">Currículo</a> </li>
    <li> <a href="../pages/sobre.html">Sobre</a> </li>
    <li class="dropdown">
        <a href="../pages/utilidades.html" class="dropbtn">Utilidades</a>
        <div class="dropdown-content">
            <a href="../pages/sites.html">Sites Úteis</a>
            <a href="../pages/dicas.html">Dicas Úteis</a>
            <a href="../pages/codigos.html">Códigos Úteis</a>
            <a href="../pages/livros.html">Livros Úteis</a>
            <a href="../pages/programas.html">Programas Úteis</a>
            <a href="../pages/frases.html">Frases Úteis</a>
            <a href="../pages/materiais.html">Materiais Úteis</a>
        </div>
    </li>
    <li> <a href = "../pages/python.html">Python</a> </li>
    <li> <a href = "../pages/jquery.html">JQuery</a> </li>
    <li> <a href = "../pages/contato.html">Contato</a> </li>
</ul>
`

document.getElementById('barra-lateral').innerHTML = `
<div class="espacamento">
    <h1>Mais</h1>
        <p id = "palavra"></p>
    <p>
        <img src="../img/psg1.png" />
    </p>
    <p>
        <img src="../img/psg2.png"/>
    </p>
    <p>
        <img src="../img/psg3.png" />
    </p>
</div>
`

let url = "https://bibleapi.co/api/verses/nvi/random";

fetch(url)
    .then(response => response.json())
    .then(data => {
        $('#palavra').html(
            `${data.text} - ${data.book.name} ${data.chapter}:${data.number}`
        );
});

document.getElementById('rodape').innerHTML = `
    <a href="../index.html" style="color: #eee;" >Victor Manhani</a> /
    <a href='https://contador.s12.com.br'><img src='https://contador.s12.com.br/img-8z6dBYWZCwdzc8w7-27.gif' border='0'></a><script type='text/javascript' src='https://contador.s12.com.br/ad.js?id=8z6dBYWZCwdzc8w7'></script>
`

function Enviar() {
    var nome = document.getElementById("nomeid").value;
    var email = document.getElementById("emailid").value;
    var message = document.getElementById("messageid").value;

    var link = `mailto:victorgomesmanhani@gmail.com?cc=${email}&subject=Meu Blog Contato ${nome}&body=${message}`;

    window.location.href = link;

    if (nome.value != "") {
        alert('Obrigado sr(a) ' + nome + ' os seus dados serão encaminhados.');
    }
}