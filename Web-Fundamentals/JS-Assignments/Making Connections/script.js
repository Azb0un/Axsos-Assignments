
const two = document.querySelector('#two')

let twoCount = 2
function hideTod(){
    const todd = document.querySelector('.content-row1')
    todd.remove();
    twoCount -= 1;
    two.textContent = twoCount
}
function hidePhill(){
    const phill = document.querySelector('.content-row2')
    phill.remove()
    twoCount -=1
    two.textContent = twoCount
}

const acceptBtns = [
    document.querySelector('.accept1'),
    document.querySelector('.accept2')
]
const ignoreBtns = [
    document.querySelector('.ignore1'),
    document.querySelector('.ignore2')
]

const fouroneeight = document.querySelector('#plusfive')
let fouroneeightCount = 418

acceptBtns.forEach(btn => {
    btn.addEventListener('click', () => {
    fouroneeightCount++
    fouroneeight.textContent = fouroneeightCount
    })
})

ignoreBtns.forEach(btn => {
    btn.addEventListener('click', () => {
    fouroneeightCount--
    fouroneeight.textContent = fouroneeightCount
    })
})

function changeUsername(){
    const username = document.querySelector('.userName')
    const img = document.querySelector('#jane')
    username.textContent = "Alli"
    img.src = "images/linkedin_profile_photo_under_1mb.png"
}