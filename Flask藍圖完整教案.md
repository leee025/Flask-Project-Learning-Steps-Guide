# Flask藍圖(Blueprint)完整教案

## 🎯 什麼是Flask藍圖？

Flask藍圖是一種組織Flask應用程式的方式，它允許你將相關的路由、視圖函數、模板和靜態文件組織在一起，形成一個可重用的組件。

### 為什麼需要藍圖？
```python
# 沒有藍圖的問題：所有路由都在一個文件中
@app.route('/login')
@app.route('/register')
@app.route('/user/list')
@app.route('/user/create')
@app.route('/admin/dashboard')
@app.route('/admin/users')
# ... 數百個路由，難以維護！
```

## 🏗️ 藍圖的核心概念

### 1. 藍圖的定義
```python
from flask import Blueprint

# 創建藍圖
bp = Blueprint(
    'auth',           # 藍圖名稱
    __name__,         # 模組名稱
    url_prefix='/auth', # URL前綴（可選）
    template_folder='templates',  # 模板文件夾（可選）
    static_folder='static'        # 靜態文件夾（可選）
)
```

### 2. 藍圖的註冊
```python
# 在應用工廠中註冊藍圖
def create_app():
    app = Flask(__name__)
    
    # 註冊藍圖
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    return app
```

## 📁 本專案的藍圖架構分析

### 認證藍圖 (app/auth/)
```
app/auth/
├── __init__.py     # 藍圖定義和初始化
└── routes.py       # 路由和視圖函數
```

#### 藍圖初始化 (app/auth/__init__.py)
```python
from flask import Blueprint

# 創建認證藍圖
bp = Blueprint('auth', __name__)

# 導入路由（避免循環導入）
from app.auth import routes
```

#### 路由定義 (app/auth/routes.py)
```python
from app.auth import bp  # 導入藍圖實例

@bp.route('/login', methods=['GET', 'POST'])
def login():
    # 登入邏輯
    pass

@bp.route('/register', methods=['GET', 'POST'])
def register():
    # 註冊邏輯
    pass

@bp.route('/logout')
def logout():
    # 登出邏輯
    pass
```

### 用戶管理藍圖 (app/models/user/)
```
app/models/user/
├── __init__.py     # 藍圖定義
└── routes.py       # CRUD路由
```

## 🔄 藍圖的工作流程

### 1. 創建階段
```python
# Step 1: 創建藍圖實例
bp = Blueprint('user', __name__)

# Step 2: 定義路由
@bp.route('/list')
def user_list():
    return "用戶列表"
```

### 2. 註冊階段
```python
# Step 3: 在應用中註冊藍圖
app.register_blueprint(user_bp, url_prefix='/user')
```

### 3. 運行階段
```
用戶訪問: /user/list
    ↓
Flask路由系統匹配
    ↓
找到user藍圖的list路由
    ↓
執行user_list()函數
    ↓
返回響應
```

## 🛠️ 藍圖的高級特性

### 1. URL前綴
```python
# 註冊時指定前綴
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/user')

# 結果：
# /auth/login
# /auth/register
# /user/list
# /user/create
```

### 2. 模板文件夾
```python
# 藍圖可以有自己的模板文件夾
bp = Blueprint('auth', __name__, template_folder='templates')

# 模板結構
templates/
├── auth/
│   ├── login.html
│   └── register.html
└── base.html
```

### 3. 靜態文件
```python
# 藍圖可以有自己的靜態文件
bp = Blueprint('auth', __name__, static_folder='static')

# 靜態文件結構
static/
├── auth/
│   ├── css/
│   └── js/
└── common/
```

## 📊 本專案藍圖詳細分析

### 認證藍圖功能映射
```
URL路徑                    視圖函數        功能描述
/auth/login               login()         用戶登入
/auth/register            register()      用戶註冊
/auth/logout              logout()        用戶登出
```

### 用戶管理藍圖功能映射
```
URL路徑                    視圖函數           功能描述
/user/list                user_list()       用戶列表
/user/create              create_user()     創建用戶
/user/<id>                user_detail()     用戶詳情
/user/<id>/edit           edit_user()       編輯用戶
/user/<id>/delete         delete_user()     刪除用戶
```

## 🔧 藍圖最佳實踐

### 1. 文件組織結構
```
推薦結構：
app/
├── auth/                 # 認證模組
│   ├── __init__.py
│   ├── routes.py
│   └── forms.py         # 表單定義（可選）
├── user/                 # 用戶管理模組
│   ├── __init__.py
│   └── routes.py
└── main/                 # 主要頁面模組
    ├── __init__.py
    └── routes.py
```

