from flask import Flask, render_template, request, redirect, url_for
from models import db, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

db.init_app(app)

with app.app_context():
    db.create_all()  # Create database tables


@app.before_request
def method_override():
    if request.method == 'POST' and '_method' in request.form:
        method = request.form['_method'].upper()
        if method in ['PUT', 'DELETE', 'PATCH']:
            request.environ['REQUEST_METHOD'] = method


@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=['POST'])
def create():
    try:
        title = request.form['title']
        content = request.form['content']

        if not title or not content:
            raise ValueError("Title and content cannot be empty")

        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()

        # Render the new post as HTML
        return render_template('post_snippet.html', post=new_post)
    except Exception as e:
        print(f"Error occurred: {e}")
        db.session.rollback()
        return '', 500  # Return an error response


@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        return redirect(url_for('post', post_id=post.id))
    return render_template('edit_post.html', post=post)


@app.route('/delete/<int:post_id>', methods=['POST', 'DELETE'])
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return '<div id="post-{}"></div>'.format(post_id)


if __name__ == '__main__':
    app.run(debug=True)
