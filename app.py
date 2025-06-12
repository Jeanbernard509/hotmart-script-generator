from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = ""  # Cle API sa ap mete sou Render pa isit la

@app.route('/', methods=['GET', 'POST'])
def index():
    script = None
    if request.method == 'POST':
        product = request.form['product']
        category = request.form['category']
        audience = request.form['audience']
        language = request.form['language']

        prompt = f"Ekri yon script TikTok pou '{product}' nan kategori '{category}', pou odyans '{audience}' an '{language}'. Li dwe kout, atiran e san vwa."

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        script = response.choices[0].text.strip()

    return render_template('index.html', script=script)

if __name__ == '__main__':
    app.run(debug=True)
