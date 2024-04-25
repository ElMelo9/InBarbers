import bcrypt


class Security:

    # Hashear la contraseña antes de almacenarla en la base de datos
    def hash_password(self,password: str) -> str:
        # Genera un hash con un costo predeterminado
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    # Verificar la contraseña con el hash almacenado
    def verify_password(self,password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))