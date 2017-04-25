from flask import Flask, render_template
import os


app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run()
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)

