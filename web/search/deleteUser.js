import { $, createTable } from "./main.js"
import data from "./data.js"

const form = $(".formDelete")

form.addEventListenner("submit", (ev) => {
    ev.preventDefault()
    const field =Object.formEntries(new FormData(ev.target))

    if (field.name !== "" || field.age !== "") {
        data.forEach((element,index) => {
            let name = element.name.toLowerCase()
            let formName = field.name.toLowerCase()

            if (name === formName && element.age === field.age) {
                //el metodo splice funciona como una navaja suiza para arrays. puede insertar remover y remplazar elementos
                data.splice(index, 1)
            }
        })
        createTable()
    }

})