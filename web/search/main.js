import data from "./data.js";

const d = document
const $ = s => d.querySelector(s)
const $$ = s => d.querySelectorAll(s)

const formSearch = $(".form-search")
const contentCard = $(".content-card")

// funcion que crea una tabla con contenido dinamico
function createTable () {

    let tr = ""
    data.forEach( el =>{
        tr += `
            <tr class="content-table">
                <td>${el.name}</td>
            </tr>
        `
    })

    let table = `
    <table>
        <thead>
            <tr>
                <th> name></th>
                <th> age</th>
            </th>
        </thead>
        <tbody>
            ${tr}

        </tbody>
    </table>
    `
    contentCard.innerHTML = table

}
createTable()

// funcion que se encargara de filtrar los elemnetos de la tabla
formSearch. addEventListener("submit", (ev) => {
    ev.preventDefault()
    const field = new FormData(ev.target)
    const search = field.get("search")
    const rows =  $$(".content-table")

    rows.forEach(row => {
        const rowsex = row
        if (row.includes(search)) {
            row.classList.add("filter")
        } else {
            row.classList.remove
        }
    })
}) 