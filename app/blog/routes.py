from flask import Blueprint, render_template

blog_bp = Blueprint(
    'blog',
    __name__,
    url_prefix='/blog',
    template_folder='templates'
)

@blog_bp.route('/entrada/<id>')
def entrada(id):
    return render_template('entrada.html', id=id)