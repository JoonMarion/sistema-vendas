(function (win, doc) {
    'use strict';

    // VERIFICA SE O USUÁRIO QUER MESMO DELETAR O DADO
    if (doc.querySelector('.btnDel')) {
        let btnDel = doc.querySelectorAll('.btnDel');
        for (let i = 0; i < btnDel.length; i++) {
            btnDel[i].addEventListener('click', function (event) {
                if (confirm('Deseja mesmo apagar este dado?')) {
                    return true;
                } else {
                    event.preventDefault();
                }
            });
        }
    }

    // AJAX DO FORM
    if (doc.querySelector('#form')) {
        let form = doc.querySelector('#form');
        function sendForm(event) {
            event.preventDefault();
            let data = new FormData(form);
            let ajax = new XMLHttpRequest();
            let token = doc.querySelectorAll('input')[0].value;
            ajax.open('POST', form.action);
            ajax.setRequestHeader('X-CSRF-TOKEN', token);
            ajax.onreadystatechange = function () {
                if (ajax.status === 200 && ajax.readyState === 4) {
                    let result = doc.querySelector('#result');
                    result.innerHTML = 'Operação realizada com sucesso! Aguarde...';
                    result.classList.add('alert');
                    result.classList.add('alert-success');
                    window.setTimeout(function () {
                        window.location.reload();
                    }, 1000);
                }
            };
            ajax.send(data);
            form.reset();
        }
        form.addEventListener('submit', sendForm, false);
    }
})(window, document);

// FUNÇÃO PARA MOSTRAR E OCULTAR SENHA NO FORM
const passwordInput = document.getElementById('password');
const eyeSvg = document.getElementById('eyeSvg');

function eyeClick() {
    let inputTypeIsPassword = passwordInput.type === 'password';

    if (inputTypeIsPassword) {
        showPassword();
    } else {
        hidePassword();
    }
}

function showPassword() {
    passwordInput.setAttribute('type', 'text');
    var element = document.getElementById('eyeSvg');
    var src = element.getAttribute('data-original');
    element.setAttribute('src', src);
}

function hidePassword() {
    passwordInput.setAttribute('type', 'password');
    var element = document.getElementById('eyeSvg');
    var src = element.getAttribute('data-original2');
    element.setAttribute('src', src);
}