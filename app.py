# app.py

from flask import Flask, render_template, request, redirect, url_for
from complex import generate_complex_image

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    image_path = None
    error_message = None
    if request.method == "POST":
        function_str = request.form.get("function")
        try:
            # Generate the complex function image with error handling
            image_path = generate_complex_image(function_str)
        except Exception as e:
            # Catch any errors and pass them to the template
            error_message = f"An error occurred: {str(e)}"

    return render_template("index.html", image_path=image_path, error_message=error_message)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
