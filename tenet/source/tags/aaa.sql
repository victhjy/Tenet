-- 查询dau
select count(*)
FROM
  (
SELECT DISTINCT utdidd
  FROM
    (
SELECT DISTINCT utdidb as utdidc
    FROM


      (
SELECT DISTINCT utdid as utdida
      FROM alilog.dwd_lzd_user_track
      WHERE ds = '20200923'
        AND event_id = '1010'
  )
  AS a

      INNER JOIN


      (SELECT DISTINCT utdid as utdidb
      FROM alilog.dwd_lzd_user_track
      WHERE ds = '20200923'
        AND event_id = '2001'
)
AS b
      ON a.utdida=b.utdidb 

)
AS c



    INNER JOIN

    (
SELECT DISTINCT utdid as utdidd
    FROM alilog.dwd_lzd_user_track
    WHERE ds = '20200923'
      AND event_id = '2101'
)
AS d
    ON  c.utdidc=d.utdidd
)
;

select utdid
from (
select utdid
from alilog.dwd_lzd_user_track 
where ds = '20200929'
and event_id = '2101'
and app_version = '6.54.0'
-- and app_id in ('23868882@iphoneos','23867946@android','23868882@ipad')
and app_id = '23868882@iphoneos'
and arg1 in ('/lzdhome.modules_will_render.server_module_render', '/lzdhome.modules_will_render.cache_module_render')
and KEYVALUE(lower(args),',','=','flashsalev2') = '1'
EXCEPT
select utdid
from alilog.dwd_lzd_user_track 
where ds = '20200929'
and event_id = '2201'
and app_version = '6.54.0'
-- and app_id in ('23868882@iphoneos','23867946@android','23868882@ipad')
and app_id = '23868882@iphoneos'
and lower(page) = 'aage_home'
and lower(arg1) = 'flashsalev2'
)
limit 10
;

select count(DISTINCT b.utdid)
from
(select utdid
from alilog.dwd_lzd_user_track 
where ds = '20200929'
and event_id = '2101'
and app_version = '6.54.0'
-- and app_id in ('23868882@iphoneos','23867946@android','23868882@ipad')
and app_id = '23868882@iphoneos'
and arg1 = '/lzdhome.modules_will_render.server_module_render'
and KEYVALUE(lower(args),',','=','flashsalev2') = '1')
as a 
INNER JOIN
(select utdid
from alilog.dwd_lzd_user_track 
where ds = '20200929'
and event_id = '2101'
and app_version = '6.54.0'
-- and app_id in ('23868882@iphoneos','23867946@android','23868882@ipad')
and app_id = '23868882@iphoneos'
and arg1 = '/lzdhome.modules_will_render.cache_module_render'
and KEYVALUE(lower(args),',','=','flashsalev2') = '1')
as b
on a.utdid = b.utdid
)
;