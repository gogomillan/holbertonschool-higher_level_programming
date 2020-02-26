-- Best genre
-- Select sum inner join group by and order by
SELECT tg.name, Sum(tsr.rate) AS "rating"
FROM tv_shows ts JOIN tv_show_ratings tsr ON tsr.show_id = ts.id
                 JOIN tv_show_genres tsg ON ts.id = tsg.show_id
                 JOIN tv_genres tg ON tg.id = tsg.genre_id
GROUP BY tg.name
ORDER BY Sum(tsr.rate) DESC;
