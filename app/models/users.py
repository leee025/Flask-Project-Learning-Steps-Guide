from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """
    用户模型类
    
    用于存储用户的基本信息，包括用户名、邮箱和密码哈希值
    """
    # 用户ID，主键，自动递增
    id = db.Column(db.Integer, primary_key=True)
    
    # 用户名，字符串类型，最大长度80，唯一且不能为空
    username = db.Column(db.String(80), unique=True, nullable=False)
    
    # 邮箱地址，字符串类型，最大长度120，唯一且不能为空
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    # 密码哈希值，字符串类型，最大长度128
    password_hash = db.Column(db.String(128))
    
    def set_password(self, password: str) -> None:
        """
        设置用户密码
        
        Args:
            password (str): 明文密码
            
        Returns:
            None
        """
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password: str) -> bool:
        """
        验证用户密码
        
        Args:
            password (str): 待验证的明文密码
            
        Returns:
            bool: 密码正确返回True，否则返回False
        """
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self) -> str:
        """
        用户对象的字符串表示
        
        Returns:
            str: 用户对象的字符串表示形式
        """
        return f'<User {self.username}>'
