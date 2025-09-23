// Estados globais
const state = {
    views:{
        panel: document.querySelector('.panel'),
        squares: document.querySelectorAll('.square'),
        score: document.querySelector('.score-player'),
        timer: document.querySelector('.time'),
        enemy: document.querySelector('.enemy'),
        lifes: document.querySelector('.lifes'),
        spanLevel: document.getElementById('span-level'),
    },
    values:{
        hitPosition: 0,
        result: 0,
        lifes: 3,
        currentTime: 60,
        level: 0,
        velocity: 1000,
        change: false
    },
    actions: {
        countDownTime: setInterval(countDown, 1000),
        timerId: setInterval(spanEnemy, 1000),
    }
}

function spanEnemy(){
    state.views.squares.forEach(square => {
        square.classList.remove('enemy')
    })

    let randomNumber = Math.floor(Math.random()*9)
    let randomSquare = state.views.squares[randomNumber]

    randomSquare.classList.add('enemy')

    state.values.hitPosition = randomSquare.id
}


function countDown(){
    if (state.values.currentTime > 0){
        state.values.currentTime--
        state.views.timer.textContent = state.values.currentTime
        console.clear()
        console.log('Level: ', state.values.level)
        console.log("Velocity: ", state.values.velocity)
        
    }else{
        clearInterval(state.actions.countDownTime)
        clearInterval(state.actions.timerId)
        text = '<p>O teu resultado foi: <br></br><span>' + state.values.result +'</span></p>'
        gameOverScreen(text)
        state.views.squares.forEach(square => {
            if (square.classList.contains('enemy')) square.classList.remove('enemy')
        })
    }
}

function gameOverScreen(text){
    playSound('end')
    modal = document.createElement('div')
    h1 = document.createElement('h1')
    p = document.createElement('p')
    p.innerHTML = text
    h1.textContent = 'Game Over'
    modal.appendChild(h1)
    modal.appendChild(p)
    close = document.createElement('button')
    close.textContent = 'X'
    close.classList.add('close')
    modal.appendChild(close)
    modal.classList.add('modal')
    state.views.panel.appendChild(modal)

    close.addEventListener('click', () => {
        modal.classList.add('hide')
        reset()
    })
    
}

function hit(){
    state.views.squares.forEach(square => {
        state.values.squareId = Math.floor(Math.random()*9)
        square.addEventListener('mousedown', ()=>{
            if (square.id === state.values.hitPosition){
                console.log('Acertou o inimigo')
                playSound('start')
                state.values.result += 1
                state.views.score.textContent = state.values.result
                state.values.hitPosition = null
                state.values.change = true
                changeLevel()
            }else if (state.values.lifes > 0){
                console.error('Errou!')
                state.values.lifes -= 1
                state.values.hitPosition = null
                state.views.lifes.textContent = 'x'+state.values.lifes
            }else {
                state.values.gameVelocity = 0
            }
        })
    })

}

function playSound(sound){
    let audio = new Audio(`../../src/sounds/${sound}.m4a`)
    audio.volume = 0.5
    audio.play()    
}

function changeLevel(){
    if(state.values.change && state.values.result % 5 == 0 && state.values.result > 0){
        state.values.change = false
        state.values.level++
        state.views.spanLevel.textContent = state.values.level
    }
}

function reset(){
    state.values.currentTime = 60
    state.values.hitPosition = 0
    state.values.level = 0
    state.values.lifes = 3
    state.values.result = 0

    state.actions.countDownTime = setInterval(countDown, 1000)
    state.actions.timerId = setInterval(spanEnemy, 1000)
}

function game(){
    
    hit()
    console.log('Game iniciado...')    
}

game()
