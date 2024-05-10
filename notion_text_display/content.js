function addStyleToElements() {
    var elementsWithClassA = document.getElementsByClassName('notranslate');
    
    for (var i = 0; i < elementsWithClassA.length; i++) {
        elementsWithClassA[i].style.textAlign = 'justify';
        elementsWithClassA[i].style.display = 'block';
    }
  }

window.addEventListener('load', (event) => {
  console.log("hhhhhhhhhhhhhhhhh")
  if (document.documentElement.classList.contains('notion-html')) {
      console.log("hhhhhhhhhhhhhhhhh===============")
    addStyleToElements();
  }
  console.log("===============hhhhhhhhhhhhhhhhh")
  // 监听页面内容的变化
  var observer = new MutationObserver(function(mutationsList, observer) {
    mutationsList.forEach(function(mutation) {
      if (mutation.type === 'childList' || (mutation.type === 'attributes' && mutation.attributeName === 'class')) {
        // 检查页面的根元素是否包含 'notion' 类名
        if (document.documentElement.classList.contains('notion-html')) {
          // 添加样式
          addStyleToElements();
        }
      }
    });
  });

  // 监听根元素的变化
  observer.observe(document.documentElement, { attributes: true, childList: true, subtree: true });
});