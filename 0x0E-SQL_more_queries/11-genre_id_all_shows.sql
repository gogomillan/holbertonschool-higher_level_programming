-- Script that lists all shows contained in the database hbtn_0d_tvshows plus its genre.
-- Select left join
SELECT ts.title, tsg.genre_id
FROM   tv_shows ts LEFT JOIN tv_show_genres tsg
  ON   tsg.show_id = ts.id
ORDER BY ts.title, tsg.genre_id;
