-- Write a SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
-- Note: An average score can be a decimal

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser ( IN u_id INT )
BEGIN
    DECLARE avg_score float;

    SELECT AVG(score) INTO avg_score
    FROM corrections 
    WHERE user_id = u_id;

    UPDATE users
    SET average_score = IFNULL(avg_score, 0)
    WHERE id = u_id;

END $$

DELIMITER ;