function changerfond ( ) {
var element1 = document.getElementById ( 'colonneUne') ;
element1.className = element1.className==='bleu'? 'rouge':'bleu';
}
let bouton1=document.getElementById ( 'bouton1') ;
bouton1.addEventListener ( 'click' , function () {
changerfond () ;
}) ;
