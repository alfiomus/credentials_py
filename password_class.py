class password_validar():

    errors=[]

    def longitud(self, passw):
        if len(passw) < 8:
            self.errors.append('La contrasena debe tener al menos 8 caracteres')
            return False
        else:
            return True

    def minuscula(self, passw):
        letras_minuscula=False
        for carac in passw:
            if carac.islower()==True:
                letras_minuscula=True
        if not letras_minuscula:
            self.errors.append('La contrasena debe tener al menos una minuscula')
            return False
        else:
            return True

    def mayuscula(self, passw):
        letras_mayuscula=False
        for carac in passw:
            if carac.isupper()==True:
                letras_mayuscula=True
        if not letras_mayuscula:
            self.errors.append('La contrasena debe tener al menos una mayuscula')
            return False
        else:
            return True

    def numero(self, passw):
        num=False
        for carac in passw:
            if carac.isdigit()== True:
                num=True

        if not num:
            self.errors.append('La contrasena debe tener al menos un numero')
            return False
        else:
            return True

    def no_alfanumerico(self, passw):
        if passw.isalnum()==True:
            self.errors.append('La contrasena debe tener al menos un caracter no alfanumerico')
            return False
        else:
            return True

    def espacios(self, passw):
        if passw.count(" ")> 0:
            self.errors.append('La contrasena no puede contener espacios en blanco')
            return False
        else:
            return True

    def validar_password(self,passw):
        valido=self.longitud(passw) and self.minuscula(passw) and self.mayuscula(passw) and self.numero(passw) and self.no_alfanumerico(passw) and self.espacios(passw)
        return valido