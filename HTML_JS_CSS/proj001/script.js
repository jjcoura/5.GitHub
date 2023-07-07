function carregar() {
    var bicho = document.getElementById('txtani').value.toLowerCase();
    var img = document.getElementById('imagem');

    if (bicho === 'cachorro' || bicho === 'cao' || bicho === 'toto' || bicho === 'totó' || bicho === 'cão') {
        // Cachorro
        img.src = 'ft-cao.png';
        document.body.style.backgroundColor = '#c2734a';
    } else if (bicho === 'gato' || bicho === 'bichano' || bicho === 'cat' || bicho === 'gata' || bicho === 'Gato') {
        // Gato
        img.src = 'ft-gato.png';
        document.body.style.backgroundColor = '#9e9283';
    } else if (bicho === 'porco' || bicho === 'leitão' || bicho === 'leitao' || bicho === 'suíno' || bicho === 'porca' || bicho === 'leitoa' || bicho === 'suino') {
        // Porco
        img.src = 'ft-porco.png';
        document.body.style.backgroundColor = '#e0909d';
    } else if (bicho === 'cavalo' || bicho === 'egua' || bicho === 'égua' || bicho === 'Cavalo' || bicho === 'Égua' || bicho === 'Egua') {
        img.src = 'ft-cavalo.png';
        document.body.style.backgroundColor = '#38251f';
    } else if (bicho === 'rinoceronte' || bicho === 'Rinoceronte' || bicho === 'rino' || bicho === 'Rino') {
        // Rinoceronte
        img.src = 'ft-rino.png';
        document.body.style.backgroundColor = '#52555e';
    } else if (bicho === 'Bode' || bicho === 'Cabra' || bicho === 'Cabrito' || bicho === 'bode' || bicho === 'cabra' || bicho === 'cabrito') {
        // Bode
        img.src = 'ft-bode.png';
        document.body.style.backgroundColor = '#10100e';
    } else if (bicho === 'onça'|| bicho === 'Onça' || bicho === 'Onca' || bicho === 'onca') {
        // Onça
        img.src = 'ft-onca.png';
        document.body.style.backgroundColor = '#d75c02';
    } else if (bicho === 'leao'|| bicho === 'Leao' || bicho === 'Leão' || bicho === 'leão' || bicho === 'felino' || bicho === 'Felino') {
        // Leão
        img.src = 'ft-leao.png';
        document.body.style.backgroundColor = '#f2c5a5';
    } else if (bicho === 'elefante'|| bicho === 'Elefante') {
        // Elefante
        img.src = 'ft-elefante.png';
        document.body.style.backgroundColor = '#646470';
    } else if (bicho === 'girafa'|| bicho === 'Girafa') {
        // Girafa
        img.src = 'ft-girafa.png';
        document.body.style.backgroundColor = '#85501d';
    } else if (bicho === 'burro'|| bicho === 'Burro' || bicho === 'Jegue' || bicho === 'jegue' || bicho === 'Jumento'|| bicho === 'jumentinho'|| bicho === 'jumento' || bicho === 'Asno' || bicho === 'asno') {
        // Burro
        img.src = 'ft-burro.png';
        document.body.style.backgroundColor = '#514847'; 
    } else if (bicho === 'pato'|| bicho === 'Pato' || bicho === 'Patinho' || bicho === 'Pata' || bicho === 'pata' || bicho === 'patinho') {
        // Pato
        img.src = 'ft-pato.png';
        document.body.style.backgroundColor = '#d0c7d2';  
    } else if (bicho === 'jacaré'|| bicho === 'jacare' || bicho === 'Jacaré'|| bicho === 'Jacare'|| bicho === 'crocodilo' || bicho === 'Crocodilo'|| bicho === 'Aligator' || bicho === 'aligator') {
        // Jacaré
        img.src = 'ft-jacare.png';
        document.body.style.backgroundColor = '#4f3815'; 
    } else if (bicho === 'galo'|| bicho === 'Galo') {
        // Galo
        img.src = 'ft-galo.png';
        document.body.style.backgroundColor = '#e01b37';
    } else if (bicho === 'peixe'|| bicho === 'Peixe' || bicho === 'Peixinho' || bicho === 'peixinho') {
        // Peixe
        img.src = 'ft-peixe.png';
        document.body.style.backgroundColor = '#e05e24';
    } else if (bicho === 'vaca'|| bicho === 'Vaca' || bicho === 'Vaquinha' || bicho === 'vaquinha') {
        // Vaca
        img.src = 'ft-vaca.png';
        document.body.style.backgroundColor = '#521001';
    } else if (bicho === 'ave'|| bicho === 'Ave' || bicho === 'Pássaro' || bicho === 'pássaro' || bicho === 'Passarinho' || bicho === 'passarinho' || bicho === 'passaro') {
        // Passarinho
        img.src = 'ft-ave.png';
        document.body.style.backgroundColor = '#074264';
    } else if (bicho === 'Hipo'|| bicho === 'hipo' || bicho === 'Hipopótamo' || bicho === 'hipopótamo' || bicho === 'hipopotamo') {
        // Hipopótamo
        img.src = 'ft-hipo.png';
        document.body.style.backgroundColor = '#776b76';
    } else if (bicho === 'galinha'|| bicho === 'Galinha' || bicho === 'Frango' || bicho === 'frango') {
        // Galinha
        img.src = 'ft-gali.png';
        document.body.style.backgroundColor = '#c09c88';
    } else if (bicho === 'ovelha'|| bicho === 'ovelinha' || bicho === 'Ovelha' || bicho === 'Ovelinha') {
        // Ovelha
        img.src = 'ft-ove.png';
        document.body.style.backgroundColor = '#4c504'
    } else if (bicho === 'boi'|| bicho === 'Boi' || bicho === 'Gado' || bicho === 'gado' || bicho === 'bovino' || bicho === 'Bovino' || bicho === 'Touro' || bicho === 'touro') {
        // Vaca
        img.src = 'ft-boi.png';
        document.body.style.backgroundColor = '#b98a69';
    }  else {
        // BICINHO NÃO ENCONTRADO!!!
        img.src = 'ft-nao.png';
        document.body.style.backgroundColor = '#000000';
    }
}