function carrés_nb() {
    var affichage = document.getElementsByClassName('nombre') ;
    for (let i=0; i<affichage.length; i++){
        var cellule_cont=i+1
        affichage[i].textContent = cellule_cont**2
    }
    }
    var carrés=document.getElementById('carrés') ;
    carrés.addEventListener ('click' , function() {
    carrés_nb() ;
    }) ;


function multiples_recherche() {
    var nb_cont = document.getElementsByClassName('nombre') ;
    var tonmultiple=document.getElementById('multiplechoisi').value;
    for (let i=0; i<100; i++){
        if ((i+1)%tonmultiple==0){
            nb_cont[i].className = 'nombre multiple'
        }
    }
    }
    var multiples=document.getElementById('multiples') ;
    multiples.addEventListener ('click' , function() {
    multiples_recherche() ;
    }) ;


function getRandomInt(min,max){
    const minCeiled=Math.ceil(min);
    const maxFloored=Math.floor(max);
    return Math.floor(Math.random()*(maxFloored-minCeiled)+minCeiled);
}
function generer(){
    var remplacementalea= document.getElementsByClassName('nombre')
    for(let i=0; i<remplacementalea.length;i++){
        var nombrealea=getRandomInt(1,100)
        remplacementalea[i].textContent=nombrealea
    }
}
    var genereralea=document.getElementById('alea') ;
    genereralea.addEventListener ('click' , function() {
    generer() ;
    }) ;

function triselection(){
    var tabatrier=document.getElementsByClassName('nombre')
    var minstock=0
    for(let i=0; i<tabatrier.length-1; i++){
        var mintri=i
        for(let j=i+1; j<tabatrier.length; j++){
            if(parseInt(tabatrier[j].textContent)<parseInt(tabatrier[mintri].textContent)){
                mintri=j
            }
        }
        minstock=tabatrier[mintri].textContent
        tabatrier[mintri].textContent=tabatrier[i].textContent
        tabatrier[i].textContent=minstock
    }
}
    var trier=document.getElementById('tri') ;
    trier.addEventListener ('click' , function() {
    triselection() ;
    }) ;