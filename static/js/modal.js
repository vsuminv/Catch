const body = document.querySelector('body');
const modal = document.querySelectorAll('.modal');
const btnOpenPopup = document.querySelectorAll('.btn-open-popup');
const ProfileOpenPopup = document.querySelectorAll('.profile-open-popup');
const closeBtn = document.querySelectorAll('.modal_btn_close');

btnOpenPopup.forEach((item, idx) =>{

    item.addEventListener('click', (e)=>{
    e.target.previousElementSibling.classList.toggle('show')

    if (e.target.previousElementSibling.classList.contains('show')) {
      body.style.overflow = 'hidden';
    }
    })
    
    item.addEventListener('click', (e) => {
        if (e.target === modal) {
          modal.classList.toggle('show');

          if (!modal.classList.contains('show')) {
            body.style.overflow = 'auto';
          }
        }
      });

});

//Hide modal
window.addEventListener('click', (e) => {
    if (e.target.getAttribute('class') == 'modal show') 
        e.target.classList.remove('show');
});

closeBtn.forEach((item, idx) => {
  item.addEventListener('click', (e)=>{
    console.log(e.target);
    e.target.parentElement.classList.remove('show');
  });
  
});
