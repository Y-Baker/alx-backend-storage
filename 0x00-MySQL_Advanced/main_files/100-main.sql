SELECT * FROM users;
SELECT * FROM projects;
SELECT * FROM corrections;

CALL ComputeAverageWeightedScoreForUser((SELECT id FROM users WHERE id = 1));

SELECT "--";
SELECT * FROM users;
