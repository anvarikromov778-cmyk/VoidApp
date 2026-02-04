[app]

# Название приложения
title = Void Assistant

# Имя пакета
package.name = voidassistant

# Домен (обратный)
package.domain = com.void

# Исходный код
source.dir = .

# Главный файл
source.include_exts = py,png,jpg,kv,atlas

# Версия
version = 3.0

# Требования
requirements = python3,kivy,jnius,android

# Разрешения Android
android.permissions = RECORD_AUDIO,INTERNET,ACCESS_NETWORK_STATE,WAKE_LOCK,
                      CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,
                      CALL_PHONE,SEND_SMS,READ_CONTACTS,ACCESS_FINE_LOCATION,
                      ACCESS_COARSE_LOCATION

# API
android.api = 33
android.minapi = 21
android.ndk = 23b

# Ориентация
orientation = portrait

# Полноэкранный режим
fullscreen = 0

# Иконка
icon.filename = %(source.dir)s/icon.png

# Splash экран
presplash.filename = %(source.dir)s/presplash.png

# Тип сборки
android.arch = armeabi-v7a,arm64-v8a

[buildozer]

# Логи
log_level = 2

# Уведомления
warn_on_root = 1
