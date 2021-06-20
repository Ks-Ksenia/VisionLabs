# VisionLabs

## О проекте
Тестовый проект, в котором реализован простой web-сервис, работающий с изображениями. Сервис отображает, создаёт и удаляет изображения.

### Endpoints
- http://hostname:port/images/image_name.jpg
    - отображает изображение image_name.jpg
- http://hostname:port/image
    - выводить список изображений в формате json, где содержиться имя файла, размер, время последней модификации
    - удаляет изображение по его имени
    - создаёт новое изображение из переданной base64-строки
