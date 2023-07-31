function myFunction() {
  var x = document.getElementById("password");
  icon = document.querySelector("i.icon");
  if (x.type === "password") {
    x.type = "text";
    icon.classList.remove("icon-eye")
    icon.classList.add("icon-eye-blocked")
  } else {
    x.type = "password";
    icon.classList.add("icon-eye")
  	icon.classList.remove("icon-eye-blocked")
  }
} 
