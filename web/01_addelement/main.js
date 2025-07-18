import {d,$} from "./loggerr.js"
//definir variables


const friut = ["manzana", "naranja", "platano"]
const root = $("root")

friut.forEach(element => {
    let p = d.createElement("p")
    p.textContent = element
    root.appendChild(p)
})
