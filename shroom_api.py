from flask import Flask, url_for
import scripts.label_image as li
app = Flask(__name__)

@app.route('/predict/<path:img>')
def api_article(img):
    # Example Image = tf_files/mushroom_photos/oyster/pic_001.jpg
    result = li.predict(img)
    return result

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
