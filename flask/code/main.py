from flask import Flask
import flask
import Levenshtein
from main_qroq import *

app = Flask(__name__)

@app.route("/<request>")
def index(request):

    def grab_jaro_winkler(word1: str, word2: str) -> float:
        return Levenshtein.jaro_winkler(word1, word2)

    data = get_data()
    data = map( lambda x: {
        **x,
        "score" : grab_jaro_winkler(request, x["md_chapter"])
    }, data )

    search_result = sorted(data, key= lambda x : x["score"], reverse=True)[:5]

    data_prompt = "\n\n------------------------------------------\n".join(map(
        lambda row: f"""
    {row["md_file_path"]}

    {row["md_chapter"]}

    """, search_result ))


    user_prompt2 = f"""
    以下は相談内容です。
    （日本語でお願いします）

    {request}

    この問題に対して、次の手法が有効であるとします。
    これらの手段を用いて、大まかな作戦を立案してください！
    （日本語でお願いします）

    {data_prompt}

    """

    print(user_prompt2)

    response = call_groq(client, system_prompt, user_prompt2)
    text = response.choices[0].message.content
    print(text)
    response = flask.jsonify({'text': text,'hints' : search_result})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)


