from flask import Blueprint, request, jsonify
from function_jwt import validate_token
palindromo = Blueprint("palindromo", __name__)

@palindromo.before_request
def verify_token_middleware():
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token,output=False)

@palindromo.route("/palindromo", methods=["POST"])
def palindromo_calculo():
    word = {
        "word": request.json['word']
    }
    maxstr = []
    for i in range(0, len(word['word'])):
        for j in range(0, len(word['word'])):
            substr = word['word'][i:j+1]
            if str(substr) == "".join(reversed(substr)) and substr !="":
                maxstr.append(substr)
            else:
                continue
    return jsonify({"El palindromo de la subcadena mas larga es ": max(maxstr, key=len)})
