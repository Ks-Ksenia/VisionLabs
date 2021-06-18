import base64
import os

from flask import jsonify, request, make_response

from app import app


PATH = os.path.realpath('/images/')

@app.route('/images/<path:name>.jpg')
def img_detail(name, methods=['GET']):

    path_img = os.path.join(PATH, f'{name}.jpg')

    if os.path.isfile(path_img):
        return make_response(f'<img src="{path_img}">', 200)
    else:
        return make_response('Not Found', 404)


@app.route('/image', methods=['GET'])
def img_list_get():

    list_img = os.listdir(PATH + '/')

    list_files = []

    for name_img in list_img:
        path_img = os.path.join(PATH, name_img)

        property_img = {}

        property_img['name'] = name_img
        property_img['size'] = os.path.getsize(path_img)
        property_img['time'] = os.path.getmtime(path_img)

        list_files.append(property_img)

    return jsonify({'list_files': list_files}), 200


@app.route('/image', methods=['POST'])
def img_list_post():

    if 'name' in request.json:

        data = request.get_json()['name']
        decode = base64.b64decode(data)
        name = decode.decode('utf-8')

        path_img = os.path.join(PATH, f'{name}.jpg')

        open(path_img, 'w')

        return make_response('Created', 201)
    else:
        return make_response('Not Found', 404)


@app.route('/image', methods=['DELETE'])
def img_list_del():

    try:
        if 'name' in request.json:
            data = request.get_json()['name']
            path_img = os.path.join(PATH, f'{data}.jpg')

            os.remove(path_img)

    except (TypeError, FileNotFoundError):
        return make_response('Not Found', 404)
    else:
        return make_response('No Content', 204)
