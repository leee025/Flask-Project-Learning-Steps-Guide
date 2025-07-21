from flask import render_template, flash, redirect, url_for, request, jsonify
from app.user import bp  # 更新導入路徑
from app.models.users import User
from app import db
from typing import Union

@bp.route('/list')
def user_list():
    """
    显示用户列表页面
    
    查询所有用户并渲染用户列表模板
    
    Returns:
        str: 渲染后的HTML页面
    """
    # 查询所有用户记录
    users = User.query.all()
    return render_template('user/list.html', users=users)

@bp.route('/create', methods=['GET', 'POST'])
def create_user():
    """
    创建新用户
    
    GET请求：显示创建用户表单
    POST请求：处理表单提交，创建新用户
    
    Returns:
        str: 渲染后的HTML页面或重定向响应
    """
    if request.method == 'POST':
        # 从表单获取用户输入数据
        username: str = request.form.get('username')
        email: str = request.form.get('email')
        password: str = request.form.get('password')
        
        # 检查用户名是否已存在
        existing_user: Union[User, None] = User.query.filter_by(username=username).first()
        if existing_user:
            flash('用户名已存在')
            return redirect(url_for('user.create_user'))
            
        # 检查邮箱是否已被注册
        existing_email: Union[User, None] = User.query.filter_by(email=email).first()
        if existing_email:
            flash('邮箱已被注册')
            return redirect(url_for('user.create_user'))
        
        # 创建新用户实例
        user: User = User(username=username, email=email)
        user.set_password(password)
        
        # 保存到数据库
        db.session.add(user)
        db.session.commit()
        
        flash('用户创建成功！')
        return redirect(url_for('user.user_list'))
    
    # GET请求，显示创建用户表单
    return render_template('user/create.html')

@bp.route('/<int:id>')
def user_detail(id: int):
    """
    显示用户详情页面
    
    Args:
        id (int): 用户ID
        
    Returns:
        str: 渲染后的HTML页面
        
    Raises:
        404: 如果用户不存在
    """
    # 根据ID查询用户，如果不存在则返回404
    user: User = User.query.get_or_404(id)
    return render_template('user/detail.html', user=user)

@bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_user(id: int):
    """
    编辑用户信息
    
    GET请求：显示编辑用户表单
    POST请求：处理表单提交，更新用户信息
    
    Args:
        id (int): 用户ID
        
    Returns:
        str: 渲染后的HTML页面或重定向响应
        
    Raises:
        404: 如果用户不存在
    """
    # 根据ID查询用户，如果不存在则返回404
    user: User = User.query.get_or_404(id)
    
    if request.method == 'POST':
        # 从表单获取更新数据
        username: str = request.form.get('username')
        email: str = request.form.get('email')
        password: str = request.form.get('password')
        
        # 检查用户名是否被其他用户使用
        existing_user: Union[User, None] = User.query.filter_by(username=username).first()
        if existing_user and existing_user.id != user.id:
            flash('用户名已存在')
            return redirect(url_for('user.edit_user', id=id))
            
        # 检查邮箱是否被其他用户使用
        existing_email: Union[User, None] = User.query.filter_by(email=email).first()
        if existing_email and existing_email.id != user.id:
            flash('邮箱已被注册')
            return redirect(url_for('user.edit_user', id=id))
        
        # 更新用户信息
        user.username = username
        user.email = email
        
        # 只有提供密码时才更新密码
        if password:
            user.set_password(password)
        
        # 提交更改到数据库
        db.session.commit()
        flash('用户信息更新成功！')
        return redirect(url_for('user.user_detail', id=id))
    
    # GET请求，显示编辑表单
    return render_template('user/edit.html', user=user)

@bp.route('/<int:id>/delete', methods=['POST'])
def delete_user(id: int):
    """
    删除用户
    
    Args:
        id (int): 要删除的用户ID
        
    Returns:
        Response: 重定向到用户列表页面
        
    Raises:
        404: 如果用户不存在
    """
    # 根据ID查询用户，如果不存在则返回404
    user: User = User.query.get_or_404(id)
    
    # 从数据库中删除用户
    db.session.delete(user)
    db.session.commit()
    
    flash('用户删除成功！')
    return redirect(url_for('user.user_list'))