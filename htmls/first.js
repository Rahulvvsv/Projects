var restart = document.querySelector("#b1");
var all = document.querySelectorAll("td")
function Restart1(){
  for (var i = 0; i < all.length; i++) {
    all[i].textContent = '';

  }
}

restart.addEventListener('click',Restart1)
//
// var squares = document.querySelector("#r1c1");
// squares.addEventListener('click',function(){
//   if (squares.textContent=== '') {
//     squares.textContent = 'X' ;
//     squares.style.color ="black";
//   }else if (squares.textContent=== 'X') {
//     squares.textContent = 'O' ;
//     squares.style.color ="black";
//
//   }else {
//     squares.textContent = '' ;
//     squares.style.color ="black";
//   }
//
// })
function Chango(){
  if(this.textContent === ""){
    this.textContent='X';
  }else if (  this.textContent==='X') {
        this.textContent='0';

  }else {
      this.textContent='';
  }
}



for (var i = 0; i < all.length; i++) {

  all[i].addEventListener('click',Chango)
  
  console.log("nigama");
}
