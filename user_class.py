class usuario_validar():
    
    errors=[]
    
    def longitud(self,username):
        if len(username)<6:
            self.errors.append('El nombre de usuario debe contener al menos 6 caracteres')
            return False

        elif len(username)>12:
            self.errors.append('El nombre de usuario debe contener maximo 12 caracteres')
            return False

        else:
            return True
    
    def alfanumerico(self,username):
        if username.isalnum()==False:
            self.errors.append('El nombre de usuario puede contener solo letras y numeros')
            return False
        else:
            return True

    def validar_usuario(self,username):
        valido=self.longitud(username) and self.alfanumerico(username)
        return valido