
function showItems(){
    let items = document.getElementById("items")
    let services = document.getElementById("services")
    let biz = document.getElementById("biz")
    let elements = document.getElementsByClassName("tab")
    items.style.display = "grid"
    services.style.display = "none"
    biz.style.display = "none"
    for (let index = 0; index < elements.length; index++) {
        const element = elements[index];
        if(element.id == "itemtab"){
            element.classList.add("selected")
        } else {
            element.classList.remove("selected")
        }
    }
}
function showServices(){
    let items = document.getElementById("items")
    let services = document.getElementById("services")
    let biz = document.getElementById("biz")
    let elements = document.getElementsByClassName("tab")
    items.style.display = "none"
    services.style.display = "grid"
    biz.style.display = "none"
    for (let index = 0; index < elements.length; index++) {
        const element = elements[index];
        if(element.id == "servicetab"){
            element.classList.add("selected")
        } else {
            element.classList.remove("selected")
        }
    }
}
function showBiz(){
    let items = document.getElementById("items")
    let services = document.getElementById("services")
    let biz = document.getElementById("biz")
    let elements = document.getElementsByClassName("tab")
    items.style.display = "none"
    services.style.display = "none"
    biz.style.display = "grid"
    for (let index = 0; index < elements.length; index++) {
        const element = elements[index];
        if(element.id == "biztab"){
            element.classList.add("selected")
        } else {
            element.classList.remove("selected")
        }
    }
}