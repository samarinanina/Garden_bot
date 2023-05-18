class const():
    start = 'start'
    op = 'посмотреть возможности'
    welcome = 'Добро пожаловать'
    cont = 'continue'
    cont_1 = 'продолжаем'
    text = 'text'
    delete = "удалить"
    add = "добавить"
    f_return = "вернуться в главное меню"
    t_return = 'Вы вернулись в главное меню'
    new = "обновить каталог"
    look = "посмотреть каталог"
    have = "посмотреть имеющиеся"
    name_delete = 'запишите название, которое хотите удалить'
    name_change = 'запишите название, которое хотите перенести в имеющиеся'
    in_stock = 'растения в наличии'
    to_buy = 'собираюсь купить'
    next_move = 'ваши дальнейшие действия?'
    wish = "чего именно вы хотите?"
    change_to_have = "перенести в имеющиеся"
    wrong_message = 'чтобы продолжить напишите /continue'
    add_new = "добавить новые"
    change = 'Какое изменение вы хотите произвести?'
    table = 'table.sql'
    create = 'CREATE TABLE IF NOT EXISTS buy( name varchar(50), description varchar(200), have_it bool);'
    delete_table = f"DELETE FROM buy WHERE name='%s';"
    write_name = 'запишите название'
    ready = 'Готово!'
    insert = 'INSERT INTO buy(name, description, have_it) VALUES("%s", "%s", "%d")'
    desc = 'создайте описание(_ при отсутствии)'
    select = f"SELECT * FROM buy WHERE name = '%s'"
    update = f"UPDATE buy SET have_it=1 WHERE name= '%s'"
