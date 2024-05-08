$(document).ready(function() {
    $('.clickable-tr').click(function() {
        window.location = $(this).attr('href');
        return false;
    });
});

function hoverRow(row) {
    row.style.backgroundColor = 'var(--tertiary)';
    row.style.color = 'var(--black)';
    row.style.cursor = 'pointer'
}

function unhoverRow(row) {
    row.style.backgroundColor = '';
    row.style.color = 'var(--white)';
    row.style.cursor = 'default';
}

function searchTable(tabname, searchname) {
    let noresultname = tabname + 'Res';
    let input, filter, table, tr, td, i, txtValue;
    input = document.getElementById(searchname);
    filter = input.value.toUpperCase();
    table = document.getElementById(tabname);
    tr = table.getElementsByClassName("row-to-search");
    let nbr = 0;
    for (i = 0; i < tr.length; i++) {
        let display = "none";
        for (const element of tr[i].getElementsByTagName("td")) {
            td = element;
            if (td) {
                txtValue = td.textContent || td.innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    display = "";
                    nbr++;
                }
            }
        }
        tr[i].style.display = display;
    }

    if (nbr == 0) {
        document.getElementById(noresultname).style.display = "";
        table.style.display = "none";
    } else {
        document.getElementById(noresultname).style.display = "none";
        table.style.display = "";
    }

    /*
    if (input.value != "") {
        let re = new RegExp(filter, 'gi');
        for (i = 0; i < tr.length; i++) {
            for (const element of tr[i].getElementsByTagName("td")) {
                td = element;
                if (td) {
                    txtValue = td.textContent || td.innerText;
                    td.innerHTML = txtValue.replace(re, match => `<mark>${match}</mark>`);
                }
            }
        }
    } else {
        for (i = 0; i < tr.length; i++) {
            for (const element of tr[i].getElementsByTagName("td")) {
                td = element;
                if (td) {
                    txtValue = td.textContent || td.innerText;
                    td.innerHTML = txtValue;
                }
            }
        }
    }
    */
}