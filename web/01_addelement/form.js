
import { $ } from ".logger.js"
const form=$(".form")
form.onsubmit=(ev)=>{

    ev.preventDefault()
    const formdata= new FormData(ev.target)
    const addEl = formdata.get("addElement")
    console.log
}
