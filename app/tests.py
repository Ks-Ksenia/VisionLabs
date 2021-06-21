import base64
import os
import unittest
import json


from app import app
import views


class AppTestCase(unittest.TestCase):

    def test_img_detail(self):

        with app.test_client() as client:
            rv = client.get('/images/b1.jpg')

            self.assertEqual(rv.content_type, 'image/jpg')

    def test_img_list_get(self):

        with app.test_client() as client:
            rv = client.get('/image')

            str_json = json.loads(rv.data.decode('utf-8'))

            rv_dict = str_json['list_files'][0]

            self.assertEqual(rv.content_type, 'application/json')

            self.assertIn('name', rv_dict)
            self.assertIn('size', rv_dict)
            self.assertIn('time', rv_dict)

    def test_img_list_post(self):

        test_img = os.path.join(os.path.realpath('/images/'), 'b1.jpg')

        with open(test_img, 'rb') as file:
            bytes_img = file.read()

        base64_str = base64.b64encode(bytes_img)

        with app.test_client() as client:
            rv = client.post('/image', data=base64_str)

            self.assertEqual(rv.status_code, 201)

    def test_img_list_del(self):
        with app.test_client() as client:
            test_img = os.path.join(os.path.realpath('/images/'), 'b2.jpg')

            rv = client.delete('/image', data='b2')

            self.assertFalse(os.path.isfile(test_img))
            self.assertEqual(rv.status_code, 204)
