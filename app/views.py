import base64
import os

from flask import jsonify, request, make_response

from app import app


PATH = PATH = os.path.realpath('/images/')

@app.route('/images/<path:name>.jpg')
def img_detail(name, methods=['GET']):
    name = name

    path_img = PATH + '/' + name + '.jpg'

    if os.path.isfile(path_img):
        return f'file {name}'
    else:
        return f'not file {name}'


@app.route('/image', methods=['GET', 'POST', 'DELETE'])
def img_list():

    if request.method == 'GET':

        list_img = os.listdir(PATH + '/')

        list_files = []

        for name_img in list_img:
            path_img = PATH + '/' + name_img

            property_img = {}

            property_img['name'] = name_img
            property_img['size'] = os.path.getsize(path_img)
            property_img['time'] = os.path.getmtime(path_img)

            list_files.append(property_img)

        return jsonify({'list_files': list_files}), 200

    elif request.method == 'POST':
        if 'name' in request.json:

            data = request.get_json()['name']
            decode = base64.b64decode(data)
            name = decode.decode('utf-8')

            file = open(PATH + '/' + name + '.jpg', 'w')

            return make_response('Created', 201)
        else:
            return make_response('Not Found', 404)

    elif request.method == 'DELETE':
        try:
            if 'name' in request.json:
                data = request.get_json()['name']
                path_img = PATH + '/' + data + '.jpg'

                os.remove(path_img)

        except (TypeError, FileNotFoundError):
            return make_response('Not Found', 404)
        else:
            return make_response('No Content', 204)
