-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student

DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser ( IN u_id INT )
BEGIN
    DECLARE sum_weight INT;
    DECLARE sum_scores INT;

    SELECT SUM(score * projects.weight) INTO sum_scores
    FROM corrections INNER JOIN projects
    ON corrections.project_id = projects.id
    WHERE user_id = u_id;

    SELECT SUM(projects.weight) INTO sum_weight
    FROM corrections INNER JOIN projects
    ON corrections.project_id = projects.id
    WHERE user_id = u_id;

    UPDATE users
    SET average_score = sum_scores / sum_weight
    WHERE id - u_id;

END $$

DELIMITER ;
