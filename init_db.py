from app import create_app, db
from app.models.users import User

def init_database() -> None:
    """
    初始化数据库函数
    
    创建数据库表并添加测试数据
    
    Returns:
        None
    """
    # 创建应用实例
    app = create_app()
    
    with app.app_context():
        # 创建所有数据库表
        db.create_all()
        print("数据库表创建成功！")
        
        # 检查是否已存在用户，如果没有则创建测试用户
        existing_user: User = User.query.first()
        if not existing_user:
            # 创建管理员测试用户
            test_user: User = User(username='admin', email='admin@example.com')
            test_user.set_password('admin123')
            
            # 保存到数据库
            db.session.add(test_user)
            db.session.commit()
            print("创建了测试用户: admin / admin123")

if __name__ == '__main__':
    init_database()
