function addStyleToElements() {
    var elementsWithClassA = document.getElementsByClassName('notranslate');
    
    for (var i = 0; i < elementsWithClassA.length; i++) {
        elementsWithClassA[i].style.textAlign = 'justify';
        elementsWithClassA[i].style.display = 'block';
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