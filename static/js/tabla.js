document.addEventListener("keyup", e=>{

  if (e.target.matches("#buscador")){

      if (e.key ==="Escape")e.target.value = ""

  document.querySelectorAll(".articulo").forEach(item =>{

      item.textContent.toLowerCase().includes(e.target.value.toLowerCase())
        ?item.classList.remove("filtro")
        :item.classList.add("filtro")
  })
  }

})