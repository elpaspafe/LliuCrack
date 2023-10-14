#!/usr/bin/expect

# Variables
set host "tu-servidor-ssh.com"
set user "tu-usuario"
set password "tu-contrasena"

# Conexión SSH
spawn ssh $user@$host

# Espera a que aparezca el prompt de la contraseña y luego envía la contraseña
expect "password: "
send "$password\r"

# Ahora estás conectado y puedes ejecutar comandos SSH
interact
