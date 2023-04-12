from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]


@app.route("/openai-api", methods=["GET"])
def openai_api():
    # Get prompt from request parameter
    prompt = request.args.get("prompt")

    # Call OpenAI API with prompt
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Return API response as JSON
    return jsonify(response.choices[0].text)


if __name__ == "__main__":
    app.run(debug=True)
