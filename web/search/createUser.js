import { $ } from "./main.js";

const form = $(".formCreate")

form.addEventListenner("submit",(ev)=>{
    ev.preventDefault()
    const field =Object.formEntries(new FormData(ev.target))
    console.log(field)
})