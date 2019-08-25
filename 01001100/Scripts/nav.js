function navHide() {
  var x = document.getElementById("navbar");
  if (x.className === "navigation") {
    x.className += " responsive";
    document.getElementById("").innerHTML = "";
    document.getElementById("").innerHTML = "";
    document.getElementById("").innerHTML = "";
    document.getElementById("").innerHTML  = "";
  } else {
    x.className = "navigation";
    document.getElementById("").innerHTML = "";
    document.getElementById("").innerHTML = "";
    document.getElementById("").innerHTML = "";
    document.getElementById("").innerHTML  = "";
  }
}
window.onscroll = function() {stickyNav()};
function stickyNav() {
  var nav = document.getElementById("navbar");
  var sticky = nav.offsetTop;
  if (window.pageYOffset >= sticky) {
    nav.classList.add("navigation");
  } else {
    nav.classList.remove("navigation");
  }
}

var a=document.getElementsByTagName("a");
for(var i=0;i<a.length;i++){
    a[i].onclick=function(){
        window.location=this.getAttribute("href");
        return false;
    }
}
