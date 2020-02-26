-- Script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.
-- Select left join and not in
SELECT DISTINCT tg.name
FROM tv_shows ts
     LEFT JOIN tv_show_genres tsg ON tsg.show_id = ts.id
     LEFT JOIN tv_genres tg ON tsg.genre_id = tg.id
WHERE tg.name NOT IN (SELECT g.name
                      FROM   tv_genres g, tv_show_genres t, tv_shows s
                      WHERE  g.id = t.genre_id
                        AND  t.show_id = s.id
                        AND  s.title = "Dexter")
ORDER BY tg.name;
