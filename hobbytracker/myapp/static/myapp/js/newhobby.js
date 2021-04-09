var openModalButtons = document.querySelectorAll('[data-modal-target]');
var closeModalButtons = document.querySelectorAll('[data-close-button]');
var submitButtons = document.querySelectorAll('[submit-button]');
var overlay = document.getElementById('overlay');
openModalButtons.forEach(button => {
    button.addEventListener('click', () => {
        const modal = document.querySelector(button.dataset.modalTarget);
        openModal(modal);
    })
})
closeModalButtons.forEach(button => {
    button.addEventListener('click', () => {
        const modal = button.closest('.modal');
        closeModal(modal);
        
    })
})
submitButtons.forEach(button => {
    button.addEventListener('click', () => {
        var a = document.getElementById("id_timeLimit").value;
        var b = document.getElementById("id_name").value;
        var c = document.getElementById("id_spriteId").value;
        if(a <= 168 && a > 0 && b.trim().length && c != 0){
            document.getElementById("forms").submit();
        }
    })
}) 
function openModal(modal){
    if(modal == null) return;
    modal.classList.add('active');
    overlay.classList.add('active');
}
function closeModal(modal){
    if(modal == null) return;
    modal.classList.remove('active');
    overlay.classList.remove('active');
}