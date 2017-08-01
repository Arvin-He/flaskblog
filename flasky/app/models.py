from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    #...
    password_hash = db.Column(db.String(128))
    
    @property
    def password(self):
        raise ArithmeticError('password is not a readsble attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    