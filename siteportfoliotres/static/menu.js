let btnMenu = document.getElementById('btn-menu')
let menu = document.getElementById('menu-mobile')
let orvelay = document.getElementById ('orverlay-menu')

/*Abrir e fechar menu */
btnMenu.addEventListener('click', ()=>{
    menu.classList.add('abrir-menu')
})

menu.addEventListener('click', ()=>{
    menu.classList.remove('abrir-menu')
})

orvelay.addEventListener('click', ()=>{
    menu.classList.remove('abrir-menu')
})