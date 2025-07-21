# app/auth/routes.py
from flask import render_template, flash, redirect, url_for, request, session
from app.auth import bp
from app.models.users import User
from app import db
from typing import Union

@bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    用户登录功能
    
    GET请求：显示登录表单
    POST请求：处理登录验证
    
    Returns:
        str: 渲染后的HTML页面或重定向响应
    """
    if request.method == 'POST':
        # 从表单获取登录凭据
        username: str = request.form.get('username')
        password: str = request.form.get('password')
        
        # 根据用户名查询用户
        user: Union[User, None] = User.query.filter_by(username=username).first()
        
        # 验证用户存在且密码正确
        if user is None or not user.check_password(password):
            flash('用户名或密码错误')
            return redirect(url_for('auth.login'))
        
        # 登录成功，将用户ID存储到会话中
        session['user_id'] = user.id
        flash('登录成功！')
        return redirect(url_for('index'))
    
    # GET请求，显示登录表单
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    """
    用户登出功能
    
    清除会话中的用户信息并重定向到首页
    
    Returns:
        Response: 重定向到首页
    """
    # 从会话中移除用户ID
    session.pop('user_id', None)
    flash('已成功登出')
    return redirect(url_for('index'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    用户注册功能
    
    GET请求：显示注册表单
    POST请求：处理用户注册
    
    Returns:
        str: 渲染后的HTML页面或重定向响应
    """
    if request.method == 'POST':
        # 从表单获取注册信息
        username: str = request.form.get('username')
        email: str = request.form.get('email')
        password: str = request.form.get('password')
        
        # 检查用户名是否已被使用
        existing_user: Union[User, None] = User.query.filter_by(username=username).first()
        print(type(existing_user))
        if existing_user: # 等價於 if existing_user is not None
            flash(f'用户名已被使用:{username}')
            return redirect(url_for('auth.register'))
        
        # 检查邮箱是否已被注册
        existing_email: Union[User, None] = User.query.filter_by(email=email).first()
        if existing_email:
            flash('邮箱已被注册')
            return redirect(url_for('auth.register'))
        
        # 创建新用户
        user: User = User(username=username, email=email)
        user.set_password(password)
        
        # 保存到数据库
        db.session.add(user)
        db.session.commit()
        
        flash('注册成功！请登录。')
        return redirect(url_for('auth.login'))
    
    # GET请求，显示注册表单
    return render_template('auth/register.html')
