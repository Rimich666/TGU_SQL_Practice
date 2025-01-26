CREATE TABLE IF NOT EXISTS users
(
    id serial NOT NULL,
    expire_at Datetime NOT NULL,
    updated_on Datetime,
    name Utf8,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS words
(
    id serial NOT NULL,
    expire_at Datetime NOT NULL,
    updated_on Datetime,
    ru Utf8,
    de Utf8,

    PRIMARY KEY (id),
	FOREIGN KEY(de) REFERENCES audio(de)
);

CREATE TABLE IF NOT EXISTS user_lists
(
    id serial NOT NULL,
    expire_at Datetime NOT NULL,
    updated_on Datetime,
    user_id Int64,
    count Int32,
    name utf8,
    is_loaded Bool DEFAULT FALSE,
    is_created Bool DEFAULT FALSE,
    PRIMARY KEY (id),
	FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS user_words
(
    id serial NOT NULL,
    list_id Int64,
    word_id Int64,
    is_processed Bool,
    audio_id utf8,
    learned Bool DEFAULT FALSE,
    PRIMARY KEY (id),
	FOREIGN KEY(list_id) REFERENCES user_lists(id),
	FOREIGN KEY(word_id) REFERENCES words(id)
);

CREATE TABLE IF NOT EXISTS audio
(
    de Utf8 NOT NULL ,
    file_path Utf8,

    PRIMARY KEY (de)
);
