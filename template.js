function showContent(contentId) {
    var contentDivs = document.getElementsByClassName('content')[0].getElementsByTagName('div');
    for (var i = 0; i < contentDivs.length; i++) {
        contentDivs[i].style.display = 'none';
    }
    document.getElementById(contentId).style.display = 'block';
}
