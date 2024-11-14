USE MediaWiki;

-- 1
SELECT user_name, user_real_name, user_editcount
FROM user u
ORDER BY u.user_editcount ASC;

-- 3
SELECT COUNT(*) anzahlAenderungen, EXTRACT(HOUR FROM rev_timestamp) stunde
FROM revision
GROUP BY stunde
ORDER BY stunde ASC;

-- 4
SELECT page_title, COUNT(page_title) ausgehendeLinks
FROM page p
JOIN pagelinks pl ON p.page_id = pl.pl_from
GROUP BY page_title

-- 5
SELECT pl_title, COUNT(pl_title) eingehendeLinks
FROM pagelinks pl, page p
WHERE pl.pl_from = p.page_id
GROUP BY pl.pl_title
ORDER BY eingehendelinks DESC
