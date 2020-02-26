-- Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Select left join
SELECT tg.name AS genre, count(*) AS number_of_shows
FROM   tv_show_genres tsg LEFT JOIN tv_genres tg
  ON   tg.id = tsg.genre_id
GROUP BY tsg.genre_id
ORDER BY count(*) DESC;
