// showPage = (page) => {
//   document.querySelector(`#${page}`).style.display = 'block';
// }

window.onpopstate = function(event) {
  console.log(event.state.page);
    showPage(event.state.page);
  
}

function showPage(page) {
  document.querySelectorAll('div').forEach(div => {
    div.style.display = 'none';
  })
  
  document.querySelector(`#${page}`).style.display = 'block';
}

document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('button').forEach(button => {
    button.onclick = function() {
      const page = this.dataset.page;
      history.pushState({page: page}, "", `${page}`);
      showPage(page);
    }
  });

});