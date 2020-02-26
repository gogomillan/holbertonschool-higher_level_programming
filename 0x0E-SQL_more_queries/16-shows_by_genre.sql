-- Script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- Select left join left join and order by
SELECT ts.title, tg.name
FROM   tv_shows ts
       LEFT JOIN tv_show_genres tsg ON tsg.show_id = ts.id
       LEFT JOIN tv_genres tg ON tsg.genre_id = tg.id
ORDER BY ts.title, tg.name ;
