INSERT INTO p_crm_status (ENTITY_ID, STATUS_ID, TITLE, COLOR, SYSTEM_STATUS, SEMANTICS, SORT) VALUES
('DEAL_STAGE', 'NEW', 'Новая сделка', '#FF5752', 1, NULL, 100),
('DEAL_STAGE', 'С_2736', 'Определение требований', '#FF5752', 0, 'P', 200),
('DEAL_STAGE', 'С_8945', 'Подготовка документов', '#FF5752', 0, 'P', 300),
('DEAL_STAGE', 'APOLOGY', 'Анализ причины провала', '#FF5752', 1, 'F', 0),
('DEAL_STAGE', 'LOSE', 'Сделка провальна', '#FF5752', 1, 'F', 0),
('DEAL_STAGE', 'WON', 'Сделка успешна', '#7BD500', 1, 'S', 0);