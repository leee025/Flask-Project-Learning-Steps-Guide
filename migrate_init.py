from flask_migrate import init, migrate, upgrade
from app import create_app, db

app = create_app()

with app.app_context():
    # 初始化迁移
    init()
    print("迁移仓库初始化完成")
    
    # 创建第一个迁移
    migrate(message='Initial migration')
    print("创建初始迁移文件")
    
    # 应用迁移
    upgrade()
    print("应用迁移完成")