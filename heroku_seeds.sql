INSERT INTO users (first_name, last_name, email, hashed_password, gender, gender_pref, img_url, spectrum, likes_puns, favorite_pet, spontaneous, into_tech, introvert)
VALUES
    ('demo',
    'user',
    'demouser@demouser.com',
    'pbkdf2:sha256:150000$Kae4NpQC$0f5d41ceda81c71f16e5c4f7c5651b12e3bb9aa631ff9c2c9a979a6781b7fe7f',
    'nonbinary',
    'all',
    null,
    'asexual',
    true,
    'dogs',
    true,
    true,
    true),
    (
        'Domenico',
        'Scandella',
        'cheese@worms.com',
        'pbkdf2:sha256:150000$Kae4NpQC$0f5d41ceda81c71f16e5c4f7c5651b12e3bb9aa631ff9c2c9a979a6781b7fe7f',
        'male',
        'all',
        null,
        'asexual',
        true,
        'cats',
        true,
        true,
        true
    );


INSERT INTO messages (sender_id, recipient_id, content)
VALUES
    (
        1,
        2,
        'Hey!',
        false
    )