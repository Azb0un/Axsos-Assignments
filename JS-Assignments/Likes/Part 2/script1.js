const btnNeil = document.querySelector('.likeBtnNeil')
const btnNichole = document.querySelector('.likeBtnNichol')
const btnJim = document.querySelector('.likeBtnJim')

const displayCountNeil = document.querySelector('#countNeil')
const displayCountNichol = document.querySelector('#countNichol')
const displayCountJim =  document.querySelector('#countJim')

var countNeil = 0
var countNichol = 0
var countJim = 0

btnNeil.addEventListener('click' , function(){
    countNeil += 1
    displayCountNeil.textContent = countNeil
})
btnNichole.addEventListener('click', function(){
    countNichol += 1 
    displayCountNichol.textContent = countNichol
})
btnJim.addEventListener('click', function(){
    countJim +=1
    displayCountJim.textContent = countJim
})