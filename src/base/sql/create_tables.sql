CREATE TABLE IF NOT EXISTS users
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at Datetime NOT NULL,
    updated_at Datetime,
    name Utf8
);

CREATE TABLE IF NOT EXISTS words
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at Datetime NOT NULL,
    updated_at Datetime,
    ru Utf8,
    de Utf8,

	FOREIGN KEY(de) REFERENCES audio(de)
);

CREATE TABLE IF NOT EXISTS user_lists
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at Datetime NOT NULL,
    updated_at Datetime,
    user_id Int64,
    count Int32,
    name utf8,
    is_loaded Bool DEFAULT FALSE,
    is_created Bool DEFAULT FALSE,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS user_words
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    list_id Int64,
    word_id Int64,
    is_processed Bool,
    audio_id utf8,
    learned Bool DEFAULT FALSE,
	FOREIGN KEY(list_id) REFERENCES user_lists(id),
	FOREIGN KEY(word_id) REFERENCES words(id)
);

CREATE TABLE IF NOT EXISTS audio
(
    de Utf8 PRIMARY KEY,
    file_path Utf8
);
