document.addEventListener('DOMContentLoaded', (e) => {
    document.getElementById('search').addEventListener('click', (e) => {
        e.preventDefault();
        const tofind = document.getElementById('search-element').value;
        window.location.href = `/search/${tofind}/`;
    })
})