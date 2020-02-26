-- Script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- Select where and order by
SELECT tg.name
FROM   tv_genres tg, tv_show_genres tsg, tv_shows ts
WHERE  tg.id = tsg.genre_id
  AND  tsg.show_id = ts.id
  AND  ts.title = "Dexter"
ORDER BY tg.name ASC;
