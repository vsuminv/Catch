

const commentUpdate = document.querySelectorAll('.comment_update');
const commentDelete = document.querySelector('.comment_modal_delete')

commentUpdate.forEach((item, idx) =>{

    item.addEventListener('click', (e)=>{
  
    e.target.previousElementSibling.classList.toggle('comment_update');    
    })

    
  // function close () { 
  //   document.querySelector(".comment_div_modal").className = "comment_div_modal";
  // }
  
  // document.querySelector("#comment_modal_delete").addEventListener('click', close);
    
  // commentDelete.addEventListener("click", e => {
  //   document.querySelector(".comment_div_modal").className = "comment_div_modal";
  // })
  function close () { 
  document.querySelector(".comment_div_modal").className = "comment_div_modal";
}

document.querySelector("#comment_modal_delete").addEventListener('click', close);
});





// //Hide modal
window.addEventListener('click', (e) => {
    if (e.target.getAttribute('class') == 'comment_div_modal comment_update') 
        e.target.classList.remove('comment_update') 
});


// function show () {
//   document.querySelector(".comment_div_modal").className = "comment_div_modal comment_update";
// }

// function close () { 
//   document.querySelector(".comment_div_modal").className = "comment_div_modal";
// }

// document.querySelector("#comment_update").addEventListener('click', show);
// document.querySelector("#comment_modal_delete").addEventListener('click', close);


