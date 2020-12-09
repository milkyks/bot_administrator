INSERT INTO commands (main_name, is_active, priority) VALUES ('Комендант', 1, 1);
INSERT INTO commands (main_name, is_active, priority) VALUES ('Кастелянша', 1, 1);
INSERT INTO commands (main_name, is_active, priority) VALUES ('Спортзал', 1, 1);
INSERT INTO commands (main_name, is_active, priority) VALUES ('study_room', 1, 1);
INSERT INTO commands (main_name, is_active, priority) VALUES ( 'guests', 1, 1);
INSERT INTO commands (main_name, is_active, priority) VALUES ( 'shower', 1, 1);
INSERT INTO commands (main_name, is_active, priority) VALUES ( 'laundry', 1, 1);
INSERT INTO commands (main_name, is_active, priority) VALUES ( 'duty', 1, 1);
INSERT INTO commands (main_name, is_active, priority) VALUES ( 'question', 1, 1);
INSERT INTO commands (main_name, is_active, priority) VALUES ( 'Приветствие', 1, 3);
INSERT INTO commands (main_name, is_active, priority) VALUES ( 'parting', 1, 4);
INSERT INTO commands (main_name, is_active, priority) VALUES ( 'gratitude', 1, 1);
INSERT INTO commands (main_name, is_active, priority) VALUES ( 'opportunities', 1, 1);
INSERT INTO commands (main_name, is_active, priority) VALUES ( 'invoice', 1, 1);
INSERT INTO commands (main_name, is_active, priority) VALUES ( 'topical', 1, 1);
INSERT INTO commands (main_name, is_active, priority) VALUES ( 'registration', 1, 1);
INSERT INTO commands (main_name, is_active, priority) VALUES ( 'Шутка', 1, 2);



select @curr_id:=c.id from commands c where c.main_name = 'Комендант';
INSERT INTO command_synonyms (synonym, command_id) VALUES ('КОМЕНДАНТ', @curr_id);
INSERT INTO command_synonyms (synonym, command_id) VALUES ('МИЛЕНА', @curr_id);
INSERT INTO command_responses (response, command_id) VALUES ('Милена Леонидовна работает в непраздничные дни с понедельника по четверг с 9:00 до 17:00.\nВ пятницу с 9:00 до 16:30.\nОбеденный перерыв с 13:00 до 13:30.\nТелефон: +78127750530 доб. 1454.\nПочта: dorm5@spbstu.ru', @curr_id);

select @curr_id:=c.id from commands c where c.main_name = 'Кастелянша';
INSERT INTO command_synonyms (synonym, command_id) VALUES ('БЕЛЬЕ', @curr_id);
INSERT INTO command_synonyms (synonym, command_id) VALUES ('ПОСТЕЛЬ', @curr_id);
INSERT INTO command_responses (response, command_id) VALUES ('Маргарита Валерьевна (кастелянша) меняет белье в понедельник и в среду с 10:00 до 17:00.\nОбеденный перерыв с 13:00 до 13:30.\nБелье приносить СТРОГО в пакетах.\nВозможны изменения, актуальная информация размещена на первом этаже.', @curr_id);

select @curr_id:=c.id from commands c where c.main_name = 'Спортзал';
INSERT INTO command_synonyms (synonym, command_id) VALUES ('СПОРТЗАЛ', @curr_id);
INSERT INTO command_synonyms (synonym, command_id) VALUES ('СПОРТ', @curr_id);
INSERT INTO command_synonyms (synonym, command_id) VALUES ('ЗАЛ', @curr_id);
INSERT INTO command_synonyms (synonym, command_id) VALUES ('СПОРТИВНЫЙ', @curr_id);
INSERT INTO command_synonyms (synonym, command_id) VALUES ('ТРЕНАЖЕРКА', @curr_id);
INSERT INTO command_responses (response, command_id) VALUES ('Тут будет информация о зале
Интерено сохранился ли преренос строки между предложениями?', @curr_id);



select @curr_id:=c.id from commands c where c.main_name = 'Приветствие';
INSERT INTO command_synonyms (synonym, command_id) VALUES ('ПРИВЕТ', @curr_id);
INSERT INTO command_synonyms (synonym, command_id) VALUES ('ЗДРАВСТВУЙТЕ', @curr_id);
INSERT INTO command_synonyms (synonym, command_id) VALUES ('ДОБРЫЙ', @curr_id);
INSERT INTO command_responses (response, command_id) VALUES ('И тебе привет!', @curr_id);

select @curr_id:=c.id from commands c where c.main_name = 'Шутка';
INSERT INTO command_synonyms (synonym, command_id) VALUES ('ШУТКА', @curr_id);
INSERT INTO command_synonyms (synonym, command_id) VALUES ('ЮМОР', @curr_id);
INSERT INTO command_synonyms (synonym, command_id) VALUES ('АНЕКДОТ', @curr_id);
INSERT INTO command_responses (response, command_id) VALUES ('Колобок повесился.', @curr_id);
INSERT INTO command_responses (response, command_id) VALUES ('Кощей застрелился.', @curr_id);


select @curr_id:=c.id from commands c where c.main_name = 'DEFAULT';
INSERT INTO command_responses (response, command_id) VALUES ('Я не понял что от меня хотят :(', @curr_id);

insert into users (full_name, vk_id, room_number, phone_number, type)
    values ('Тест Тестович', 134728452, 566, '+7999999999', 'Студент');

insert into users (full_name, vk_id, room_number, phone_number, type)
    values ('Георгий Батькович', 184541442, 300, '+7999999999', 'Администратор');
-- кстати, админу\коменде не нужна комната же
-- ножно внятное описание какие типы юзеров бывают

insert into rooms (id, size, floor) values (566, 3, 5);
insert into rooms (id, size, floor) values (300, 3, 3);
insert into rooms (id, size, floor) values (250, 2, 2);



