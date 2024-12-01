# Лаба 4 юхууу

## Задание: 
1. Написать “плохой” CI/CD файл, который работает, но в нем есть не менее пяти “bad practices” по написанию CI/CD
2. Написать “хороший” CI/CD, в котором эти плохие практики исправлены
3. В Readme описать каждую из плохих практик в плохом файле, почему она плохая и как в хорошем она была исправлена, как исправление повлияло на результат

   ## Дисклеймер:
 во время работы над данной лабой я больше намучилась с косяками в тестах, простеньком коде проекта и зависимостях… Ужос….

Написать “плохой” CI/CD файл, который работает, но в нем есть не менее пяти “bad practices” по написанию CI/CD

В Общем, достаточно интересно получилось, но плохой файл выглядит вот так:


```yaml
name: CI/CD with bad practise


# запуск на всех ветках
on:
 push:
   branches:
     - '*'
# все шаги в одной джобе, нет деления на билд тест деплой
jobs:
 test:
   runs-on: ubuntu-latest


   steps:
     - name: Checkout code
       uses: actions/checkout@v2


     # установка зависимостей без создания виртуального окружения
     - name: Install dependencies
       run: |
         pip install -r requirements.txt  # Установка в глобальное окружение может вызвать конфликты


     # пропуск тестов
     - name: Skip tests
       run: echo "Skipping tests"


     # тесты и так пропустили, так еще и деплоим без проверки пройденности, во неадекваты....
     - name: Build and deploy
       run: |
         echo "Building the project..."  # Отсутствие проверки успешности предыдущих шагов

```
