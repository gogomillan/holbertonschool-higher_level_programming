-- Script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Select join
SELECT ts.title, tsg.genre_id
FROM   tv_shows ts JOIN tv_show_genres tsg
ON     tsg.show_id = ts.id
ORDER BY ts.title, tsg.genre_id;
