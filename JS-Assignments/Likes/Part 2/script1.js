const posts = document.querySelectorAll('.post')

posts.forEach(function (post) {
    const button = post.querySelector('.like-button')
    const display = post.querySelector('.like-count')
    let count = 0

    button.addEventListener('click', function () {
        count += 1
        display.textContent = count
    })
})