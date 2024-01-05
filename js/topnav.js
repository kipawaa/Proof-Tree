function home() {
    var contentDivs = document.getElementsByClassName('content')[0].getElementsByTagName('div');
    for (var i = 0; i < contentDivs.length; i++) {
        contentDivs[i].style.display = 'none';
    }
    document.getElementsById('tree').style.display = "block";
}
