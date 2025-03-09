INSERT INTO p_crm_status (ENTITY_ID, STATUS_ID, TITLE, COLOR, SYSTEM_STATUS, SEMANTICS, SORT) VALUES
('DEAL_STAGE', 'NEW', 'Новая сделка', '#FF5752', 1, NULL, 100),
('DEAL_STAGE', 'С_2736', 'Определение требований', '#FF5752', 0, 'P', 200),
('DEAL_STAGE', 'С_8945', 'Подготовка документов', '#FF5752', 0, 'P', 300),
('DEAL_STAGE', 'APOLOGY', 'Анализ причины провала', '#FF5752', 1, 'F', 0),
('DEAL_STAGE', 'LOSE', 'Сделка провальна', '#FF5752', 1, 'F', 0),
('DEAL_STAGE', 'WON', 'Сделка успешна', '#7BD500', 1, 'S', 0);


INSERT INTO p_crm_deal (TITLE, CREATED_BY_ID, MODIFY_BY_ID, ASSIGNED_BY_ID, LEAD_ID, COMPANY_ID, CONTACT_ID, STAGE_ID, IS_NEW, CLOSED, TYPE_ID, OPPORTUNITY, DATE_MODIFY) VALUES
('Сделка 1', 1, NULL, 2, NULL, NULL, NULL, 'NEW', TRUE, FALSE, 'Тип 1', '10000', NOW()),
('Сделка 2', 1, NULL, 2, NULL, NULL, NULL, 'С_2736', TRUE, FALSE, 'Тип 1', '15000', NOW()),
('Сделка 3', 2, NULL, 3, NULL, NULL, NULL, 'С_2736', FALSE, TRUE, 'Тип 2', '20000', NOW()),
('Сделка 4', 2, NULL, 3, NULL, NULL, NULL, 'LOSE', TRUE, FALSE, 'Тип 2', '25000', NOW()),
('Сделка 5', 3, NULL, 1, NULL, NULL, NULL, 'С_8945', TRUE, FALSE, 'Тип 1', '30000', NOW()),
('Сделка 6', 3, NULL, 1, NULL, NULL, NULL, 'APOLOGY', FALSE, TRUE, 'Тип 1', '35000', NOW()),
('Сделка 7', 1, NULL, 2, NULL, NULL, NULL, 'NEW', TRUE, FALSE, 'Тип 3', '40000', NOW()),
('Сделка 8', 2, NULL, 3, NULL, NULL, NULL, 'С_2736', TRUE, FALSE, 'Тип 2', '45000', NOW()),
('Сделка 9', 2, NULL, 3, NULL, NULL, NULL, 'WON', FALSE, TRUE, 'Тип 3', '50000', NOW()),
('Сделка 10', 3, NULL, 1, NULL, NULL, NULL, 'WON', TRUE, FALSE, 'Тип 1', '55000', NOW());


INSERT INTO p_user_field (TITLE, ENTITY_ID, FIELD_NAME, USER_TYPE_ID, SORT, MANDATORY) VALUES 
('Годовой доход', 'DEAL', 'UF_CRM_3478539932943', 'string', 100, 1);

INSERT INTO p_utm_crm_deal (DEAL_ID, FIELD_ID, VALUE) VALUES 
(2, 1, 'ASHAB BRATKA');