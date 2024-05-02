function afficher(e){
    var affichage=document.getElementById('ecrire')
    var textefruit=e.currentTarget.textContent
    affichage.textContent="vous avez choisi : "+textefruit
}
var monfruit=document.getElementsByClassName('fruit')
for (let i=0; i<monfruit.length; i++){
monfruit[i].addEventListener('click',afficher,false)
}