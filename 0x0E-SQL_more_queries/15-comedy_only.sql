-- Script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- Select where and order by
SELECT ts.title
FROM   tv_genres tg, tv_show_genres tsg, tv_shows ts
WHERE  tg.id = tsg.genre_id
  AND  tsg.show_id = ts.id
  AND  tg.name = "Comedy"
ORDER BY ts.title ASC;
