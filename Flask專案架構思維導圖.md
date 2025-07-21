# Flask專案架構思維導圖

## 🏗️ 專案整體架構

```
Flask Web應用程式
├── 📁 核心配置層
│   ├── app.py (應用程式入口點)
│   ├── config.py (環境配置管理)
│   ├── .env (環境變數)
│   └── wsgi.py (部署配置)
│
├── 📁 應用程式層 (app/)
│   ├── __init__.py (應用工廠函數)
│   ├── 📁 認證模組 (auth/)
│   ├── 📁 用戶管理模組 (user/)
│   ├── 📁 數據模型 (models/)
│   └── 📁 模板層 (templates/)
│
├── 📁 數據層
│   ├── instance/app.db (SQLite數據庫)
│   ├── init_db.py (數據庫初始化)
│   └── migrate_init.py (數據遷移)
│
└── 📁 依賴管理
    ├── pyproject.toml (專案配置)
    └── uv.lock (依賴鎖定)
```

## 🔧 核心配置層詳解

### 1. 應用程式入口 (app.py)
```python
# 職責：啟動應用程式
from app import create_app
app = create_app()
```

### 2. 配置管理 (config.py)
```
配置類別架構
├── Config (基礎配置)
│   ├── SECRET_KEY
│   ├── DATABASE_URI
│   └── SQLALCHEMY_TRACK_MODIFICATIONS
│
├── DevelopmentConfig (開發環境)
├── ProductionConfig (生產環境)
└── TestingConfig (測試環境)
```

## 🏛️ 應用程式架構 (MVC模式)

### 應用工廠模式 (app/__init__.py)
```
create_app() 工廠函數
├── 1. 創建Flask實例
├── 2. 載入配置
├── 3. 初始化擴展 (SQLAlchemy, Migrate)
├── 4. 註冊藍圖 (Blueprint)
└── 5. 定義路由
```

### 藍圖架構 (Blueprint Pattern)
```
藍圖系統
├── 🔐 認證藍圖 (auth/)
│   ├── URL前綴: /auth
│   ├── 登入 (/login)
│   ├── 註冊 (/register)
│   └── 登出 (/logout)
│
└── 👤 用戶管理藍圖 (user/)
    ├── URL前綴: /user
    ├── 用戶列表 (/list)
    ├── 創建用戶 (/create)
    ├── 用戶詳情 (/<id>)
    ├── 編輯用戶 (/<id>/edit)
    └── 刪除用戶 (/<id>/delete)
```

## 📊 數據模型層

### User模型 (app/models/users.py)
```
User類別
├── 屬性
│   ├── id (主鍵)
│   ├── username (用戶名)
│   ├── email (電子郵件)
│   └── password_hash (密碼雜湊)
│
└── 方法
    ├── set_password() (設定密碼)
    ├── check_password() (驗證密碼)
    └── __repr__() (字串表示)
```

## 🎨 視圖層架構

### 模板繼承結構
```
模板系統
├── base.html (基礎模板)
│   ├── 導航欄
│   ├── 訊息閃現
│   └── 內容區塊
│
├── 📁 auth/ (認證模板)
│   ├── login.html
│   └── register.html
│
├── 📁 user/ (用戶管理模板)
│   ├── list.html
│   ├── create.html
│   ├── detail.html
│   └── edit.html
│
└── index.html (首頁)
```

## 🔄 請求處理流程

### 典型請求流程
```
用戶請求
    ↓
路由匹配 (Flask路由系統)
    ↓
藍圖處理 (Blueprint)
    ↓
視圖函數 (Controller)
    ↓
數據模型操作 (Model)
    ↓
模板渲染 (View)
    ↓
HTTP響應
```

## 🛡️ 安全機制

### 認證與授權
```
安全功能
├── 密碼雜湊 (Werkzeug)
├── 會話管理 (Flask Session)
├── CSRF保護 (SECRET_KEY)
└── 表單驗證
```

## 📦 依賴管理

### 核心依賴
```
主要套件
├── Flask (Web框架)
├── Flask-SQLAlchemy (ORM)
├── Flask-Migrate (數據庫遷移)
├── Werkzeug (密碼雜湊)
└── python-dotenv (環境變數)
```

## 🚀 部署配置

### 環境管理
```
環境配置
├── .env (環境變數)
├── .python-version (Python版本)
├── pyproject.toml (專案配置)
└── wsgi.py (WSGI入口)
```