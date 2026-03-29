"""Flask web application for emotion detection using Watson NLP."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

# Create Flask app and define template/static folders
app = Flask(
    __name__,
    template_folder="oaqjp-final-project-emb-ai/templates",
    static_folder="oaqjp-final-project-emb-ai/static"
)


@app.route("/")
def home():
    """Render the main page (index.html)."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Handle emotion detection requests and return formatted response.

    Retrieves text from the query parameter, calls the emotion_detector
    function from the EmotionDetection package, and returns a formatted
    message. If input is blank or invalid, returns an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if result is None or result.get("dominant_emotion") is None:
        return "Invalid text! Please try again."

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
