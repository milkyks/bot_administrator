-- Код добавления новой-новой команды
INSERT INTO commands (main_name, is_active, priority) VALUES (основное_название, 1, 1);
select @curr_id:=c.id from commands c where c.main_name = основное_название;
INSERT INTO command_synonyms (synonym, command_id) VALUES (основное_название, @curr_id);


-- Добавление синонима
select @curr_id:=c.id from commands c where c.main_name = основное_название;
INSERT INTO command_synonyms (synonym, command_id) VALUES (синоним, @curr_id);

-- Быстрый поиск для людей, которые пишут правильные запросы в чат - по списку команд поля main_name

-- Медленный поиск по всем словам - перебирать всю таблицу command_synonyms


