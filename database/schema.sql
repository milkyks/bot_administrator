-- Дежурство
-- mark - молодцы или не молодцы товарищи [ТЗ BS-11]
create table duties (
  id int primary key auto_increment,
  floor int not null,
  room_number int not null,
  date timestamp not null,
  mark int not null
);


-- Пользователи бота
create table users (
  id int primary key auto_increment,
  full_name varchar(250) not null,
  vk_id bigint not null,
  room_number int not null,
  phone_number varchar(250) not null,
  type varchar(250) not null
);

-- Запись в спортзал
create table registrations_sport (
  id int primary key auto_increment,
  user_id int not null,
  date timestamp not null,

  constraint registration_ibfk_1
      foreign key (user_id) references users (id)
          on delete cascade
);

-- Запись в учебку
create table registrations_studyroom (
  id int primary key auto_increment,
  user_id int not null,
  date timestamp not null,

  constraint registration_ibfk_1
      foreign key (user_id) references users (id)
          on delete cascade
);

-- Команды
-- Приоритет - "привет" менее приоритетно чем  "душ" и т.д.
-- main_name - главное название команды, которое отображается на клавиатуре\заголовок в UI
create table commands (
  id int primary key auto_increment,
  main_name varchar(250) not null,
  is_active boolean not null,
  priority int not null
);


-- Статистика по командам
create table command_statistics (
  id int primary key auto_increment,
  vk_id bigint not null,
  date timestamp not null,
  command_id int not null,


  constraint command_statistics_ibfk_1
      foreign key (command_id) references commands (id)
          on delete cascade
);

-- Ответы на команду
create table command_responses (
  id int primary key auto_increment,
  response mediumtext not null,
  command_id int not null,

  constraint command_responses_ibfk_1
      foreign key (command_id) references commands (id)
          on delete cascade
);

-- Синонимы, на которые реагирует бот и сопоставляет с командой
create table command_synonyms (
  id int primary key auto_increment,
  synonym varchar(250) not null,
  command_id int not null,
  constraint command_synonyms_ibfk_1
      foreign key (command_id) references commands (id)
          on delete cascade
);


-- информация о комнатах, id=номер
-- alive=1 сейчас комната не пустует, alive = 0 - пустует
-- этаж хранится для быстрого доставания комнат по этажу
create table rooms (
  id int primary key,
  floor int not null,
  alive int not null
);
