from flask import Flask
app=Flask("test")

@app.route("/")
def test_home():
    return "You have reached the home directory"

if __name__ == "__main__":
    app.run(host="127.0.0.1",port="9091")