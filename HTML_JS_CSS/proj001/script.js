function carregar() {
    var bicho = document.getElementById('txtani').value.toLowerCase();
    var img = document.getElementById('imagem');

    if (bicho === 'cachorro' || bicho === 'cao' || bicho === 'toto' || bicho === 'totó' || bicho === 'cão') {
        // Cachorro
        img.src = 'ft-cao.png';
        document.body.style.backgroundColor = '#c2734a';
    } else if (bicho === 'gato' || bicho === 'bichano' || bicho === 'cat' || bicho === 'gata' || bicho === 'Gato') {
        // Gato
        img.src = 'ft-gato.png'
        document.body.style.backgroundColor = '#9e9283';
    } else if (bicho === 'porco' || bicho === 'leitão' || bicho === 'leitao' || bicho === 'suíno' || bicho === 'porca' || bicho === 'leitoa' || bicho === 'suino') {
        // Porco
        img.src = 'ft-porco.png'
        document.body.style.backgroundColor = '#e0909d';
    } else if (bicho === 'cavalo' || bicho === 'egua' || bicho === 'égua' || bicho === 'Cavalo' || bicho === 'Égua' || bicho === 'Egua') {
        img.src = 'ft-cavalo.png'
        document.body.style.backgroundColor = '#38251f';
    } else if (bicho === 'rinoceronte' || bicho === 'Rinoceronte' || bicho === 'rino' || bicho === 'Rino') {
        // Rinoceronte
        img.src = 'ft-rino.png'
        document.body.style.backgroundColor = '#52555e';
    } else if (bicho === 'Bode' || bicho === 'Cabra' || bicho === 'Cabrito' || bicho === 'bode' || bicho === 'cabra' || bicho === 'cabrito') {
        // Bode
        img.src = 'ft-bode.png'
        document.body.style.backgroundColor = '#10100e';
    } else if (bicho === 'onça'|| bicho === 'Onça' || bicho === 'Onca' || bicho === 'onca') {
        // Onça
        img.src = 'ft-onca.png'
        document.body.style.backgroundColor = '#d75c02';
    } else if (bicho === 'leao'|| bicho === 'Leao' || bicho === 'Leão' || bicho === 'leão' || bicho === 'felino' || bicho === 'Felino') {
        // Leão
        img.src = 'ft-leao.png'
        document.body.style.backgroundColor = '#f2c5a5';
    } else if (bicho === 'elefante'|| bicho === 'Elefante') {
        // Elefante
        img.src = 'ft-elefante.png'
        document.body.style.backgroundColor = '#646470';
    } else if (bicho === 'girafa'|| bicho === 'Girafa') {
        // Girafa
        img.src = 'ft-girafa.png'
        document.body.style.backgroundColor = '#85501d';
    }  else {
        // BICINHO NÃO ENCONTRADO!!!
        img.src = 'imagem-nao-encontrada.png';
        document.body.style.backgroundColor = '#f5f5f5';
    }
}