let posts = document.querySelectorAll('.post')

posts.forEach(function (post) {
    const button = post.querySelector('.like-button')
    const display = post.querySelector('.like-count')
    let count = Number(post.querySelector('.like-count').innerText)

    button.addEventListener('click', function () {
        count += 1
        display.textContent = count
    })
})