### 2. 命名規範
```python
# 藍圖命名：使用模組功能名稱
auth_bp = Blueprint('auth', __name__)
user_bp = Blueprint('user', __name__)
admin_bp = Blueprint('admin', __name__)

# 路由命名：使用動詞+名詞
@bp.route('/create')      # 創建
@bp.route('/list')        # 列表
@bp.route('/<id>/edit')   # 編輯
@bp.route('/<id>/delete') # 刪除
```

### 3. 循環導入避免
```python
# 正確的導入順序
# __init__.py
from flask import Blueprint
bp = Blueprint('auth', __name__)
from app.auth import routes  # 在藍圖創建後導入

# routes.py
from app.auth import bp      # 導入藍圖實例
```

## 🎨 模板中的藍圖使用

### URL生成
```html
<!-- 使用藍圖名稱.函數名稱 -->
<a href="{{ url_for('auth.login') }}">登入</a>
<a href="{{ url_for('auth.register') }}">註冊</a>
<a href="{{ url_for('user.user_list') }}">用戶列表</a>
<a href="{{ url_for('user.create_user') }}">創建用戶</a>
```

### 條件顯示
```html
<!-- 根據用戶狀態顯示不同連結 -->
{% if session.get('user_id') %}
    <a href="{{ url_for('user.user_list') }}">用戶列表</a>
    <a href="{{ url_for('auth.logout') }}">登出</a>
{% else %}
    <a href="{{ url_for('auth.login') }}">登入</a>
    <a href="{{ url_for('auth.register') }}">註冊</a>
{% endif %}
```

## 🚀 擴展藍圖功能

### 1. 添加新的藍圖
```python
# 創建API藍圖
# app/api/__init__.py
from flask import Blueprint
bp = Blueprint('api', __name__)
from app.api import routes

# app/api/routes.py
from flask import jsonify
from app.api import bp

@bp.route('/users')
def get_users():
    return jsonify({'users': []})

# 註冊API藍圖
app.register_blueprint(api_bp, url_prefix='/api')
```

### 2. 藍圖中間件
```python
# 藍圖級別的請求處理
@bp.before_request
def require_login():
    if not session.get('user_id'):
        return redirect(url_for('auth.login'))

@bp.after_request
def after_request(response):
    # 請求後處理
    return response
```

### 3. 錯誤處理
```python
# 藍圖級別的錯誤處理
@bp.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404

@bp.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500
```

## 📝 實作練習

### 練習1：創建管理員藍圖
```python
# 任務：創建一個管理員藍圖，包含以下功能：
# - 管理員登入
# - 用戶管理
# - 系統設置

# 1. 創建 app/admin/__init__.py
# 2. 創建 app/admin/routes.py
# 3. 在應用中註冊藍圖
# 4. 創建相應的模板
```

### 練習2：API藍圖
```python
# 任務：創建一個RESTful API藍圖
# - GET /api/users (獲取用戶列表)
# - POST /api/users (創建用戶)
# - GET /api/users/<id> (獲取用戶詳情)
# - PUT /api/users/<id> (更新用戶)
# - DELETE /api/users/<id> (刪除用戶)
```

## 🔍 常見問題與解決方案

### 1. 循環導入問題
```python
# 問題：ImportError: cannot import name 'bp'
# 解決：確保導入順序正確

# 錯誤方式
from app.auth.routes import bp  # ❌

# 正確方式
from flask import Blueprint
bp = Blueprint('auth', __name__)
from app.auth import routes     # ✅
```

### 2. URL前綴衝突
```python
# 問題：多個藍圖使用相同的URL前綴
app.register_blueprint(user_bp, url_prefix='/admin')
app.register_blueprint(admin_bp, url_prefix='/admin')  # 衝突！

# 解決：使用不同的前綴
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(admin_bp, url_prefix='/admin')
```

### 3. 模板找不到
```python
# 問題：TemplateNotFound
# 解決：檢查模板路徑配置

# 方法1：指定模板文件夾
bp = Blueprint('auth', __name__, template_folder='templates')

# 方法2：使用相對路徑
return render_template('auth/login.html')
```

## 📚 總結

Flask藍圖是組織大型應用程式的重要工具，它提供了：

1. **模組化**：將相關功能組織在一起
2. **可重用性**：藍圖可以在多個應用中重用
3. **可維護性**：代碼結構清晰，易於維護
4. **團隊協作**：不同團隊成員可以負責不同的藍圖

通過本專案的實例，你可以看到藍圖如何將認證功能和用戶管理功能分離，使代碼更加組織化和可維護。這種模式在大型Flask應用中是必不可少的。