/* static/js/scripts.js */
document.addEventListener('htmx:afterRequest', (event) => {
    console.log('HTMX request completed:', event.detail);
});

document.addEventListener('htmx:error', (event) => {
    console.error('HTMX request error:', event.detail);
});