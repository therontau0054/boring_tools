function addStyleToElements() {
    var elements = document.getElementsByClassName('notranslate');
    
    for (var i = 0; i < elements.length; i++) {
        elements[i].style.textAlign = 'justify';
        elements[i].style.display = 'block';
    }
  }

window.addEventListener('load', (event) => {
    if (document.documentElement.classList.contains('notion-html')) {
        addStyleToElements();
    }

    var observer = new MutationObserver(function(mutationsList, observer) {
        mutationsList.forEach(function(mutation) {
            if (mutation.type === 'childList' || (mutation.type === 'attributes' && mutation.attributeName === 'class')) {
                if (document.documentElement.classList.contains('notion-html')) {
                    addStyleToElements();
                }
            }
        });
    });

  observer.observe(document.documentElement, { attributes: true, childList: true, subtree: true });
});