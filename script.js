function toggleMenu(){
    let sidebar = document.getElementById("sidebar");

    if(sidebar.style.left === "0px"){
        sidebar.style.left = "-250px";
    } else {
        sidebar.style.left = "0px";
    }
}

function scrollDown(){
    document.getElementById("overview")
    .scrollIntoView({ behavior: "smooth" });
}

function toggleWeek(element){
    let content = element.querySelector(".week-content");

    if(content.style.display === "block"){
        content.style.display = "none";
    } else {
        content.style.display = "block";
    }
}