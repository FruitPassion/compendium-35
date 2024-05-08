function searchBlocs(){
    let input = document.getElementById('searchBar').value.toLowerCase();
    let blocs = document.getElementsByClassName('blocs');
    let nbr = 0;
    for (const element of blocs) {
        let display = "none";
        if (element.textContent.toLowerCase().indexOf(input) > -1) {
            display = "";
            nbr++;
        }
        element.style.display = display;
    }
    
    let searchRes = document.getElementById('searchRes');
    if (nbr == 0) {
        searchRes.style.display = "";
    } else {
        searchRes.style.display = "none";
    }
}