document.getElementById('logForm').addEventListener('submit', login);

function login(e) {
  e.preventDefault();
  var user = getInputValues('user');
  var password = getInputValues('password');
  signIn(user, password);
}
function signIn(user, password) {
  var x = false;
  var users = ["TAF100112H1A", "PST1205156S0", "JXA0004269K14"];
  var passwords = ["TAF100112H1A", "PST1205156S0", "JXA0004269K14"];
  for (var i = 0; i < users.length; i++) {
    if (user == users[i]){
      if (password == passwords[i]){
        x = true;
        window.location = "reto_konfio.html?user="+user
      }
    }
  }
  if (!x) {
    alert("Acceso Invalido");
  }
}

function getInputValues(id) {
  return document.getElementById(id).value;
}
