# <img width="70" alt="image" src="https://github.com/Jayveersinh-Raj/innoagent/assets/69463767/0b07bac1-9f91-41d6-a511-55c9f0fe3498"> Giga Researcher 
Английская версия инструкции доступна [здесь](README.md).
### ✨ Инструмент для анализа литературы, который поможет исследователям быстрее изучать статьи и писать код.
### ✨ GigaResearcher - это автономная система на базе ИИ агентов для проведения комплексных онлайн-исследований. Система предоставит обзор литературы в виде репорта, в котором основное внимание будет уделяться деталям реализации.
### 😎 Разработана на основе [GigaChat](https://developers.sber.ru/docs/ru/gigachat/overview) и [GigaChain](https://github.com/ai-forever/gigachain). 

## Дизайн системы:
### Процесс запускает агенты "planner", "executor" и "report generator" для проведения анализа литературы и создания отчета. Planner генерирует исследовательские вопросы. Затем, несколько executor-агентов ищут наиболее релевантную информацию на основе сгенерированных вопросов. Наконец, report generator фильтрует и агрегирует всю полученную информацию и создает отчет об исследовании.

![Workflow](https://github.com/Jayveersinh-Raj/giga_researcher/assets/69463767/55333b33-bdc6-40b0-ba34-ea6d87088983)

<br>


## ✨ Как использовать

### 📖 Внимание: Обязательно укажите API-ключи `GITHUB` и `GIGACHAIN` в `secret_key.env`.

### 👉Реализованы поисковые агенты для arxiv и web crawl. Они генерируют отчеты по задаваемым вопросам или промптам, переданным вместе с названием статьи или ссылкой на ресурс.
### 👉Также, реализован пользовательский поиск по ссылкам, который позволяет запрашивать информацию по указанному URL, например, в GitHub репозитории.

## ✨ Структура кода и установка для `arxiv` и `web` поиска
### Установите зависимости в родительском каталоге, создав виртуальную среду (рекомендуется):
    pip install -r requirements.txt
### 💻`arxiv_search_git` &rarr; Содержит файлы для запуска `arxiv retriever`. Каталог `github_retrieve` управляет частью агента GitHub. `main.py` служит точкой входа. Перейдите в каталог `arxiv_search_git` и выполните следующие действия:
    cd arxiv_search_git/
    python main.py
### 💻`web_search_git` &rarr; Содержит файлы для запуска `web retriever`. Каталог `github_retrieve` управляет частью агента GitHub. `main.py` служит точкой входа. Перейдите в каталог `web_search_git` и выполните следующие действия:
    cd web_search_git/
    python main.py    

### ✨ Перейдите по ссылке ниже, чтобы воспользоваться сервисом:
    http://localhost:8000/giga_research/playground/
### 📖 Примечание: arxiv и web-search должны запускаться под разными портами или по отдельности. Не забудьте предоставить свои API-ключи `GITHUB` и `GIGACHAIN` в `secret_key.env`.

## ✨ Структура кода и установка агента для пользовательского поиска по ссылкам
### Установите зависимости в родительском каталоге, создав виртуальную среду (рекомендуется):
    pip install -r requirements.txt
### `main.py` служит точкой входа. Перейдите в каталог `custom_link_search` и запустите следующие команды:
    cd custom_link_search/
    python main.py    

### ✨ Перейдите по ссылке ниже, чтобы воспользоваться сервисом:
    http://localhost:4000/research-assistant/playground/

### 📖 Примечание: Поместите свои API-ключи `GITHUB` и `GIGACHAIN` в `secret_key.env`. Этот агент будет размещен на отдельном порте (port:4000), поэтому он может работать одновременно с `arxiv` и `web` агентом.
