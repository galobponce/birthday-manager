let input = document.querySelector('input[name="filter"]')
input.addEventListener('keyup', () => {
  if (input.value != "") {
    // Gets all rows data
    let dataRows = Array.from(document.querySelectorAll('tr')).filter(trow => trow.dataset.row).map(t => t.dataset.row)
    // GET '/search'
    $.get('search?q=' + input.value, (data) => {
        let htmlContent = ''
        for (let i in data) {
            // Displays each person's name and its birthay
            let textContent = `${data[i].name} => ${data[i].month}/${data[i].day}`
            htmlContent += `<li class="list-group-item">${textContent}</li>`
        }
        // Displaying the htmlContent in DOM
        document.querySelector('ul[class="list-group list-group-flush"]').innerHTML = htmlContent
    })
  }
})