-- Write a SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
-- Note: An average score can be a decimal

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser ( IN user_id INT )
BEGIN
    DECLARE avg float;

    SELECT AVG(score) INTO avg
    FROM corrections 
    WHERE user_id = user_id;

    UPDATE users
    SET average_score = IFNULL(avg, 0)
    WHERE id = user_id;

END $$

DELIMITER ;