const state = {
    views: {
        container: document.querySelector('.container'),
        tabuleiro: document.querySelector('.tabuleiro'),
        timer: document.createElement('div'),
        emojis: ["😺", "😺", "🐵", "🐵","🐶","🐶","🦁","🦁","🐯","🐯","🐻","🐻","🐸","🐸", "🐮", "🐮"]
    },
    values: {
        currentTime: 60, 
        openCards: [],
    },
    actions: {
    }
}

const shuffleEmojis = state.views.emojis.sort(() => (
    Math.random() > 0.5 ? 2 : -1
))




function createCards(){
    const cards = document.createElement('div')
    cards.classList.add('cards')
    

    for (let i = 0; i < state.views.emojis.length; i++){
        const card = document.createElement('div')
        card.className = 'card'
        card.innerHTML = shuffleEmojis[i]
        card.onclick = !card.classList.contains('box-match') ? handleClick : console.log('Não possível clicar!')
        cards.appendChild(card)
    }
    
    state.views.tabuleiro.appendChild(cards)
}

function handleClick(){
    if (state.values.openCards.length < 2){   
        this.classList.add('card-open')
        console.log(this.textContent)
        state.values.openCards.push(this)
    }
    
    if (state.values.openCards.length == 2){    
        setTimeout(checkMatch(), 500)
    }
}

const player = (audioPath) => ({
    audio: new Audio(audioPath),
    play(){
        this.audio.play()
    },
    stop(){
        this.audio.pause()
        // this.audio.currentTime = 0
    }
})

const music = player('src/audios/cell - AGST - Epidemic Sound.mp3')

function checkMatch(){
    if (state.values.openCards[0].innerHTML === state.values.openCards[1].innerHTML){
        state.values.openCards[0].classList.add('card-match')
        state.values.openCards[1].classList.add('card-match')
    }else{
        setTimeout(() =>{
            state.values.openCards[0].classList.remove('card-open')
            state.values.openCards[1].classList.remove('card-open')
        }, 800)
        
    }
    setTimeout(() => {state.values.openCards = []}, 1000)

    if(document.querySelectorAll('.card-match').length === state.views.emojis.length){
        const winner = player('src/audios/winner.m4a')
        music.stop()
        winner.play()
        // setTimeout(alert('Você venceu!'),100)
    }
}




function createAudioIcon(audioPath){
    // const player = player(audioPath)
    const container = document.querySelector('.container')
    const span = document.createElement('span')

    span.innerHTML = "<span class='material-symbols-outlined audio'>volume_off</span>"
    span.addEventListener('click', e => {
        const icon = e.target

        icon.textContent = icon.textContent === 'volume_up' ? 'volume_off' : "volume_up"
        
        if(icon.textContent === 'volume_up'){
            music.play()
        }else{
            music.stop()
        }
    })
    container.appendChild(span)

}

function createModal(){
    const container = document.querySelector('.container')
    const modal = document.createElement('div')
    const span = document.createElement('span')
    const close = document.createElement('p')

    close.textContent = 'X'
    close.classList.add('close-modal')
    modal.appendChild(close)
    
    close.addEventListener('click', e => {
        modal.classList.add('hide')
        console.log(modal)
    })

    span.textContent = 'Para ativar o áudio, click no ícone à direita do cabeçalho. Divirta-se 😉'
    span.classList.add('span-modal')
    modal.appendChild(span)

    modal.classList.add('modal')
    container.appendChild(modal)


}

function game(){
    createModal()
    createCards()
    createAudioIcon()
}

game()