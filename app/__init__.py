# app/__init__.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config
import os

# 创建SQLAlchemy数据库实例
db = SQLAlchemy()

# 创建Flask-Migrate迁移实例
migrate = Migrate()

def create_app(config_name: str = None) -> Flask:
    """
    应用工厂函数
    
    创建并配置Flask应用实例
    
    Args:
        config_name (str, optional): 配置名称，默认从环境变量获取
        
    Returns:
        Flask: 配置好的Flask应用实例
    """
    # 如果未指定配置名称，从环境变量获取，默认为'default'
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')
    
    # 创建Flask应用实例
    app = Flask(__name__)
    
    # 从配置对象加载配置
    app.config.from_object(config[config_name])
    
    # 初始化扩展
    db.init_app(app)
    migrate.init_app(app, db)
    
    # 导入模型以确保它们被SQLAlchemy识别
    from app.models.users import User
    
    # 在应用上下文中创建数据库表
    with app.app_context():
        db.create_all()
    
    # 注册认证蓝图
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    # 注册用户管理蓝图
    from app.user import bp as user_bp
    app.register_blueprint(user_bp, url_prefix='/user')
    
    @app.route('/')
    def index() -> str:
        """
        首页路由
        
        显示应用首页，包含用户统计信息
        
        Returns:
            str: 渲染后的HTML页面
        """
        # 统计注册用户总数
        user_count: int = User.query.count()
        return render_template('index.html', user_count=user_count)
    
    return app
