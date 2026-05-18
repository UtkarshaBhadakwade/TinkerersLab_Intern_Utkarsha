function toggleMenu(){
    let sidebar = document.getElementById("sidebar");

    if(sidebar.style.left === "0px"){
        sidebar.style.left = "-250px";
    }else{
        sidebar.style.left = "0px";
    }
}

function scrollDown(){
    window.scrollBy({
        top: window.innerHeight,
        behavior: "smooth"
    });
}
function scrollDown(){
    document.getElementById("overview")
        .scrollIntoView({ behavior: "smooth" });
}