const d = document
const $ = s =>d.querySelector(s)
// definir variables
const form = $(".form")
form.onsubmit = (ev) =>{

    ev.preventDefault()
    const formData = new FormData(ev.target)
    console.log(formData);
    
}