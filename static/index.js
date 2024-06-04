function copyFunction()
{
    var copyText = document.getElementById("url_copy").innerHTML;

    navigator.clipboard.writeText(copyText);
}