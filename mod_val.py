# -*- coding: utf-8 -*-

import usuario  as uv
import password as pv

user_validator = uv.usuario_validar()
pass_validator = pv.password_validar()

correcto= False

while correcto==False:
    nombre = raw_input('Ingrese su nombre de usuario: ')
    if not user_validator.validar_usuario(nombre):
        for error in user_validator.errors:
            print error
            correcto=False
            user_validator.errors.remove(error)           
    else:
        correcto=True
            
while correcto==True:        
    passwd = raw_input('Ingrese su contraseña: ')
    if not pass_validator.validar_password(passwd):
        for error in pass_validator.errors:
            print error
            correcto=True
            pass_validator.errors.remove(error)
    else:
        correcto=False