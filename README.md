# Flask專案學習步驟指南

這是一個用於學習Flask框架的示範專案，提供了完整的學習路徑和架構指南。

## 📋 專案概述

這個專案是一個基於Flask的Web應用程式，實現了用戶認證和用戶管理功能。專案採用了模組化的架構設計，使用藍圖(Blueprint)組織代碼，並遵循MVC設計模式。

## 🏗️ 專案架構

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
└── 📁 數據層
    └── instance/app.db (SQLite數據庫)
```

## 🚀 功能特點

- 用戶註冊與登入
- 用戶管理 (CRUD操作)
- 密碼安全存儲
- 模板繼承系統
- 環境配置管理

## 📚 學習資源

專案包含以下學習資源：

1. **Flask專案架構思維導圖** - 視覺化展示整個專案架構
2. **Flask專案學習步驟指南** - 11天的詳細學習計劃
3. **Flask藍圖完整教案** - 深入解釋Flask藍圖的概念和實踐
4. **Flask應用發現機制詳解** - 解釋Flask如何找到並啟動應用

## 🛠️ 安裝與運行

### 環境準備

```bash
# 克隆專案
git clone https://github.com/leee025/Flask-Project-Learning-Steps-Guide.git
cd Flask-Project-Learning-Steps-Guide

# 創建虛擬環境
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 安裝依賴
pip install -r requirements.txt
```

### 運行應用

```bash
# 初始化數據庫
python init_db.py

# 啟動應用
flask run
```

訪問 http://localhost:5000 查看應用。

## 📝 學習路徑

1. **基礎理解** (1-2天)
   - 了解專案結構
   - 理解應用工廠模式

2. **數據模型** (2-3天)
   - 掌握SQLAlchemy ORM
   - 數據庫操作實踐

3. **藍圖架構** (3-4天)
   - 理解藍圖模式
   - 認證功能實現
   - CRUD操作實現

4. **前端模板** (2-3天)
   - 模板繼承系統
   - 表單處理

5. **整合測試** (2天)
   - 功能測試
   - 代碼優化

## 📄 授權

本專案僅供學習使用。