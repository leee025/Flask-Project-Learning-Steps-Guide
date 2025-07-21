import os
from dotenv import load_dotenv

# 获取项目根目录的绝对路径
basedir: str = os.path.abspath(os.path.dirname(__file__))

# 加载环境变量文件
load_dotenv()

class Config:
    """
    基础配置类
    
    包含所有环境共用的配置项
    """
    # 应用密钥，用于会话加密等安全功能
    SECRET_KEY: str = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    
    # 数据库连接URI
    SQLALCHEMY_DATABASE_URI: str = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    
    # 禁用SQLAlchemy事件系统的修改跟踪功能以节省内存
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

class DevelopmentConfig(Config):
    """
    开发环境配置类
    
    继承基础配置，添加开发环境特定的配置
    """
    # 启用调试模式
    DEBUG: bool = True

class ProductionConfig(Config):
    """
    生产环境配置类
    
    继承基础配置，添加生产环境特定的配置
    """
    # 禁用调试模式
    DEBUG: bool = False

class TestingConfig(Config):
    """
    测试环境配置类
    
    继承基础配置，添加测试环境特定的配置
    """
    # 启用测试模式
    TESTING: bool = True
    
    # 使用内存数据库进行测试
    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///:memory:'

# 配置字典，用于根据环境名称获取对应的配置类
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
