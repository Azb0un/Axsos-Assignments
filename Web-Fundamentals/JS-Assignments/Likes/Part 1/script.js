const btn = document.querySelector('.like-count')
const countDisplay = document.querySelector('#count')

let count = 0

btn.addEventListener("click", () => {
    count ++
    countDisplay.textContent = count 
})
