//1. inicializar el canvas
const canvas = document.querySelector("canvas")
const context = canvas.getContext("2d")
 //configuracion de la pantalla y tamaño de los bloques
 const BLOCK_SIZE = 20
 const BOARD_WIDTH = 14
 const BOARD_HEIGTH = 30

 //creando el tablero de tetris
 context.scale(BLOCK_SIZE,BLOCK_SIZE)
 //3. crear board de 30 filas
 const board = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 ]

 //4.la pieza del jugador
 const pice = {
    position: { x: 5, y:5 },
    shape: [
        [1,1],
        [1,1],
    ]
 }
//2. game loop <- parte importante esta es el area donde se dibujara nuestro escenario
function update() {
    drow()
    //loop ifinito o tambien conocido funcion recursiva
    //una fncion recursiva se llama a si misma
    window.requestAnimationFrame(update)
}

function drow() {
    //vamos a dibujar nuestro boad
    context.fillStyle = "#222"
    context.fillRect(0, 0, canvas.width, canvas.height)

    // pintar el board
    board.forEach((row, y) => {
        row.forEach((value, x) => {
            if (value === 1) {
                context.fillStyle = "red"
                context.fillRect(x, y, 1, 1)
            }
        })
    })
    pice.shape.forEach((row, y) => {
        row.forEach((value, x) => {
            if (value === 1){
                context.fillStyle ="yellow"
                context.fillRect(x + pice.position.x, y + pice.position.y,1,1)
            }
        })
    })
}
//5.mover la pieza
document.addEventListener("keydown", ev => {
    if (ev.key === "ArrowRight") {
        pice.position.x++
        if (checkCollision()) {
            pice.position.x--
        }
    }
    if (ev.key === "ArrowLeft") {
        pice.position.x--
        if (checkCollision()) {
            pice.position.x++
        }
    }
    if (ev.key === "ArrowDown") {
        pice.position.y++
        if (checkCollision()) {
            pice.position.y--
        }
    }
    if (ev.key === "ArrowUp") {
        const
    }
})
update()
