from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def set_cookies():
    # Create a response object
    response = make_response("Cookies are set!")
    
    # Set a session cookie (temporary)
    response.set_cookie('session_cookie', 'temporary_value')
    
    # Set a persistent cookie (permanent)
    response.set_cookie('permanent_cookie', 'permanent_value', max_age=60*60*24*30)  # Expires in 30 days
    
    return response

@app.route('/get_cookies')
def get_cookies():
    # Retrieve cookies from the request
    session_cookie = request.cookies.get('session_cookie')
    permanent_cookie = request.cookies.get('permanent_cookie')
    
    return f"Session Cookie: {session_cookie}, Permanent Cookie: {permanent_cookie}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
