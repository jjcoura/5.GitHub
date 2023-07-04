function carregar() {
    var msg  = window.document.getElementById('msg')
    var img  = window.document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    msg.innerHTML = `Agora são ${hora} horas.`
    if (hora >= 0 && hora < 12) {
        // BOM DIA!
        img.src = 'manha-redondo.png'
        document.body.style.background = '#f6e5c2'
    } else if (hora >= 12 && hora <= 18) {
        // BOA TARDE!
        img.src = 'por-sol-redondo.png'
        document.body.style.background = '#a51502'
    } else {
        //BOA NOITE
        img.src = 'noite-redondo.png'
        document.body.style.background = '#201c1c'
    }
}
