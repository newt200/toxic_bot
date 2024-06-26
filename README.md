# Toxic_bot
[Тг-бот](https://t.me/DontBeToxic_bot) умеет определять уровень токсичности сообщения, а также выдает статистику с форума [woman.ru](https://www.woman.ru/forum/)
# Устройство репозитория
* **parsing_and_model.ipynb** – тетрадка, в которой находится код для парсинга, обучения модели и создания графиков
* **woman.ru – 9 topic.csv** – файл с готовым датасетом после парсинга
* **labeled.csv** – файл для обучения
* **woman_predicted.csv** – датасет с готовыми предсказаниями
* **pictures.zip** – архив с графиками
* **model.pkl** – сохраненная обученная модель
* **tg_bot2024.py** – основной код для бота
# Установка и использование
Чтобы запустить бота локально, нужно установить библиотеки следующих версий, которые указаны в файле [requirements.txt](https://github.com/newt200/toxic_bot/blob/main/requirements.txt), также скачать предобученную в google colab модель [model.pkl](https://github.com/newt200/toxic_bot/blob/main/model.pkl) и папку с картинками [pictures.zip](https://github.com/newt200/toxic_bot/blob/main/pictures.zip) (но все это можно получить, запустив код в коллабе). Бот выложен на python-anywhere.
# Данные
## Обучение
Для обучения модели, которая может определять, является ли текст токсичным, я использовала датасет `labeled.txt`, который также можно скачать с [kaggle.com](https://www.kaggle.com/datasets/blackmoon/russian-language-toxic-comments).

Перед векторизацией данные прошли препроцессинг: сообщения были лемматизированы, и из них были удалены стоп-слова.

Далее я посмотрела на две модели LogisticRegression и SVC (метод опорных векторов). В качестве векторизатора я использовала TfIdfVectorizer, который имел параметр нормирования `l2` для нормализации значений и он учитывал только слова (с n-gramm результат получался хуже). Для самой модели классификации при помощи GridSearch было подобрано на валидационной выборке оптимальное значение коэффициента регуляризации С. 

Наиболее эффективной оказалась модель LogisticRegression с С=17. Значение метрики recall – 0.73, а precision – 0.86, что относительно неплохо и выше значений этих метрик, который получились у пользователей для текущего датасета на kaggle.com.

## Парсинг, предсказания и анализ
Я спарсила сообщения людей в различных тредах на форуме [woman.ru](https://www.woman.ru/forum/) по следующим топикам:
* отношения;
* психология;
* дети;
* отдых;
* звезды;
* мода;
* здоровье;
* дом;
* красота.

У меня получился csv-фал `woman.ru – 9 topic.csv` с ~ 57k строк.

После применения модели на `woman.ru – 9 topic.csv` токсичными оказались всего лишь около ~ 8k сообщений. 
Самыми токсичными оказались следующие топики (с долей токсичных сообщений ~ 0.18):
1. Дети
2. Звезды
3. Отношения

# Работа бота
В боте есть следующие команды:
* `\start` – для начала работы
* `\toxic_detect` – бот просит пользователя ввести сообщение и классифицирует его как токсичное/нетоксичное
* `\statistics` – здесь на кнопках пользователю предложено либо посмотреть облако слов для разных топиков форума, либо посмотреть на  доли токсичных сообщений в зависимости от темы/года

# Комментарии
В целом, модель неплохо классифицирует сообщения. Она отлично реагирует на нецензурную лексику и другие негативно окрашенные слова. Но все-таки поведение может быть непредсказуемо. Например, модель классифицирует фразу "Привет, как дела?" как токсичную. Таким образом, нельзя полностью полагаться на надежность модели, обученной на векторных представлениях слов. Для таких целей отлично подходят LLM с механизмом внимания, особенно модели типа BERТ, где у каждого токена есть доступ к друг другу.

Перед началом реализации проекта у меня были гипотезы, что доля токсичных комментариев будет находиться в линейной зависимости с годом, а какие-то темы будут сильно выделяться по уровню токсичности. Но, кажется, гипотезы не были подтверждены. Возможно, нужно подобрать более эффективный алгоритм для сбора сообщений с форума.

# Что дальше
1. Поработать с контекстом, использовать языковую модель для обучения
2. Поработать со словарем и стоп-словами

# Автор
Мария Селифанова (@newt2000)
