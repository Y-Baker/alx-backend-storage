-- Show and compute average score
SELECT * FROM users;
SELECT * FROM corrections;

SELECT "--";
CALL ComputeAverageScoreForUser((SELECT id FROM users WHERE id = 1));

SELECT "--";
SELECT * FROM users;
