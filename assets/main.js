function showHide(ShowClass, HideClass) {
    const elementsToShow = document.querySelectorAll(`.${ShowClass}`);
    const elementsToHide = document.querySelectorAll(`.${HideClass}`);
  
    elementsToShow.forEach(element => {
      element.classList.remove('hidden');
    });
  
    elementsToHide.forEach(element => {
      element.classList.add('hidden');
    });
}

function copia(texto) {
  var elementoTemporal = document.createElement("textarea");
  elementoTemporal.value = texto;
  document.body.appendChild(elementoTemporal);
  elementoTemporal.select();
  document.execCommand("copy");
  document.body.removeChild(elementoTemporal);
  notify("Copiado!");
}

function initCopia(){
    const copyableElements = document.querySelectorAll('.copy');
    copyableElements.forEach(element => {
        element.addEventListener('click', function() {
            const textToCopy = this.innerText;
            copia(textToCopy);
        });
    });
}

// Función para mostrar el mensaje al lado del ratón
function notify(texto, miliseconds) {
    var x = event.clientX + 15;
    var y = event.clientY + 10;

    if (miliseconds === undefined) {
        miliseconds = 500;
    }

    var div = document.createElement("div");
    div.style.position = "fixed";
    div.style.left = x + "px";
    div.style.top = y + "px";
    div.style.fontSize = "80%";
    div.style.zIndex = "10000";
    div.textContent = texto;

    document.body.appendChild(div);

    setTimeout(function() {
        document.body.removeChild(div);
    }, miliseconds);
}

function switchTheme(){
    theme = document.getElementById("theme");
    checkbox = document.getElementById("themeSwitch");
    if (!checkbox.checked) {
        theme.href = "assets/themes/dark.css";
        
    } else {
        theme.href = "assets/themes/light.css";
    }
}