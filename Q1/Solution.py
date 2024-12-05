from flask import Flask,render_template,url_for,request,redirect
app=Flask(__name__)
class ACM_Debugging_Competition():
    @app.route('/')
    def index():
        return "hi"
if __name__=="__main__":
    app.run(debug=False)

# Change the /hi to /
