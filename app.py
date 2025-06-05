from flask import Flask, request

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return '''
    <h1>Welcome to My Portfolio</h1>
    <p>Hello! I'm a virtual intern at TECHSONIX. Below are the sections of my site:</p>
    <a href="/about">About Me</a> | 
    <a href="/projects">Projects</a> | 
    <a href="/contact">Contact</a>
    '''

# About Page
@app.route('/about')
def about():
    return '''
    <h1>About Me</h1>
    <p>I am a beginner Python programmer exploring web development using Flask at TECHSONIX.I am pursuading my Btech degree from Kashi Institute of Technology,Mirzamurad,Uttar Pradesh.My core branch is Computer Science and Engineering(Artificial Intelligence and Machine Learning.</p>
    <a href="/">Back to Home</a>
    '''

# Projects Page
@app.route('/projects')
def projects():
    return '''
    <h1>My Projects</h1>
    <ul>
        <li><strong>Portfolio Website</strong> – Built using Flask</li>
        <li><strong>Calculator </strong> – Simple calculator in Python</li>
        <li><strong>Password generator </strong> – using python</li>
    </ul>
    <a href="/">Back to Home</a>
    '''

# Contact Page with Form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        return f'''
        <h1>Thank You!</h1>
        <p>Hi <b>{name}</b>, your message has been received.</p>
        <blockquote>{message}</blockquote>
        <a href="/">Back to Home</a>
        '''
    
    return '''
    <h1>Contact Me</h1>
    <form method="post">
        <label>Name:</label><br>
        <input type="text" name="name" required><br><br>
        
        <label>Message:</label><br>
        <textarea name="message" rows="5" cols="40" required></textarea><br><br>
        
        <input type="submit" value="Send">
    </form>
    <a href="/">Back to Home</a>
    '''

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
