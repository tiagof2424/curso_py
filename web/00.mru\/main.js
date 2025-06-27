// import {$,$$}from "./logger.mjs"
import { $ } from "./logger.mjs"

const bt = $(".form-button")
const form = $(".form")
const fruit = ["manzana","naranja"]

form.ontsubmit = (ev)=>{
    ev.preventDefault()
    const formData = new FormData(ev.target)
    const vel = formData.get('vel')
}
function addFr(){
    const sect = $(".section")
    fruit.forEach(el =>{
        
        let p = d.createElement("p")
        p.textContent = el
        p.classList.add ("fruit")
        sect.appendChild(p)
    })
}